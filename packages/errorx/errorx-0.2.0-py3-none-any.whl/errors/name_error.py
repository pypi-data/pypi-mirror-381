# errors/name_error.py
def handle(exc, advanced=False, frames=None):
    print(f"❌ {exc}")
    print("ℹ️ Cause: A variable or name is used before assignment or is undefined.")
    print("🛠️ Fix: Ensure the variable is defined before use. Check for typos or missing imports.")
    if advanced:
        print("⚡ Advanced Recommendations:")
        if frames:
            for f in frames[-3:]:
                print(f"- Occurred in {f['filename']}:{f['lineno']} (function {f['name']})")
        print("✅ Example:")
        print("outname = 'value'")
        print("print(outname)")