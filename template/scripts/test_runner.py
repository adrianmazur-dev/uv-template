import subprocess
import sys

def main():
    """Run pytest."""
    try:
        result = subprocess.run(["pytest"], check=False)
        sys.exit(result.returncode)
    except Exception as e:
        print(f"Error running pytest: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
