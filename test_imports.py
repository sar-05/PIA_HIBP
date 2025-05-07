# test_imports.py
try:
    import pia_hibp
    print(f"Package imported successfully. Location: {pia_hibp.__file__}")
    
    from pia_hibp.config import RAW_DIR
    print(f"Config imported successfully. RAW_DIR = {RAW_DIR}")
except ImportError as e:
    print(f"Import failed: {e}")
