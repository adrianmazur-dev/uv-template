import subprocess
import sys

def main():
    """Upgrade project dependencies."""
    print("\n--- Upgrading dependencies ---")
    try:
        subprocess.run(["uv", "lock", "--upgrade"], check=True)
        subprocess.run(["uv", "sync", "--all-extras"], check=True)
        print("\nPASSED: Upgrade successful!")
    except subprocess.CalledProcessError as e:
        print(f"\nFAILED: Upgrade failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
