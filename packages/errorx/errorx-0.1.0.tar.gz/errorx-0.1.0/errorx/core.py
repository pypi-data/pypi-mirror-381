"""
Core basic error explanation with simple fixes.
"""

ERROR_GUIDE = {
    "ZeroDivisionError": {
        "why": "You attempted to divide a number by zero. Division by zero is mathematically undefined.",
        "fix": "Check if the denominator is zero before dividing to avoid runtime errors.",
        "example": "if b != 0:\n    result = a / b\nelse:\n    print('Cannot divide by zero')"
    },
    "ValueError": {
        "why": "An invalid value was passed to a function or type conversion failed.",
        "fix": "Validate inputs before converting or passing them.",
        "example": "int('123')  # Works fine"
    },
    "TypeError": {
        "why": "An operation was applied to incompatible types, e.g., adding str and int.",
        "fix": "Ensure operands are compatible before performing operations.",
        "example": "'abc' + str(5)  # Works fine"
    },
    "KeyError": {
        "why": "Accessed a dictionary key that does not exist.",
        "fix": "Check key existence or use dict.get('key', default) method.",
        "example": "mydict.get('key', 'default')"
    },
    "IndexError": {
        "why": "Attempted to access a list index that is out of range.",
        "fix": "Check list length before accessing an index.",
        "example": "if i < len(mylist): print(mylist[i])"
    },
}

def explain_error(error: Exception):
    """Explain the error with why it happened and how to fix it."""
    err_type = type(error).__name__
    message = str(error)

    if err_type in ERROR_GUIDE:
        guide = ERROR_GUIDE[err_type]
        print(f"❌ {err_type}: {message}\n")
        print(f"🔎 Why?\n{guide['why']}\n")
        print(f"🛠️ How to Fix?\n{guide['fix']}\n")
        print(f"✅ Example Fix:\n{guide['example']}\n")
    else:
        print(f"❌ {err_type}: {message}")
        print("ℹ️ No guide available yet. Please check official Python docs or contact Admin @Kakkarotofficial.")