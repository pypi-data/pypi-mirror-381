"""
Math utility functions.
"""

def percentage(part: float, whole: float) -> float:
    """
    Calculate percentage.
    
    Args:
        part: The part value
        whole: The whole value
        
    Returns:
        Percentage value
        
    Example:
        >>> percentage(25, 100)
        25.0
    """
    if whole == 0:
        return 0.0
    return (part / whole) * 100



def clamp(value: float, min_val: float, max_val: float) -> float:
    """
    Clamp a value between minimum and maximum bounds.
    
    Args:
        value: Value to clamp
        min_val: Minimum allowed value
        max_val: Maximum allowed value
        
    Returns:
        Clamped value
        
    Example:
        >>> clamp(15, 0, 10)
        10
    """
    return max(min_val, min(value, max_val))
