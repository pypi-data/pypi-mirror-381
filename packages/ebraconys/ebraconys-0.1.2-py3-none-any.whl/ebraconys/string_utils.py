"""
String utility functions.
"""

import re
import unicodedata

def slugify(text: str, separator: str = "-") -> str:
    """
    Convert text to a URL-friendly slug.
    
    Args:
        text: Input text to convert
        separator: Word separator (default: "-")
        
    Returns:
        URL-friendly slug string
        
    Example:
        >>> slugify("Hello World!")
        'hello-world'
    """
    # Normalize unicode characters
    text = unicodedata.normalize('NFKD', text)
    
    # Convert to lowercase and remove special characters
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text.lower())
    
    # Replace spaces and hyphens with separator
    text = re.sub(r'[-\s]+', separator, text).strip('-_')
    
    return text

def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text: Input string to reverse
        
    Returns:
        Reversed string
        
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]
