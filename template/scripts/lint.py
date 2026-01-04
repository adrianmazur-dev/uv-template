import subprocess
import sys
import os

def main():
    SRC_PATHS = ["src", "tests"]
    DOC_PATHS = ["README.md"]
    
    print("\n--- Linting project ---")
    
    # Ensure we don't use the parent's virtualenv if running inside copier
    env = os.environ.copy()
    if "VIRTUAL_ENV" in env:
        del env["VIRTUAL_ENV"]
    if "PYTHONPATH" in env:
        del env["PYTHONPATH"]
    
    try:
        # Ensure dependencies are installed (crucial for basedpyright)
        print("\n>> uv sync --all-extras")
        subprocess.run(["uv", "sync", "--all-extras"], check=True, env=env)

        # Run codespell
        print(f"\n>> uv run codespell --write-changes {' '.join(SRC_PATHS)} {' '.join(DOC_PATHS)}")
        subprocess.run(["uv", "run", "codespell", "--write-changes", *SRC_PATHS, *DOC_PATHS], check=True, env=env)
        
        # Run ruff check
        print(f"\n>> uv run ruff check --fix {' '.join(SRC_PATHS)}")
        subprocess.run(["uv", "run", "ruff", "check", "--fix", *SRC_PATHS], check=True, env=env)
        
        # Run ruff format
        print(f"\n>> uv run ruff format {' '.join(SRC_PATHS)}")
        subprocess.run(["uv", "run", "ruff", "format", *SRC_PATHS], check=True, env=env)
        
        # Run basedpyright
        print(f"\n>> uv run basedpyright --stats {' '.join(SRC_PATHS)}")
        subprocess.run(["uv", "run", "basedpyright", "--stats", *SRC_PATHS], check=True, env=env)
        
        print("\nPASSED: Linting successful!")
    except subprocess.CalledProcessError as e:
        print(f"\nFAILED: Linting failed with error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nERROR: Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
