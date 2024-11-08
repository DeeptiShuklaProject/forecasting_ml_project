import os
import subprocess

# Define the paths for the individual scripts
scripts = [
    "data_preprocessing.py",
    "exploratory_data_analysis.py",
    "forecasting_model.py",
    "machine_learning_model.py"
]

def run_script(script_name):
    """Executes a script and handles any errors."""
    try:
        print(f"\nRunning {script_name}...")
        subprocess.run(["python", script_name], check=True)
        print(f"{script_name} completed successfully.")
    except subprocess.CalledProcessError:
        print(f"Error occurred while running {script_name}.")

def main():
    print("Starting the project execution...")

    # Change to the src directory to run scripts
    os.chdir("src")

    # Run each script in sequence
    for script in scripts:
        run_script(script)

    print("\nAll tasks completed successfully. Check the 'data/' and 'reports/' folders for outputs.")

if __name__ == "__main__":
    main()
