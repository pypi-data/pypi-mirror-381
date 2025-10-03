"""
Speech recognition providers
"""

from auretrix.providers.base import BaseProvider
from auretrix.providers.whisper import WhisperProvider
from auretrix.providers.google import GoogleProvider
from auretrix.providers.assemblyai import AssemblyAIProvider
from auretrix.providers.azure import AzureProvider

__all__ = [
    'BaseProvider',
    'WhisperProvider',
    'GoogleProvider',
    'AssemblyAIProvider',
    'AzureProvider'
]