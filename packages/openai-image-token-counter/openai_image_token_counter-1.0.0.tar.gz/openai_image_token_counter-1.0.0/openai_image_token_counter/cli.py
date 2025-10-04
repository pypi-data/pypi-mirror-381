#!/usr/bin/env python3
"""
Command-line interface for OpenAI Image Token Counter
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from . import OpenAIImageTokenCalculator, ModelType, DetailLevel, FidelityLevel
from .utils import (
    find_images_in_directory, 
    batch_process_directory, 
    format_results_table,
    estimate_processing_time
)


def create_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser"""
    
    parser = argparse.ArgumentParser(
        description="Calculate OpenAI API token costs for images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Calculate tokens for a single image
  openai-image-tokens image.jpg --model gpt-4o
  
  # Calculate for multiple images
  openai-image-tokens img1.jpg img2.png --model gpt-4o --detail low
  
  # Process entire directory
  openai-image-tokens --directory ./images --model gpt-4.1-mini --recursive
  
  # Calculate from dimensions
  openai-image-tokens --dimensions 1024 768 --model o4-mini
  
  # Calculate for batch of same-resolution images (OPTIMIZED)
  openai-image-tokens --batch-same-resolution 100 1024 1024 --model gpt-4o
  
  # Batch calculation with cost estimation
  openai-image-tokens --batch-same-resolution 500 512 512 --model gpt-4o --price-per-million 5.0
  
  # Estimate costs
  openai-image-tokens image.jpg --model gpt-4o --price-per-million 5.0
  
  # List supported models
  openai-image-tokens --list-models
        """
    )
    
    # Input options (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "images", 
        nargs="*", 
        help="Image file paths to analyze"
    )
    input_group.add_argument(
        "--directory", "-d",
        type=Path,
        help="Directory containing images to process"
    )
    input_group.add_argument(
        "--dimensions",
        nargs=2,
        type=int,
        metavar=("WIDTH", "HEIGHT"),
        help="Calculate tokens from image dimensions (width height)"
    )
    input_group.add_argument(
        "--batch-same-resolution",
        nargs=3,
        type=int,
        metavar=("COUNT", "WIDTH", "HEIGHT"),
        help="Calculate tokens for COUNT images with same resolution (count width height)"
    )
    input_group.add_argument(
        "--list-models",
        action="store_true",
        help="List all supported models and exit"
    )
    
    # Model configuration
    parser.add_argument(
        "--model", "-m",
        type=str,
        default="gpt-4o",
        help="OpenAI model to calculate for (default: gpt-4o)"
    )
    
    parser.add_argument(
        "--detail",
        choices=["low", "high"],
        default="high",
        help="Detail level for tile-based models (default: high)"
    )
    
    parser.add_argument(
        "--fidelity", 
        choices=["low", "high"],
        default="low",
        help="Fidelity level for GPT Image 1 (default: low)"
    )
    
    # Directory processing options
    parser.add_argument(
        "--recursive", "-r",
        action="store_true",
        help="Process directories recursively"
    )
    
    parser.add_argument(
        "--extensions",
        nargs="+",
        default=[".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
        help="Image file extensions to include (default: common formats)"
    )
    
    # Output options
    parser.add_argument(
        "--output", "-o",
        type=Path,
        help="Save results to file (CSV format)"
    )
    
    parser.add_argument(
        "--format",
        choices=["table", "json", "csv"],
        default="table",
        help="Output format (default: table)"
    )
    
    parser.add_argument(
        "--price-per-million",
        type=float,
        help="Price per million tokens in USD (for cost estimation)"
    )
    
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress progress messages"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed information"
    )
    
    return parser


def list_supported_models():
    """List all supported models"""
    calculator = OpenAIImageTokenCalculator()
    models = calculator.list_supported_models()
    
    print("Supported OpenAI Models:")
    print("=" * 40)
    
    # Group by calculation method
    patch_models = []
    tile_models = []
    image_1_models = []
    
    for model in models:
        try:
            info = calculator.get_model_info(model)
            method = info["calculation_method"]
            
            if method == "patch_32":
                patch_models.append(model)
            elif method == "tile_512":
                tile_models.append(model)
            elif method == "image_1":
                image_1_models.append(model)
        except:
            continue
    
    if patch_models:
        print("\n32px Patch Models (GPT-4.1/o4-mini family):")
        for model in sorted(patch_models):
            print(f"  • {model}")
    
    if tile_models:
        print("\n512px Tile Models (GPT-4o/o-series family):")
        for model in sorted(tile_models):
            print(f"  • {model}")
    
    if image_1_models:
        print("\nGPT Image 1:")
        for model in sorted(image_1_models):
            print(f"  • {model}")


def process_single_image(
    image_path: Path, 
    calculator: OpenAIImageTokenCalculator,
    model: str,
    detail: DetailLevel,
    fidelity: FidelityLevel,
    verbose: bool = False
) -> dict:
    """Process a single image and return results"""
    
    try:
        tokens = calculator.calculate_tokens_from_file(
            image_path, model, detail, fidelity
        )
        
        result = {
            "file": str(image_path),
            "tokens": tokens,
            "status": "success"
        }
        
        if verbose:
            from PIL import Image
            with Image.open(image_path) as img:
                result["width"] = img.width
                result["height"] = img.height
                result["format"] = img.format
        
        return result
        
    except Exception as e:
        return {
            "file": str(image_path),
            "tokens": 0,
            "status": "error",
            "error": str(e)
        }


def format_output(results: List[dict], output_format: str, price_per_million: Optional[float] = None) -> str:
    """Format results for output"""
    
    if output_format == "json":
        import json
        return json.dumps(results, indent=2)
    
    elif output_format == "csv":
        import csv
        import io
        
        output = io.StringIO()
        if results:
            fieldnames = results[0].keys()
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        
        return output.getvalue()
    
    else:  # table format
        if not results:
            return "No results to display"
        
        # Convert to format expected by format_results_table
        table_results = {}
        for result in results:
            file_path = result["file"]
            if result["status"] == "success":
                table_results[file_path] = result["tokens"]
            else:
                table_results[file_path] = f"Error: {result.get('error', 'Unknown error')}"
        
        return format_results_table(table_results, include_totals=True)


def main():
    """Main CLI function"""
    parser = create_parser()
    args = parser.parse_args()
    
    # Handle list models
    if args.list_models:
        list_supported_models()
        return 0
    
    # Initialize calculator
    calculator = OpenAIImageTokenCalculator()
    
    # Validate model
    try:
        calculator.get_model_info(args.model)
    except ValueError:
        print(f"Error: Unsupported model '{args.model}'")
        print("Use --list-models to see supported models")
        return 1
    
    # Convert string arguments to enums
    detail = DetailLevel.HIGH if args.detail == "high" else DetailLevel.LOW
    fidelity = FidelityLevel.HIGH if args.fidelity == "high" else FidelityLevel.LOW
    
    results = []
    
    try:
        # Handle dimensions calculation
        if args.dimensions:
            width, height = args.dimensions
            tokens = calculator.calculate_tokens(
                width, height, args.model, detail, fidelity
            )
            
            results.append({
                "file": f"{width}x{height}",
                "tokens": tokens,
                "status": "success",
                "width": width,
                "height": height
            })
        
        # Handle batch same resolution calculation
        elif args.batch_same_resolution:
            count, width, height = args.batch_same_resolution
            
            if args.price_per_million:
                batch_result = calculator.calculate_batch_same_resolution_with_cost(
                    count, width, height, args.model, args.price_per_million, detail, fidelity
                )
            else:
                batch_result = calculator.calculate_batch_same_resolution(
                    count, width, height, args.model, detail, fidelity
                )
            
            # Convert to results format for consistent output
            results.append({
                "file": f"{count} images at {batch_result['resolution']}",
                "tokens": batch_result['total_tokens'],
                "tokens_per_image": batch_result['tokens_per_image'],
                "total_images": batch_result['total_images'],
                "status": "success",
                "batch_calculation": True,
                "model": batch_result['model'],
                "detail": batch_result['detail'],
                "fidelity": batch_result['fidelity']
            })
            
            if args.price_per_million:
                results[-1]["cost_per_image_usd"] = f"${batch_result['cost_per_image_usd']:.6f}"
                results[-1]["total_cost_usd"] = f"${batch_result['total_cost_usd']:.6f}"
        
        # Handle directory processing
        elif args.directory:
            if not args.directory.exists():
                print(f"Error: Directory '{args.directory}' not found")
                return 1
            
            if not args.quiet:
                images = find_images_in_directory(
                    args.directory, args.recursive, args.extensions
                )
                print(f"Found {len(images)} images in {args.directory}")
                if len(images) > 10:
                    print(f"Estimated processing time: {estimate_processing_time(len(images))}")
            
            # Process directory
            directory_results = batch_process_directory(
                args.directory, args.model, detail, fidelity, args.recursive
            )
            
            for file_path, tokens in directory_results.items():
                if isinstance(tokens, int):
                    results.append({
                        "file": file_path,
                        "tokens": tokens,
                        "status": "success"
                    })
                else:
                    results.append({
                        "file": file_path,
                        "tokens": 0,
                        "status": "error",
                        "error": str(tokens)
                    })
        
        # Handle individual images
        elif args.images:
            for image_path in args.images:
                path = Path(image_path)
                if not path.exists():
                    results.append({
                        "file": str(path),
                        "tokens": 0,
                        "status": "error",
                        "error": "File not found"
                    })
                    continue
                
                result = process_single_image(
                    path, calculator, args.model, detail, fidelity, args.verbose
                )
                results.append(result)
        
        # Add cost estimates if price provided
        if args.price_per_million:
            for result in results:
                if result["status"] == "success":
                    cost = calculator.estimate_cost_usd(
                        result["tokens"], args.model, args.price_per_million
                    )
                    result["cost_usd"] = f"${cost:.6f}"
        
        # Format and output results
        output_text = format_output(results, args.format, args.price_per_million)
        
        if args.output:
            args.output.write_text(output_text)
            if not args.quiet:
                print(f"Results saved to {args.output}")
        else:
            print(output_text)
        
        # Summary
        if not args.quiet and args.format == "table":
            success_count = sum(1 for r in results if r["status"] == "success")
            error_count = len(results) - success_count
            total_tokens = sum(r["tokens"] for r in results if r["status"] == "success")
            
            # Check if this is a batch calculation
            batch_results = [r for r in results if r.get("batch_calculation", False)]
            
            if batch_results:
                batch_result = batch_results[0]
                print(f"\nBatch Calculation Summary:")
                print(f"  Images: {batch_result['total_images']:,}")
                print(f"  Resolution: {batch_result['file'].split('at ')[1]}")
                print(f"  Model: {batch_result['model']}")
                print(f"  Detail: {batch_result['detail']}")
                print(f"  Fidelity: {batch_result['fidelity']}")
                print(f"  Tokens per image: {batch_result['tokens_per_image']:,}")
                print(f"  Total tokens: {total_tokens:,}")
                
                if args.price_per_million:
                    print(f"  Cost per image: {batch_result.get('cost_per_image_usd', 'N/A')}")
                    print(f"  Total cost: {batch_result.get('total_cost_usd', 'N/A')}")
            else:
                print(f"\nSummary:")
                print(f"  Processed: {success_count} images")
                print(f"  Errors: {error_count}")
                print(f"  Total tokens: {total_tokens:,}")
                
                if args.price_per_million and total_tokens > 0:
                    total_cost = calculator.estimate_cost_usd(
                        total_tokens, args.model, args.price_per_million
                    )
                    print(f"  Estimated cost: ${total_cost:.6f}")
        
        return 0
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())