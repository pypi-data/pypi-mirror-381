"""
Configuration loader for reading token calculation rules from MDX file
"""

import re
import yaml
from pathlib import Path
from typing import Dict, Any, NamedTuple
from enum import Enum

from .models import ModelType


class ConfigLoader:
    """Loads and parses token configuration from MDX file"""
    
    def __init__(self, config_file: Path = None):
        if config_file is None:
            # Default to token_config.mdx in package root
            package_root = Path(__file__).parent.parent
            config_file = package_root / "token_config.mdx"
        
        self.config_file = Path(config_file)
        self._config_cache = None
    
    def load_config(self) -> Dict[str, Any]:
        """Load and parse the MDX configuration file"""
        if self._config_cache is not None:
            return self._config_cache
        
        if not self.config_file.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_file}")
        
        content = self.config_file.read_text(encoding='utf-8')
        
        # Extract YAML blocks from MDX
        config = {
            'patch_32_models': self._extract_yaml_block(content, 'patch_32_models'),
            'tile_512_models': self._extract_yaml_block(content, 'tile_512_models'),
            'gpt_image_1': self._extract_yaml_block(content, 'gpt_image_1'),
            'limits': self._extract_yaml_block(content, 'limits'),
        }
        
        self._config_cache = config
        return config
    
    def _extract_yaml_block(self, content: str, block_name: str) -> Dict[str, Any]:
        """Extract a specific YAML block from the MDX content"""
        # Pattern to match YAML blocks
        pattern = rf'```yaml\s*\n{re.escape(block_name)}:(.*?)\n```'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            return {}
        
        yaml_content = f"{block_name}:" + match.group(1)
        
        try:
            parsed = yaml.safe_load(yaml_content)
            return parsed.get(block_name, {})
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML block '{block_name}': {e}")
    
    def get_model_config(self, model_name: str) -> Dict[str, Any]:
        """Get configuration for a specific model"""
        config = self.load_config()
        
        # Check each model category
        for category in ['patch_32_models', 'tile_512_models']:
            if model_name in config[category]:
                return config[category][model_name]
        
        # Check GPT Image 1
        if model_name == 'gpt-image-1':
            return config['gpt_image_1']
        
        raise ValueError(f"Model configuration not found: {model_name}")
    
    def get_limits(self) -> Dict[str, Any]:
        """Get configuration limits"""
        config = self.load_config()
        return config.get('limits', {})
    
    def list_all_models(self) -> Dict[str, str]:
        """Get all models and their calculation methods"""
        config = self.load_config()
        models = {}
        
        for model_name, model_config in config['patch_32_models'].items():
            models[model_name] = model_config['calculation_method']
        
        for model_name, model_config in config['tile_512_models'].items():
            models[model_name] = model_config['calculation_method']
        
        models['gpt-image-1'] = config['gpt_image_1']['calculation_method']
        
        return models
    
    def validate_config(self) -> bool:
        """Validate that the configuration is complete and correct"""
        try:
            config = self.load_config()
            
            # Check required sections
            required_sections = ['patch_32_models', 'tile_512_models', 'gpt_image_1', 'limits']
            for section in required_sections:
                if section not in config:
                    raise ValueError(f"Missing required section: {section}")
            
            # Validate patch_32_models
            for model_name, model_config in config['patch_32_models'].items():
                required_fields = ['multiplier', 'calculation_method']
                for field in required_fields:
                    if field not in model_config:
                        raise ValueError(f"Missing field '{field}' in patch_32_models.{model_name}")
                
                if model_config['calculation_method'] != 'patch_32':
                    raise ValueError(f"Invalid calculation_method for {model_name}")
            
            # Validate tile_512_models
            for model_name, model_config in config['tile_512_models'].items():
                required_fields = ['base_tokens', 'tile_tokens', 'calculation_method']
                for field in required_fields:
                    if field not in model_config:
                        raise ValueError(f"Missing field '{field}' in tile_512_models.{model_name}")
                
                if model_config['calculation_method'] != 'tile_512':
                    raise ValueError(f"Invalid calculation_method for {model_name}")
            
            # Validate gpt_image_1
            gpt_image_1 = config['gpt_image_1']
            required_fields = ['base_tokens', 'tile_tokens', 'calculation_method', 'fidelity_bonuses']
            for field in required_fields:
                if field not in gpt_image_1:
                    raise ValueError(f"Missing field '{field}' in gpt_image_1")
            
            fidelity_bonuses = gpt_image_1['fidelity_bonuses']
            if 'square' not in fidelity_bonuses or 'rectangular' not in fidelity_bonuses:
                raise ValueError("Missing fidelity bonuses in gpt_image_1")
            
            # Validate limits
            limits = config['limits']
            required_limits = [
                'max_patches_32px', 'max_dimension_512px', 'shortest_side_512px',
                'shortest_side_image1', 'patch_size_32px', 'tile_size_512px'
            ]
            for limit in required_limits:
                if limit not in limits:
                    raise ValueError(f"Missing limit: {limit}")
            
            return True
            
        except Exception as e:
            print(f"Configuration validation failed: {e}")
            return False
    
    def reload_config(self):
        """Force reload of configuration from file"""
        self._config_cache = None
        return self.load_config()


# Global config loader instance
_config_loader = None

def get_config_loader() -> ConfigLoader:
    """Get the global configuration loader instance"""
    global _config_loader
    if _config_loader is None:
        _config_loader = ConfigLoader()
    return _config_loader


def reload_config():
    """Reload configuration from file"""
    global _config_loader
    if _config_loader is not None:
        _config_loader.reload_config()