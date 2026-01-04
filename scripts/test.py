import subprocess
import sys
import tempfile
import shutil
import os

def main():
    print("\n--- Testing uv-template generation ---")
    
    test_dir = tempfile.mkdtemp()
    print(f"Generating test project in {test_dir}")
    
    try:
        cmd = [
            "uv", "run", "copier", "copy", "--defaults",
            "--data", "project_name=test-project",
            "--data", "project_description=Test project",
            "--data", "project_author_name=Test Author",
            "--data", "project_author_email=test@example.com",
            "--data", "include_fastapi=true",
            "--data", "include_arq=true",
            ".", os.path.join(test_dir, "test-project"),
            "--trust"
        ]
        
        print(f"\n>> {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        
        print("\nPASSED: Template generation succeeded!")
    except subprocess.CalledProcessError as e:
        print(f"\nFAILED: Template generation failed: {e}")
        sys.exit(1)
    finally:
        print(f"Cleaning up {test_dir}")
        shutil.rmtree(test_dir, ignore_errors=True)

if __name__ == "__main__":
    main()
