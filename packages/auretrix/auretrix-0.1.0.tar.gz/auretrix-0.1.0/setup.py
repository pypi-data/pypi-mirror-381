"""
Auretrix - Unified Speech Recognition Library
Setup configuration for PyPI
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
if readme_file.exists():
    long_description = readme_file.read_text(encoding='utf-8')
else:
    long_description = "Unified speech recognition library with multi-provider support"

setup(
    name="auretrix",
    version="0.1.0",
    author="Auretrix AI",
    author_email="contact@auretrix.com",
    description="Unified speech recognition library with multi-provider support and Indian language focus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/auretrix/auretrix",
    project_urls={
        "Bug Tracker": "https://github.com/auretrix/auretrix/issues",
        "Documentation": "https://docs.auretrix.com",
        "Source Code": "https://github.com/auretrix/auretrix",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "pydub>=0.25.1",
        "numpy>=1.21.0",
    ],
    extras_require={
        "whisper": ["openai-whisper>=20230314"],
        "google": ["google-cloud-speech>=2.20.0"],
        "assemblyai": ["assemblyai>=0.17.0"],
        "azure": ["azure-cognitiveservices-speech>=1.31.0"],
        "all": [
            "openai-whisper>=20230314",
            "google-cloud-speech>=2.20.0",
            "assemblyai>=0.17.0",
            "azure-cognitiveservices-speech>=1.31.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
        ],
    },
    keywords="speech recognition whisper google assemblyai azure indian languages hindi transcription",
    entry_points={
        "console_scripts": [
            "auretrix=auretrix.cli:main",
        ],
    },
)