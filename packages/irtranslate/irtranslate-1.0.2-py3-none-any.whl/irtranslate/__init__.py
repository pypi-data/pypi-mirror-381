from .translator import Translator
from .exceptions import TranslationError, NetworkError, EmptyTextError

__version__ = "1.0.2"
__all__ = ["Translator", "TranslationError", "NetworkError", "EmptyTextError"]
