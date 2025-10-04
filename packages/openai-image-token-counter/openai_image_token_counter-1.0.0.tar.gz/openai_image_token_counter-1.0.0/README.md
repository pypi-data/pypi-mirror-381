# OpenAI API Image Token Counter

A comprehensive Python package for calculating token costs when using images with OpenAI's Vision API. Supports all OpenAI vision models including GPT-4.1, GPT-4o, o-series, and GPT Image 1.

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- **Complete Model Support**: All OpenAI vision models (GPT-4.1, GPT-4o, o-series, GPT Image 1)
- **Accurate Calculations**: Implements official OpenAI token calculation algorithms
- **Flexible Input**: Calculate from file paths, image dimensions, or raw image data
- **Batch Processing**: Process multiple images or entire directories
- **CLI Interface**: Easy-to-use command-line tool
- **Cost Estimation**: Estimate USD costs based on token pricing
- **Configurable**: Easy-to-update configuration via MDX file
- **Comprehensive Testing**: Full test suite covering all documented examples

## 📦 Installation

```bash
pip install openai-image-token-counter
```

### Development Installation

```bash
git clone https://github.com/edujbarrios/openai-image-token-counter.git
cd openai-image-token-counter
pip install -e .
```

## 🏃 Quick Start

### Python API

```python
from openai_image_token_counter import OpenAIImageTokenCalculator, ModelType, DetailLevel

# Initialize calculator
calculator = OpenAIImageTokenCalculator()

# Calculate tokens from image file
tokens = calculator.calculate_tokens_from_file(
    "my_image.jpg", 
    model=ModelType.GPT_4O,
    detail=DetailLevel.HIGH
)
print(f"Tokens required: {tokens}")

# Calculate from dimensions
tokens = calculator.calculate_tokens(
    width=1024, 
    height=1024, 
    model="gpt-4o"
)
print(f"Tokens for 1024x1024 image: {tokens}")

# Batch processing for different images
image_files = ["img1.jpg", "img2.png", "img3.gif"]
token_counts = calculator.calculate_batch_tokens(
    image_files, 
    model=ModelType.GPT_4O
)

# OPTIMIZED: Batch processing for same-resolution images (much faster!)
batch_result = calculator.calculate_batch_same_resolution(
    count=1000,          # Number of images
    width=1024,          # All images are 1024px wide
    height=1024,         # All images are 1024px tall
    model="gpt-4o"
)
print(f"1000 images at 1024x1024: {batch_result['total_tokens']:,} tokens")
print(f"Per image: {batch_result['tokens_per_image']} tokens")

# Batch processing with cost estimation
cost_result = calculator.calculate_batch_same_resolution_with_cost(
    count=500,
    width=512, 
    height=512,
    model="gpt-4o",
    input_token_price_per_million=5.0  # $5 per million tokens
)
print(f"Total cost for 500 images: ${cost_result['total_cost_usd']:.2f}")
```

### Command Line Interface

```bash
# Calculate tokens for a single image
openai-image-tokens image.jpg --model gpt-4o

# Process multiple images
openai-image-tokens *.jpg --model gpt-4.1-mini --detail low

# Process entire directory
openai-image-tokens --directory ./images --model gpt-4o --recursive

# Calculate from dimensions
openai-image-tokens --dimensions 1920 1080 --model o4-mini

# Estimate costs
openai-image-tokens image.jpg --model gpt-4o --price-per-million 5.0

# List supported models
openai-image-tokens --list-models
```

## 🧮 Supported Models

### 32px Patch Models (GPT-4.1/o4-mini family)
- `gpt-5-mini` (multiplier: 1.62)
- `gpt-5-nano` (multiplier: 2.46) 
- `gpt-4.1-mini` (multiplier: 1.62)
- `gpt-4.1-nano` (multiplier: 2.46)
- `o4-mini` (multiplier: 1.72)

### 512px Tile Models (GPT-4o/o-series family)
- `gpt-5` (base: 70, tile: 140)
- `gpt-5-chat-latest` (base: 70, tile: 140)
- `gpt-4o` (base: 85, tile: 170)
- `gpt-4.1` (base: 85, tile: 170)
- `gpt-4.5` (base: 85, tile: 170)
- `gpt-4o-mini` (base: 2833, tile: 5667)
- `o1` (base: 75, tile: 150)
- `o1-pro` (base: 75, tile: 150)
- `o3` (base: 75, tile: 150)
- `computer-use-preview` (base: 65, tile: 129)

### Special Models
- `gpt-image-1` (with fidelity bonuses)

## 🧪 Calculation Examples

### Example 1: 1024x1024 Image (GPT-4o)

```python
calculator = OpenAIImageTokenCalculator()
tokens = calculator.calculate_tokens(1024, 1024, "gpt-4o", DetailLevel.HIGH)
# Result: 765 tokens
# Calculation: 4 tiles of 512px → 85 + (4 × 170) = 765
```

### Example 2: 1800x2400 Image (GPT-4.1-mini)

```python
tokens = calculator.calculate_tokens(1800, 2400, "gpt-4.1-mini")
# Result: 2352 tokens  
# Calculation: Scaled to 1452 base tokens × 1.62 multiplier = 2352
```

### Example 3: Batch Processing for Dataset

```python
# Perfect for ML datasets where all images are preprocessed to same size
from openai_image_token_counter import calculate_batch_same_resolution, quick_batch_cost_estimate

# Calculate for 10,000 training images at 224x224
result = calculate_batch_same_resolution(10000, 224, 224, "gpt-4o")
print(f"Training set: {result['total_tokens']:,} tokens")

# Estimate cost for inference on 50,000 images at 512x512
cost_info = quick_batch_cost_estimate(50000, 512, 512, "gpt-4o", 5.0)
print(f"Inference cost: ${cost_info['total_cost_usd']:.2f}")
```

### Example 4: GPT Image 1 with High Fidelity

```python
from openai_image_token_counter import FidelityLevel

tokens = calculator.calculate_tokens(
    1024, 2048, 
    "gpt-image-1", 
    fidelity=FidelityLevel.HIGH
)
# Includes fidelity bonus for rectangular image
```

### Example 5: Comparing Costs Across Models

```python
# Compare costs for the same batch across different models
models = ["gpt-4o", "gpt-4.1-mini", "o4-mini"]
image_count = 1000
width, height = 1024, 1024

for model in models:
    result = calculate_batch_same_resolution(image_count, width, height, model)
    print(f"{model}: {result['total_tokens']:,} tokens ({result['tokens_per_image']} per image)")
```


## 📊 CLI Usage Examples

### Basic Usage

```bash
# Single image
openai-image-tokens photo.jpg --model gpt-4o
```

### Batch Processing

```bash
# Multiple specific files
openai-image-tokens img1.jpg img2.png img3.gif --model gpt-4o

# Entire directory
openai-image-tokens --directory ./photos --model gpt-4o --recursive

# Specific file types
openai-image-tokens --directory ./photos --extensions .jpg .png --model gpt-4o

# OPTIMIZED: Same resolution batch (much faster!)
openai-image-tokens --batch-same-resolution 1000 1024 1024 --model gpt-4o

# Large batch with different models
openai-image-tokens --batch-same-resolution 5000 512 512 --model gpt-4.1-mini
openai-image-tokens --batch-same-resolution 10000 256 256 --model o4-mini
```

### Output Formats

```bash
# JSON output
openai-image-tokens image.jpg --model gpt-4o --format json

# CSV output  
openai-image-tokens --directory ./images --format csv --output results.csv

# Detailed table
openai-image-tokens image.jpg --model gpt-4o --verbose
```

### Cost Estimation

```bash
# Estimate costs (price per million tokens)
openai-image-tokens image.jpg --model gpt-4o --price-per-million 5.0

# Batch cost estimation
openai-image-tokens --directory ./images --model gpt-4o --price-per-million 5.0
```

## 🔄 Model Algorithm Overview

### 32px Patch Models
1. Calculate patches: `ceil(width/32) × ceil(height/32)`
2. If > 1536 patches, scale down maintaining aspect ratio
3. Apply model-specific multiplier

### 512px Tile Models  
1. **Low detail**: Return base tokens only
2. **High detail**: 
   - Scale to fit 2048×2048 if needed
   - Scale shortest side to 768px
   - Count 512px tiles
   - Calculate: `base_tokens + (tiles × tile_tokens)`

### GPT Image 1
- Similar to 512px tile models but shortest side scaled to 512px
- High fidelity adds bonus: 4160 (square) or 6240 (rectangular)


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Based on official OpenAI Vision API documentation
- Calculation algorithms verified against OpenAI's examples
- Inspired by the need for accurate cost estimation in AI applications

**Note**: This package implements the token calculation algorithms as documented by OpenAI. Always verify costs with the official OpenAI pricing page before making financial decisions.

# Author
**Eduardo J. Barrios** - [https://edujbarrios.com](https://edujbarrios.com)