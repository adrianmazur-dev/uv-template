import subprocess
import sys
import os

def main():
    TEMPLATE_PATHS = ["template/src", "template/tests"]
    DOC_PATHS = ["README.md", "copier.yml"]
    
    print("\n--- Linting template repository ---")
    
    env = os.environ.copy()
    # No need to del VIRTUAL_ENV here as we want to use the project's venv
    
    try:
        # Run codespell
        print(f"\n>> uv run codespell --write-changes {' '.join(TEMPLATE_PATHS)} {' '.join(DOC_PATHS)}")
        subprocess.run(["uv", "run", "codespell", "--write-changes", *TEMPLATE_PATHS, *DOC_PATHS], check=True, env=env)
        
        # Run ruff check
        print(f"\n>> uv run ruff check --fix {' '.join(TEMPLATE_PATHS)}")
        subprocess.run(["uv", "run", "ruff", "check", "--fix", *TEMPLATE_PATHS], check=True, env=env)
        
        # Run ruff format
        print(f"\n>> uv run ruff format {' '.join(TEMPLATE_PATHS)}")
        subprocess.run(["uv", "run", "ruff", "format", *TEMPLATE_PATHS], check=True, env=env)
        
        print("\nPASSED: Linting successful!")
    except subprocess.CalledProcessError as e:
        print(f"\nFAILED: Linting failed with error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nERROR: Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
