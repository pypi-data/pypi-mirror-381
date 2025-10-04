"""
Comprehensive tests for OpenAI Image Token Calculator

These tests verify all the documented calculation examples from OpenAI's documentation.
"""

import unittest
import sys
from pathlib import Path

# Add the package to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from openai_image_token_counter import OpenAIImageTokenCalculator, ModelType, DetailLevel, FidelityLevel


class TestPatch32Models(unittest.TestCase):
    """Test cases for 32px patch-based models (GPT-4.1/o4-mini family)"""
    
    def setUp(self):
        self.calculator = OpenAIImageTokenCalculator()
    
    def test_1024x1024_image_gpt4_1_mini(self):
        """
        Test Example 1 from documentation:
        A 1024 x 1024 image is 1024 tokens for GPT-4.1-mini
        """
        tokens = self.calculator.calculate_tokens(
            width=1024, 
            height=1024, 
            model=ModelType.GPT_4_1_MINI
        )
        
        # Base calculation: ceil(1024/32) * ceil(1024/32) = 32 * 32 = 1024
        # Multiplier for GPT-4.1-mini: 1.62
        expected = int(1024 * 1.62)
        self.assertEqual(tokens, expected)
    
    def test_1800x2400_image_scaling(self):
        """
        Test Example 2 from documentation:
        A 1800 x 2400 image requires scaling and results in 1452 base tokens
        """
        # Test with GPT-4.1-mini (multiplier 1.62)
        tokens = self.calculator.calculate_tokens(
            width=1800, 
            height=2400, 
            model=ModelType.GPT_4_1_MINI
        )
        
        # The documentation shows 1452 base tokens before multiplier
        # With multiplier 1.62: 1452 * 1.62 = 2352.24 -> 2352
        expected = int(1452 * 1.62)
        self.assertEqual(tokens, expected)
    
    def test_different_multipliers(self):
        """Test that different models apply different multipliers correctly"""
        width, height = 1024, 1024
        base_tokens = 1024  # 32*32 patches
        
        # Test GPT-5-mini (1.62 multiplier)
        tokens_5_mini = self.calculator.calculate_tokens(
            width, height, ModelType.GPT_5_MINI
        )
        self.assertEqual(tokens_5_mini, int(base_tokens * 1.62))
        
        # Test GPT-5-nano (2.46 multiplier)  
        tokens_5_nano = self.calculator.calculate_tokens(
            width, height, ModelType.GPT_5_NANO
        )
        self.assertEqual(tokens_5_nano, int(base_tokens * 2.46))
        
        # Test o4-mini (1.72 multiplier)
        tokens_o4_mini = self.calculator.calculate_tokens(
            width, height, ModelType.O4_MINI
        )
        self.assertEqual(tokens_o4_mini, int(base_tokens * 1.72))


class TestTile512Models(unittest.TestCase):
    """Test cases for 512px tile-based models (GPT-4o/o-series family)"""
    
    def setUp(self):
        self.calculator = OpenAIImageTokenCalculator()
    
    def test_low_detail_mode(self):
        """Test that low detail mode returns only base tokens"""
        tokens = self.calculator.calculate_tokens(
            width=2048, 
            height=4096, 
            model=ModelType.GPT_4O,
            detail=DetailLevel.LOW
        )
        
        # For GPT-4o, base_tokens = 85
        self.assertEqual(tokens, 85)
    
    def test_1024x1024_high_detail_gpt4o(self):
        """
        Test Example 3 from documentation:
        A 1024 x 1024 square image in "high" mode costs 765 tokens for GPT-4o
        """
        tokens = self.calculator.calculate_tokens(
            width=1024, 
            height=1024, 
            model=ModelType.GPT_4O,
            detail=DetailLevel.HIGH
        )
        
        # Expected calculation:
        # 1. No initial resize (1024 < 2048)
        # 2. Scale to 768x768 (shortest side = 768)
        # 3. 4 tiles of 512px needed
        # 4. 170 * 4 + 85 = 765
        self.assertEqual(tokens, 765)
    
    def test_2048x4096_high_detail_gpt4o(self):
        """
        Test Example 4 from documentation:
        A 2048 x 4096 image in "high" mode costs 1105 tokens for GPT-4o
        """
        tokens = self.calculator.calculate_tokens(
            width=2048, 
            height=4096, 
            model=ModelType.GPT_4O,
            detail=DetailLevel.HIGH
        )
        
        # Expected calculation:
        # 1. Scale down to 1024x2048 (to fit 2048 square)
        # 2. Scale to 768x1536 (shortest side = 768)  
        # 3. 6 tiles of 512px needed
        # 4. 170 * 6 + 85 = 1105
        self.assertEqual(tokens, 1105)
    
    def test_different_tile_models(self):
        """Test different tile-based models with same image"""
        width, height = 1024, 1024
        
        # All should have 4 tiles, but different base and tile costs
        
        # GPT-4o: base=85, tile=170 -> 85 + (4*170) = 765
        tokens_4o = self.calculator.calculate_tokens(
            width, height, ModelType.GPT_4O, DetailLevel.HIGH
        )
        self.assertEqual(tokens_4o, 765)
        
        # GPT-5: base=70, tile=140 -> 70 + (4*140) = 630
        tokens_5 = self.calculator.calculate_tokens(
            width, height, ModelType.GPT_5, DetailLevel.HIGH
        )
        self.assertEqual(tokens_5, 630)
        
        # o1: base=75, tile=150 -> 75 + (4*150) = 675
        tokens_o1 = self.calculator.calculate_tokens(
            width, height, ModelType.O1, DetailLevel.HIGH
        )
        self.assertEqual(tokens_o1, 675)


class TestGPTImage1(unittest.TestCase):
    """Test cases for GPT Image 1 model"""
    
    def setUp(self):
        self.calculator = OpenAIImageTokenCalculator()
    
    def test_low_fidelity(self):
        """Test GPT Image 1 with low fidelity (no bonus)"""
        tokens = self.calculator.calculate_tokens(
            width=1024, 
            height=1024, 
            model=ModelType.GPT_IMAGE_1,
            fidelity=FidelityLevel.LOW
        )
        
        # Base calculation with 512px shortest side:
        # Scale 1024x1024 to 512x512, then 4 tiles
        # 65 + (4 * 129) = 581
        self.assertEqual(tokens, 581)
    
    def test_high_fidelity_square(self):
        """Test GPT Image 1 with high fidelity on square image"""
        tokens = self.calculator.calculate_tokens(
            width=1024, 
            height=1024, 
            model=ModelType.GPT_IMAGE_1,
            fidelity=FidelityLevel.HIGH
        )
        
        # Base: 581 (from above)
        # Square bonus (aspect ratio 1.0 <= 1.2): +4160
        # Total: 581 + 4160 = 4741
        self.assertEqual(tokens, 4741)
    
    def test_high_fidelity_rectangular(self):
        """Test GPT Image 1 with high fidelity on rectangular image"""
        tokens = self.calculator.calculate_tokens(
            width=1024, 
            height=2048, 
            model=ModelType.GPT_IMAGE_1,
            fidelity=FidelityLevel.HIGH
        )
        
        # Aspect ratio: 2048/1024 = 2.0 > 1.2, so rectangular bonus
        # Base calculation: scale to 512x1024, then 6 tiles
        # Base: 65 + (6 * 129) = 839
        # Rectangular bonus: +6240
        # Total: 839 + 6240 = 7079
        self.assertEqual(tokens, 7079)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error conditions"""
    
    def setUp(self):
        self.calculator = OpenAIImageTokenCalculator()
    
    def test_very_small_image(self):
        """Test very small image (smaller than patch/tile size)"""
        tokens = self.calculator.calculate_tokens(
            width=16, 
            height=16, 
            model=ModelType.GPT_4_1_MINI
        )
        
        # Should still require 1 patch: ceil(16/32) * ceil(16/32) = 1 * 1 = 1
        # With multiplier 1.62: 1 * 1.62 = 1.62 -> 1
        self.assertEqual(tokens, 1)
    
    def test_very_large_image_32px(self):
        """Test very large image with 32px model (should trigger scaling)"""
        tokens = self.calculator.calculate_tokens(
            width=3200, 
            height=3200, 
            model=ModelType.GPT_4_1_MINI
        )
        
        # Raw patches: ceil(3200/32) * ceil(3200/32) = 100 * 100 = 10000
        # Exceeds 1536, so should be scaled down and capped
        # Result should be <= 1536 * 1.62
        max_expected = int(1536 * 1.62)
        self.assertLessEqual(tokens, max_expected)
    
    def test_string_model_names(self):
        """Test using string model names instead of enum"""
        tokens = self.calculator.calculate_tokens(
            width=1024, 
            height=1024, 
            model="gpt-4o"
        )
        
        # Should be same as using ModelType.GPT_4O
        tokens_enum = self.calculator.calculate_tokens(
            width=1024, 
            height=1024, 
            model=ModelType.GPT_4O
        )
        
        self.assertEqual(tokens, tokens_enum)
    
    def test_invalid_model(self):
        """Test error handling for invalid model"""
        with self.assertRaises(ValueError):
            self.calculator.calculate_tokens(
                width=1024, 
                height=1024, 
                model="invalid-model"
            )


class TestUtilityFunctions(unittest.TestCase):
    """Test utility and helper functions"""
    
    def setUp(self):
        self.calculator = OpenAIImageTokenCalculator()
    
    def test_list_supported_models(self):
        """Test listing supported models"""
        models = self.calculator.list_supported_models()
        
        # Should include all our test models
        expected_models = [
            "gpt-4o", "gpt-4.1-mini", "gpt-5-mini", 
            "o4-mini", "gpt-image-1", "o1"
        ]
        
        for model in expected_models:
            self.assertIn(model, models)
    
    def test_get_model_info(self):
        """Test getting model information"""
        info = self.calculator.get_model_info(ModelType.GPT_4O)
        
        expected_keys = [
            "model", "calculation_method", "multiplier", 
            "base_tokens", "tile_tokens"
        ]
        
        for key in expected_keys:
            self.assertIn(key, info)
        
        self.assertEqual(info["model"], "gpt-4o")
        self.assertEqual(info["calculation_method"], "tile_512")
        self.assertEqual(info["base_tokens"], 85)
        self.assertEqual(info["tile_tokens"], 170)
    
    def test_estimate_cost_usd(self):
        """Test USD cost estimation"""
        tokens = 1000
        price_per_million = 5.0  # $5 per million tokens
        
        cost = self.calculator.estimate_cost_usd(
            tokens, ModelType.GPT_4O, price_per_million
        )
        
        expected = (1000 / 1_000_000) * 5.0
        self.assertEqual(cost, expected)


if __name__ == "__main__":
    # Run all tests
    unittest.main(verbosity=2)