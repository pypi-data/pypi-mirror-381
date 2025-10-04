#!/usr/bin/env python3
"""
Setup script for OpenAI Image Token Counter
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

# Read requirements
requirements_path = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_path.exists():
    requirements = requirements_path.read_text().strip().split('\n')

setup(
    name="openai-image-token-counter",
    version="1.0.0",
    author="Eduardo J. Barrios",
    author_email="contact@edujbarrios.com",
    description="Calculate token costs for images in OpenAI Vision API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edujbarrios/openai-image-token-counter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "openai-image-tokens=openai_image_token_counter.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "openai_image_token_counter": ["../token_config.mdx"],
    },
    zip_safe=False,
    keywords="openai, vision, api, tokens, image, calculator, cost, estimation",
    project_urls={
        "Bug Reports": "https://github.com/edujbarrios/openai-image-token-counter/issues",
        "Source": "https://github.com/edujbarrios/openai-image-token-counter",
        "Documentation": "https://github.com/edujbarrios/openai-image-token-counter#readme",
    },
)