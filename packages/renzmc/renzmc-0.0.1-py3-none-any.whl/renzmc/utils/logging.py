"""
Logging module for RenzMC
Provides centralized logging configuration
"""

import logging
import sys
from pathlib import Path
from typing import Optional

def setup_logging(
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    format_string: Optional[str] = None
) -> logging.Logger:
    """
    Setup logging configuration for RenzMC
    
    Args:
        level: Logging level (default: INFO)
        log_file: Optional log file path
        format_string: Optional custom format string
    
    Returns:
        Configured logger instance
    """
    
    # Default format
    if format_string is None:
        format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Create formatter
    formatter = logging.Formatter(
        format_string,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Setup handlers
    handlers = []
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    handlers.append(console_handler)
    
    # File handler (optional)
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        handlers.append(file_handler)
    
    # Configure root logger
    logging.basicConfig(
        level=level,
        handlers=handlers,
        force=True
    )
    
    # Create and return RenzMC logger
    logger = logging.getLogger('renzmc')
    logger.setLevel(level)
    
    return logger

# Create default logger
logger = setup_logging()

# Convenience functions
def debug(msg: str, *args, **kwargs):
    """Log debug message"""
    logger.debug(msg, *args, **kwargs)

def info(msg: str, *args, **kwargs):
    """Log info message"""
    logger.info(msg, *args, **kwargs)

def warning(msg: str, *args, **kwargs):
    """Log warning message"""
    logger.warning(msg, *args, **kwargs)

def error(msg: str, *args, **kwargs):
    """Log error message"""
    logger.error(msg, *args, **kwargs)

def critical(msg: str, *args, **kwargs):
    """Log critical message"""
    logger.critical(msg, *args, **kwargs)