"""
Utility helpers for formatting, colored printing, emoji logs.
"""

def log_info(msg: str):
    print(f"ℹ️ INFO: {msg}")

def log_error(msg: str):
    print(f"❌ ERROR: {msg}")

def log_success(msg: str):
    print(f"✅ SUCCESS: {msg}")