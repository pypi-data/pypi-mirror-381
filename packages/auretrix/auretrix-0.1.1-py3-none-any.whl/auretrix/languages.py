"""
Language support and language codes
"""

# Indian languages with their codes
INDIAN_LANGUAGES = {
    'hi': {'name': 'Hindi', 'native': 'हिन्दी', 'code': 'hi-IN'},
    'bn': {'name': 'Bengali', 'native': 'বাংলা', 'code': 'bn-IN'},
    'te': {'name': 'Telugu', 'native': 'తెలుగు', 'code': 'te-IN'},
    'mr': {'name': 'Marathi', 'native': 'मराठी', 'code': 'mr-IN'},
    'ta': {'name': 'Tamil', 'native': 'தமிழ்', 'code': 'ta-IN'},
    'gu': {'name': 'Gujarati', 'native': 'ગુજરાતી', 'code': 'gu-IN'},
    'kn': {'name': 'Kannada', 'native': 'ಕನ್ನಡ', 'code': 'kn-IN'},
    'ml': {'name': 'Malayalam', 'native': 'മലയാളം', 'code': 'ml-IN'},
    'pa': {'name': 'Punjabi', 'native': 'ਪੰਜਾਬੀ', 'code': 'pa-IN'},
    'or': {'name': 'Odia', 'native': 'ଓଡ଼ିଆ', 'code': 'or-IN'},
    'ur': {'name': 'Urdu', 'native': 'اردو', 'code': 'ur-IN'},
    'as': {'name': 'Assamese', 'native': 'অসমীয়া', 'code': 'as-IN'},
}

# Popular global languages
GLOBAL_LANGUAGES = {
    'en': {'name': 'English', 'code': 'en-US'},
    'es': {'name': 'Spanish', 'code': 'es-ES'},
    'fr': {'name': 'French', 'code': 'fr-FR'},
    'de': {'name': 'German', 'code': 'de-DE'},
    'zh': {'name': 'Chinese', 'code': 'zh-CN'},
    'ja': {'name': 'Japanese', 'code': 'ja-JP'},
    'ko': {'name': 'Korean', 'code': 'ko-KR'},
    'ar': {'name': 'Arabic', 'code': 'ar-SA'},
    'ru': {'name': 'Russian', 'code': 'ru-RU'},
    'pt': {'name': 'Portuguese', 'code': 'pt-BR'},
    'it': {'name': 'Italian', 'code': 'it-IT'},
    'nl': {'name': 'Dutch', 'code': 'nl-NL'},
    'pl': {'name': 'Polish', 'code': 'pl-PL'},
    'tr': {'name': 'Turkish', 'code': 'tr-TR'},
    'vi': {'name': 'Vietnamese', 'code': 'vi-VN'},
    'th': {'name': 'Thai', 'code': 'th-TH'},
    'id': {'name': 'Indonesian', 'code': 'id-ID'},
}

# Combine all languages
SUPPORTED_LANGUAGES = {**INDIAN_LANGUAGES, **GLOBAL_LANGUAGES}


def get_language_code(language_id: str) -> str:
    """
    Get full language code from short ID
    
    Args:
        language_id: Short language ID (e.g., 'hi', 'en')
    
    Returns:
        Full language code (e.g., 'hi-IN', 'en-US')
    
    Example:
        >>> get_language_code('hi')
        'hi-IN'
    """
    if language_id in SUPPORTED_LANGUAGES:
        return SUPPORTED_LANGUAGES[language_id]['code']
    
    # If already a full code, return as is
    if '-' in language_id:
        return language_id
    
    raise ValueError(f"Unsupported language: {language_id}")


def get_language_name(language_id: str, native: bool = False) -> str:
    """
    Get language name
    
    Args:
        language_id: Language ID or code
        native: Return native name if True
    
    Returns:
        Language name
    
    Example:
        >>> get_language_name('hi', native=True)
        'हिन्दी'
    """
    lang_id = language_id.split('-')[0]
    
    if lang_id not in SUPPORTED_LANGUAGES:
        return language_id
    
    lang_info = SUPPORTED_LANGUAGES[lang_id]
    
    if native and 'native' in lang_info:
        return lang_info['native']
    
    return lang_info['name']


def list_indian_languages():
    """List all supported Indian languages"""
    return [
        {
            'id': lang_id,
            'name': info['name'],
            'native': info['native'],
            'code': info['code']
        }
        for lang_id, info in INDIAN_LANGUAGES.items()
    ]


def list_all_languages():
    """List all supported languages"""
    return [
        {
            'id': lang_id,
            'name': info['name'],
            'code': info['code']
        }
        for lang_id, info in SUPPORTED_LANGUAGES.items()
    ]


def is_indian_language(language_id: str) -> bool:
    """Check if language is an Indian language"""
    lang_id = language_id.split('-')[0]
    return lang_id in INDIAN_LANGUAGES


# Common language groups
LANGUAGE_GROUPS = {
    'indian': list(INDIAN_LANGUAGES.keys()),
    'european': ['en', 'es', 'fr', 'de', 'it', 'nl', 'pl', 'ru'],
    'asian': ['zh', 'ja', 'ko', 'th', 'vi', 'id'],
    'middle_east': ['ar', 'ur', 'tr']
}


def get_languages_by_group(group: str) -> list:
    """Get languages by group"""
    return LANGUAGE_GROUPS.get(group, [])