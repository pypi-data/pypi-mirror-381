"""
Model definitions and constants for OpenAI Image Token Counter
"""

from enum import Enum
from typing import Dict, NamedTuple


class ModelType(Enum):
    """Supported OpenAI model types"""
    GPT_5_MINI = "gpt-5-mini"
    GPT_5_NANO = "gpt-5-nano"
    GPT_4_1_MINI = "gpt-4.1-mini"
    GPT_4_1_NANO = "gpt-4.1-nano"
    O4_MINI = "o4-mini"
    
    GPT_5 = "gpt-5"
    GPT_5_CHAT_LATEST = "gpt-5-chat-latest"
    GPT_4O = "gpt-4o"
    GPT_4_1 = "gpt-4.1"
    GPT_4_5 = "gpt-4.5"
    GPT_4O_MINI = "gpt-4o-mini"
    O1 = "o1"
    O1_PRO = "o1-pro"
    O3 = "o3"
    COMPUTER_USE_PREVIEW = "computer-use-preview"
    
    GPT_IMAGE_1 = "gpt-image-1"


class DetailLevel(Enum):
    """Detail level for image processing"""
    LOW = "low"
    HIGH = "high"


class FidelityLevel(Enum):
    """Fidelity level for GPT Image 1"""
    LOW = "low"
    HIGH = "high"


class ModelConfig(NamedTuple):
    """Configuration for a specific model"""
    calculation_method: str  # "patch_32", "tile_512", or "image_1"
    multiplier: float = 1.0
    base_tokens: int = 0
    tile_tokens: int = 0


def get_model_configs() -> Dict[ModelType, ModelConfig]:
    """
    Load model configurations from MDX config file
    
    Returns:
        Dictionary mapping ModelType to ModelConfig
    """
    from .config_loader import get_config_loader
    
    loader = get_config_loader()
    config = loader.load_config()
    
    model_configs = {}
    
    # Load 32px patch models
    for model_name, model_data in config['patch_32_models'].items():
        try:
            model_type = ModelType(model_name)
            model_configs[model_type] = ModelConfig(
                calculation_method=model_data['calculation_method'],
                multiplier=model_data['multiplier']
            )
        except ValueError:
            # Skip unknown model types
            continue
    
    # Load 512px tile models
    for model_name, model_data in config['tile_512_models'].items():
        try:
            model_type = ModelType(model_name)
            model_configs[model_type] = ModelConfig(
                calculation_method=model_data['calculation_method'],
                base_tokens=model_data['base_tokens'],
                tile_tokens=model_data['tile_tokens']
            )
        except ValueError:
            # Skip unknown model types
            continue
    
    # Load GPT Image 1
    gpt_image_1_data = config['gpt_image_1']
    model_configs[ModelType.GPT_IMAGE_1] = ModelConfig(
        calculation_method=gpt_image_1_data['calculation_method'],
        base_tokens=gpt_image_1_data['base_tokens'],
        tile_tokens=gpt_image_1_data['tile_tokens']
    )
    
    return model_configs


# Global cache for model configurations
_MODEL_CONFIGS = None

def get_model_config(model_type: ModelType) -> ModelConfig:
    """Get configuration for a specific model type"""
    global _MODEL_CONFIGS
    if _MODEL_CONFIGS is None:
        _MODEL_CONFIGS = get_model_configs()
    
    if model_type not in _MODEL_CONFIGS:
        raise ValueError(f"Unsupported model: {model_type}")
    
    return _MODEL_CONFIGS[model_type]


def reload_model_configs():
    """Force reload of model configurations from file"""
    global _MODEL_CONFIGS
    _MODEL_CONFIGS = None