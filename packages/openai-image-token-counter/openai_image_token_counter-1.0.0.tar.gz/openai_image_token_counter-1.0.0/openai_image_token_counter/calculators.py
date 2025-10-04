"""
Calculator implementations for different OpenAI model types
"""

import math
from typing import Tuple, Union
from .models import ModelType, DetailLevel, FidelityLevel, get_model_config


class Patch32Calculator:
    """
    Calculator for models using 32px patches (GPT-4.1/o4-mini family)
    """
    
    @staticmethod
    def calculate_tokens(width: int, height: int, model: ModelType) -> int:
        """
        Calculate tokens for 32px patch-based models
        
        Args:
            width: Image width in pixels
            height: Image height in pixels
            model: The model type
            
        Returns:
            Number of tokens required
        """
        config = get_model_config(model)
        
        # Step A: Calculate raw patches needed
        raw_patches = math.ceil(width / 32) * math.ceil(height / 32)
        
        # Step B: If patches exceed 1536, scale down
        if raw_patches > 1536:
            # Calculate shrink factor
            r = math.sqrt(32**2 * 1536 / (width * height))
            
            # Apply additional scaling to ensure whole number of patches
            width_patches = width * r / 32
            height_patches = height * r / 32
            
            # Scale to fit width in whole patches
            width_scale = math.floor(width_patches) / width_patches
            height_scale = math.floor(height_patches) / height_patches
            
            # Use the more restrictive scaling
            final_scale = min(width_scale, height_scale)
            r = r * final_scale
            
            # Calculate final dimensions
            resized_width = int(width * r)
            resized_height = int(height * r)
            
            # Ensure dimensions align to patch boundaries
            resized_width = (resized_width // 32) * 32
            resized_height = (resized_height // 32) * 32
            
            # Step C: Calculate final patches
            image_tokens = math.ceil(resized_width / 32) * math.ceil(resized_height / 32)
        else:
            image_tokens = raw_patches
        
        # Step D: Apply model multiplier
        return int(image_tokens * config.multiplier)


class Tile512Calculator:
    """
    Calculator for models using 512px tiles (GPT-4o/o-series family)
    """
    
    @staticmethod
    def calculate_tokens(width: int, height: int, model: ModelType, detail: DetailLevel = DetailLevel.HIGH) -> int:
        """
        Calculate tokens for 512px tile-based models
        
        Args:
            width: Image width in pixels
            height: Image height in pixels
            model: The model type
            detail: Detail level (low or high)
            
        Returns:
            Number of tokens required
        """
        config = get_model_config(model)
        
        if detail == DetailLevel.LOW:
            return config.base_tokens
        
        # High detail calculation
        original_width, original_height = width, height
        
        # Step 1: Scale to fit in 2048x2048 square
        if width > 2048 or height > 2048:
            scale = min(2048 / width, 2048 / height)
            width = int(width * scale)
            height = int(height * scale)
        
        # Step 2: Scale so shortest side is 768px
        shortest_side = min(width, height)
        if shortest_side != 768:
            scale = 768 / shortest_side
            width = int(width * scale)
            height = int(height * scale)
        
        # Step 3: Count 512px tiles
        tiles_width = math.ceil(width / 512)
        tiles_height = math.ceil(height / 512)
        num_tiles = tiles_width * tiles_height
        
        # Step 4: Calculate total tokens
        return config.base_tokens + (num_tiles * config.tile_tokens)


class GPTImage1Calculator:
    """
    Calculator for GPT Image 1 model
    """
    
    @staticmethod
    def calculate_tokens(width: int, height: int, fidelity: FidelityLevel = FidelityLevel.LOW) -> int:
        """
        Calculate tokens for GPT Image 1
        
        Args:
            width: Image width in pixels  
            height: Image height in pixels
            fidelity: Fidelity level (low or high)
            
        Returns:
            Number of tokens required
        """
        config = get_model_config(ModelType.GPT_IMAGE_1)
        
        # Base calculation (similar to 512px tile models)
        original_width, original_height = width, height
        
        # Scale to fit in 2048x2048 square
        if width > 2048 or height > 2048:
            scale = min(2048 / width, 2048 / height)
            width = int(width * scale)
            height = int(height * scale)
        
        # Scale so shortest side is 768px (same as other 512px tile models)
        shortest_side = min(width, height)
        if shortest_side != 768:
            scale = 768 / shortest_side
            width = int(width * scale)
            height = int(height * scale)
        
        # Count 512px tiles
        tiles_width = math.ceil(width / 512)
        tiles_height = math.ceil(height / 512)
        num_tiles = tiles_width * tiles_height
        
        # Base token cost
        tokens = config.base_tokens + (num_tiles * config.tile_tokens)
        
        # Add fidelity bonus for high fidelity
        if fidelity == FidelityLevel.HIGH:
            # Determine aspect ratio
            aspect_ratio = max(original_width, original_height) / min(original_width, original_height)
            
            if aspect_ratio <= 1.2:  # Roughly square
                tokens += 4160
            else:  # Portrait or landscape
                tokens += 6240
        
        return tokens