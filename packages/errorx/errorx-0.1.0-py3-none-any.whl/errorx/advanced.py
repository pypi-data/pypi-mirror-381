"""
Advanced error explanation with contextual suggestions.
Analyzes traceback strings and provides detailed fixes.
"""

import traceback
from .core import ERROR_GUIDE

def advanced_explain(error: Exception, tb=None):
    """Advanced explanation of Python errors with optional traceback analysis."""
    err_type = type(error).__name__
    message = str(error)
    print(f"⚡ Advanced Analysis: {err_type} - {message}\n")

    if err_type in ERROR_GUIDE:
        guide = ERROR_GUIDE[err_type]
        print(f"🔍 Why?\n{guide['why']}\n")
        print(f"🛠️ How to Fix?\n{guide['fix']}\n")
        print(f"✅ Example Fix:\n{guide['example']}\n")
    else:
        print("ℹ️ Error type is uncommon. Suggest reviewing the traceback below or contacting Admin @Kakkarotofficial.\n")

    if tb:
        print("📄 Traceback (most recent call last):")
        traceback.print_tb(tb)