import subprocess
import sys
from datetime import datetime

def run_step(name, command):
    print(f"\n=== Running: {name} ===")
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"ERROR in step '{name}'")
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    print("Starting Weekly Optical Digest Pipeline")
    print("Time:", datetime.now())

    run_step(
        "Collect articles",
        "python run_collect.py"
    )

    run_step(
        "Compute relevance",
        "python run_relevance.py"
    )

    run_step(
        "Summarize articles",
        "python run_summarize.py"
    )

    run_step(
        "Build weekly digest",
        "python run_digest.py"
    )

    print("\nPipeline completed successfully")
