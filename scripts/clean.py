import shutil
import os
from pathlib import Path

def main():
    """Remove build artifacts and caches."""
    to_remove = [
        ".venv",
        ".ruff_cache",
        ".pytest_cache",
        ".mypy_cache",
        "build",
        "dist",
        "*.egg-info",
        "__pycache__",
        ".pyc",
    ]
    
    print("\n--- Cleaning project ---")
    
    count = 0
    for pattern in to_remove:
        if pattern.startswith("*"):
            # Handle extensions
            ext = pattern[1:]
            for p in Path(".").rglob(f"*{ext}"):
                if p.is_file():
                    p.unlink()
                elif p.is_dir():
                    shutil.rmtree(p)
                count += 1
        elif pattern == "__pycache__":
            for p in Path(".").rglob("__pycache__"):
                shutil.rmtree(p)
                count += 1
        else:
            p = Path(pattern)
            if p.exists():
                if p.is_file():
                    p.unlink()
                else:
                    shutil.rmtree(p)
                count += 1
                
    print(f"Cleaned {count} items.")

if __name__ == "__main__":
    main()
