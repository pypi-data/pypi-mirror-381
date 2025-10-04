"""
Utility functions for image processing and batch operations
"""

from typing import List, Dict, Union, Tuple, Optional
from pathlib import Path
import mimetypes
from PIL import Image

from .models import ModelType, DetailLevel, FidelityLevel


def get_image_dimensions(image_path: Union[str, Path]) -> Tuple[int, int]:
    """
    Get image dimensions without fully loading the image
    
    Args:
        image_path: Path to image file
        
    Returns:
        Tuple of (width, height) in pixels
        
    Raises:
        FileNotFoundError: If image file doesn't exist
        ValueError: If file is not a valid image
    """
    image_path = Path(image_path)
    
    if not image_path.exists():
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    try:
        with Image.open(image_path) as img:
            return img.size
    except Exception as e:
        raise ValueError(f"Error reading image {image_path}: {e}")


def is_image_file(file_path: Union[str, Path]) -> bool:
    """
    Check if a file is likely an image based on its extension
    
    Args:
        file_path: Path to check
        
    Returns:
        True if file appears to be an image
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        return False
    
    mime_type, _ = mimetypes.guess_type(str(file_path))
    return mime_type is not None and mime_type.startswith('image/')


def find_images_in_directory(
    directory: Union[str, Path], 
    recursive: bool = True,
    supported_extensions: Optional[List[str]] = None
) -> List[Path]:
    """
    Find all image files in a directory
    
    Args:
        directory: Directory to search
        recursive: Whether to search subdirectories
        supported_extensions: List of extensions to include (e.g., ['.jpg', '.png'])
                            If None, uses common image extensions
        
    Returns:
        List of image file paths
    """
    directory = Path(directory)
    
    if not directory.exists() or not directory.is_dir():
        return []
    
    if supported_extensions is None:
        supported_extensions = [
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', 
            '.webp', '.svg', '.ico', '.psd', '.raw'
        ]
    
    # Convert to lowercase for case-insensitive matching
    supported_extensions = [ext.lower() for ext in supported_extensions]
    
    images = []
    
    if recursive:
        pattern = "**/*"
    else:
        pattern = "*"
    
    for file_path in directory.glob(pattern):
        if (file_path.is_file() and 
            file_path.suffix.lower() in supported_extensions and
            is_image_file(file_path)):
            images.append(file_path)
    
    return sorted(images)


def batch_process_directory(
    directory: Union[str, Path],
    model: Union[ModelType, str],
    detail: DetailLevel = DetailLevel.HIGH,
    fidelity: FidelityLevel = FidelityLevel.LOW,
    recursive: bool = True
) -> Dict[str, int]:
    """
    Calculate tokens for all images in a directory
    
    Args:
        directory: Directory containing images
        model: OpenAI model type
        detail: Detail level for tile-based models
        fidelity: Fidelity level for GPT Image 1
        recursive: Whether to search subdirectories
        
    Returns:
        Dictionary mapping file paths to token counts
    """
    from .calculator import OpenAIImageTokenCalculator
    
    calculator = OpenAIImageTokenCalculator()
    images = find_images_in_directory(directory, recursive)
    
    results = {}
    
    for image_path in images:
        try:
            tokens = calculator.calculate_tokens_from_file(
                image_path, model, detail, fidelity
            )
            results[str(image_path)] = tokens
        except Exception as e:
            # Store error information
            results[str(image_path)] = f"Error: {e}"
    
    return results


def format_results_table(
    results: Dict[str, Union[int, str]],
    include_totals: bool = True
) -> str:
    """
    Format calculation results as a readable table
    
    Args:
        results: Dictionary mapping file paths to token counts or error messages
        include_totals: Whether to include summary totals
        
    Returns:
        Formatted table string
    """
    if not results:
        return "No results to display"
    
    # Calculate column widths
    max_path_length = max(len(str(Path(path).name)) for path in results.keys())
    max_tokens_length = max(len(str(tokens)) for tokens in results.values())
    
    # Ensure minimum column widths
    path_width = max(max_path_length, 20)
    tokens_width = max(max_tokens_length, 10)
    
    # Create table
    lines = []
    lines.append("=" * (path_width + tokens_width + 7))
    lines.append(f"{'Image File':<{path_width}} | {'Tokens':>{tokens_width}}")
    lines.append("=" * (path_width + tokens_width + 7))
    
    total_tokens = 0
    total_files = 0
    error_count = 0
    
    for file_path, tokens in results.items():
        file_name = Path(file_path).name
        
        if isinstance(tokens, int):
            lines.append(f"{file_name:<{path_width}} | {tokens:>{tokens_width},}")
            total_tokens += tokens
            total_files += 1
        else:
            lines.append(f"{file_name:<{path_width}} | {'ERROR':>{tokens_width}}")
            error_count += 1
    
    if include_totals and total_files > 0:
        lines.append("-" * (path_width + tokens_width + 7))
        lines.append(f"{'TOTAL':<{path_width}} | {total_tokens:>{tokens_width},}")
        
        if error_count > 0:
            lines.append(f"{'ERRORS':<{path_width}} | {error_count:>{tokens_width}}")
    
    lines.append("=" * (path_width + tokens_width + 7))
    
    return "\n".join(lines)


def estimate_processing_time(
    num_images: int, 
    avg_file_size_mb: float = 2.0
) -> str:
    """
    Estimate processing time for a batch of images
    
    Args:
        num_images: Number of images to process
        avg_file_size_mb: Average file size in MB
        
    Returns:
        Human-readable time estimate
    """
    # Rough estimates based on file I/O and PIL processing
    time_per_image_seconds = 0.1 + (avg_file_size_mb * 0.05)
    total_seconds = num_images * time_per_image_seconds
    
    if total_seconds < 60:
        return f"~{total_seconds:.1f} seconds"
    elif total_seconds < 3600:
        minutes = total_seconds / 60
        return f"~{minutes:.1f} minutes"
    else:
        hours = total_seconds / 3600
        return f"~{hours:.1f} hours"