"""
Main calculator class providing unified interface for all OpenAI models
"""

from typing import Union, List, Tuple, Optional
from pathlib import Path
from PIL import Image
import io

from .models import ModelType, DetailLevel, FidelityLevel, get_model_config
from .calculators import Patch32Calculator, Tile512Calculator, GPTImage1Calculator


class OpenAIImageTokenCalculator:
    """
    Main calculator class for OpenAI image token costs
    
    Supports all OpenAI vision models including:
    - GPT-4.1/o4-mini family (32px patches)
    - GPT-4o/o-series family (512px tiles) 
    - GPT Image 1 (512px tiles with fidelity bonuses)
    """
    
    def __init__(self):
        self.patch_calculator = Patch32Calculator()
        self.tile_calculator = Tile512Calculator()
        self.image1_calculator = GPTImage1Calculator()
    
    def calculate_tokens(
        self, 
        width: int, 
        height: int, 
        model: Union[ModelType, str],
        detail: DetailLevel = DetailLevel.HIGH,
        fidelity: FidelityLevel = FidelityLevel.LOW
    ) -> int:
        """
        Calculate token cost for an image
        
        Args:
            width: Image width in pixels
            height: Image height in pixels  
            model: OpenAI model type
            detail: Detail level for tile-based models (ignored for patch-based)
            fidelity: Fidelity level for GPT Image 1 (ignored for other models)
            
        Returns:
            Number of tokens required
            
        Raises:
            ValueError: If model is not supported
        """
        # Convert string to ModelType if needed
        if isinstance(model, str):
            try:
                model = ModelType(model)
            except ValueError:
                raise ValueError(f"Unsupported model: {model}")
        
        try:
            config = get_model_config(model)
        except ValueError:
            raise ValueError(f"Unsupported model: {model}")
        
        if config.calculation_method == "patch_32":
            return self.patch_calculator.calculate_tokens(width, height, model)
        elif config.calculation_method == "tile_512":
            return self.tile_calculator.calculate_tokens(width, height, model, detail)
        elif config.calculation_method == "image_1":
            return self.image1_calculator.calculate_tokens(width, height, fidelity)
        else:
            raise ValueError(f"Unknown calculation method: {config.calculation_method}")
    
    def calculate_tokens_from_file(
        self, 
        image_path: Union[str, Path],
        model: Union[ModelType, str],
        detail: DetailLevel = DetailLevel.HIGH,
        fidelity: FidelityLevel = FidelityLevel.LOW
    ) -> int:
        """
        Calculate token cost from an image file
        
        Args:
            image_path: Path to image file
            model: OpenAI model type
            detail: Detail level for tile-based models
            fidelity: Fidelity level for GPT Image 1
            
        Returns:
            Number of tokens required
            
        Raises:
            FileNotFoundError: If image file doesn't exist
            ValueError: If image format is not supported
        """
        image_path = Path(image_path)
        
        if not image_path.exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                return self.calculate_tokens(width, height, model, detail, fidelity)
        except Exception as e:
            raise ValueError(f"Error processing image {image_path}: {e}")
    
    def calculate_tokens_from_bytes(
        self,
        image_data: bytes,
        model: Union[ModelType, str],
        detail: DetailLevel = DetailLevel.HIGH,
        fidelity: FidelityLevel = FidelityLevel.LOW
    ) -> int:
        """
        Calculate token cost from image bytes
        
        Args:
            image_data: Image data as bytes
            model: OpenAI model type
            detail: Detail level for tile-based models
            fidelity: Fidelity level for GPT Image 1
            
        Returns:
            Number of tokens required
            
        Raises:
            ValueError: If image format is not supported
        """
        try:
            with Image.open(io.BytesIO(image_data)) as img:
                width, height = img.size
                return self.calculate_tokens(width, height, model, detail, fidelity)
        except Exception as e:
            raise ValueError(f"Error processing image data: {e}")
    
    def calculate_batch_tokens(
        self,
        images: List[Union[str, Path, Tuple[int, int]]],
        model: Union[ModelType, str],
        detail: DetailLevel = DetailLevel.HIGH,
        fidelity: FidelityLevel = FidelityLevel.LOW
    ) -> List[int]:
        """
        Calculate token costs for multiple images
        
        Args:
            images: List of image paths, or (width, height) tuples
            model: OpenAI model type
            detail: Detail level for tile-based models
            fidelity: Fidelity level for GPT Image 1
            
        Returns:
            List of token costs for each image
        """
        results = []
        
        for image in images:
            if isinstance(image, tuple) and len(image) == 2:
                # Direct width, height tuple
                width, height = image
                tokens = self.calculate_tokens(width, height, model, detail, fidelity)
            else:
                # File path
                tokens = self.calculate_tokens_from_file(image, model, detail, fidelity)
            
            results.append(tokens)
        
        return results
    
    def calculate_batch_same_resolution(
        self,
        count: int,
        width: int,
        height: int,
        model: Union[ModelType, str],
        detail: DetailLevel = DetailLevel.HIGH,
        fidelity: FidelityLevel = FidelityLevel.LOW
    ) -> dict:
        """
        Calculate token costs for multiple images with the same resolution
        
        This is optimized for batch processing when you know all images have been
        rescaled to the same dimensions, so we only need to calculate once.
        
        Args:
            count: Number of images
            width: Width of all images in pixels
            height: Height of all images in pixels
            model: OpenAI model type
            detail: Detail level for tile-based models
            fidelity: Fidelity level for GPT Image 1
            
        Returns:
            Dictionary with calculation results:
            {
                'tokens_per_image': int,
                'total_images': int, 
                'total_tokens': int,
                'resolution': str,
                'model': str,
                'detail': str,
                'fidelity': str
            }
        """
        if count <= 0:
            raise ValueError("Count must be a positive integer")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers")
        
        # Calculate tokens for one image
        tokens_per_image = self.calculate_tokens(width, height, model, detail, fidelity)
        
        # Total tokens for all images
        total_tokens = tokens_per_image * count
        
        return {
            'tokens_per_image': tokens_per_image,
            'total_images': count,
            'total_tokens': total_tokens,
            'resolution': f"{width}x{height}",
            'model': str(model) if isinstance(model, ModelType) else model,
            'detail': detail.value,
            'fidelity': fidelity.value,
            'cost_per_image_usd': None,  # Will be filled if price provided
            'total_cost_usd': None       # Will be filled if price provided
        }
    
    def calculate_batch_same_resolution_with_cost(
        self,
        count: int,
        width: int,
        height: int,
        model: Union[ModelType, str],
        input_token_price_per_million: float,
        detail: DetailLevel = DetailLevel.HIGH,
        fidelity: FidelityLevel = FidelityLevel.LOW
    ) -> dict:
        """
        Calculate token costs and USD estimates for multiple images with same resolution
        
        Args:
            count: Number of images
            width: Width of all images in pixels
            height: Height of all images in pixels
            model: OpenAI model type
            input_token_price_per_million: Price per million input tokens in USD
            detail: Detail level for tile-based models
            fidelity: Fidelity level for GPT Image 1
            
        Returns:
            Dictionary with calculation results including cost estimates
        """
        result = self.calculate_batch_same_resolution(
            count, width, height, model, detail, fidelity
        )
        
        # Add cost calculations
        cost_per_image = self.estimate_cost_usd(
            result['tokens_per_image'], model, input_token_price_per_million
        )
        
        result['cost_per_image_usd'] = cost_per_image
        result['total_cost_usd'] = cost_per_image * count
        result['price_per_million_tokens'] = input_token_price_per_million
        
        return result
    
    def get_model_info(self, model: Union[ModelType, str]) -> dict:
        """
        Get information about a specific model
        
        Args:
            model: OpenAI model type
            
        Returns:
            Dictionary with model configuration information
        """
        if isinstance(model, str):
            model = ModelType(model)
        
        try:
            config = get_model_config(model)
        except ValueError:
            raise ValueError(f"Unsupported model: {model}")
        
        return {
            "model": model.value,
            "calculation_method": config.calculation_method,
            "multiplier": config.multiplier,
            "base_tokens": config.base_tokens,
            "tile_tokens": config.tile_tokens,
        }
    
    def list_supported_models(self) -> List[str]:
        """
        Get list of all supported model names
        
        Returns:
            List of supported model names
        """
        from .models import get_model_configs
        model_configs = get_model_configs()
        return [model.value for model in model_configs.keys()]
    
    @staticmethod
    def estimate_cost_usd(
        tokens: int, 
        model: Union[ModelType, str],
        input_token_price_per_million: Optional[float] = None
    ) -> float:
        """
        Estimate USD cost based on token count
        
        Args:
            tokens: Number of tokens
            model: Model type (for reference)
            input_token_price_per_million: Price per million input tokens in USD
                                         If None, returns 0.0 (price varies by model)
        
        Returns:
            Estimated cost in USD
        """
        if input_token_price_per_million is None:
            return 0.0
        
        return (tokens / 1_000_000) * input_token_price_per_million