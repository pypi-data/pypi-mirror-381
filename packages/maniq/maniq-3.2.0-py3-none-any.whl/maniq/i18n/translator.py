#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translator class for Maniq
"""

from .translations import TRANSLATIONS


class Translator:
    """Handle translation of messages"""
    
    def __init__(self, language: str = 'en'):
        self.language = language
        self.translations = TRANSLATIONS.get(language, TRANSLATIONS['en'])
    
    def get(self, key: str, **kwargs) -> str:
        """Get translated string with formatting"""
        template = self.translations.get(key, key)
        try:
            return template.format(**kwargs)
        except KeyError:
            return template
            