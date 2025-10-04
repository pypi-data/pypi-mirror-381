"""
OpenAI Image Token Counter

A Python package for calculating token costs of images when using OpenAI's Vision API.
Supports all OpenAI models including GPT-4.1, GPT-4o, o-series, and GPT Image 1.
"""

from .calculator import OpenAIImageTokenCalculator
from .models import ModelType, DetailLevel, FidelityLevel

__version__ = "1.0.0"
__author__ = "OpenAI Image Token Counter"

__all__ = [
    "OpenAIImageTokenCalculator",
    "ModelType", 
    "DetailLevel",
    "FidelityLevel",
    "calculate_batch_same_resolution",
    "quick_batch_cost_estimate"
]

# Convenience functions for batch processing
def calculate_batch_same_resolution(
    count: int,
    width: int, 
    height: int,
    model: str,
    detail: str = "high",
    fidelity: str = "low"
):
    """
    Convenience function for calculating tokens for multiple same-resolution images
    
    Args:
        count: Number of images
        width: Image width in pixels
        height: Image height in pixels
        model: Model name (e.g., "gpt-4o")
        detail: Detail level ("low" or "high")
        fidelity: Fidelity level for GPT Image 1 ("low" or "high")
        
    Returns:
        Dictionary with calculation results
    """
    from .calculator import OpenAIImageTokenCalculator
    from .models import DetailLevel, FidelityLevel
    
    calculator = OpenAIImageTokenCalculator()
    detail_level = DetailLevel.HIGH if detail == "high" else DetailLevel.LOW
    fidelity_level = FidelityLevel.HIGH if fidelity == "high" else FidelityLevel.LOW
    
    return calculator.calculate_batch_same_resolution(
        count, width, height, model, detail_level, fidelity_level
    )


def quick_batch_cost_estimate(
    count: int,
    width: int,
    height: int, 
    model: str,
    price_per_million: float,
    detail: str = "high"
):
    """
    Quick cost estimation for batch of same-resolution images
    
    Args:
        count: Number of images
        width: Image width in pixels
        height: Image height in pixels
        model: Model name (e.g., "gpt-4o")
        price_per_million: Price per million tokens in USD
        detail: Detail level ("low" or "high")
        
    Returns:
        Dictionary with tokens and cost information
    """
    from .calculator import OpenAIImageTokenCalculator
    from .models import DetailLevel, FidelityLevel
    
    calculator = OpenAIImageTokenCalculator()
    detail_level = DetailLevel.HIGH if detail == "high" else DetailLevel.LOW
    
    return calculator.calculate_batch_same_resolution_with_cost(
        count, width, height, model, price_per_million, detail_level
    )