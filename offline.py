import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def select_and_run_script():
    # Hide the main tkinter window
    root = tk.Tk()
    root.withdraw()
    
    # Ask user to select a Python script
    file_path = filedialog.askopenfilename(
        title="Select a Python script to run",
        filetypes=[("Python files", "*.py"), ("All files", "*.*")]
    )
    
    if not file_path:
        print("No file selected. Exiting.")
        return
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return
    
    # Create the command to run the script in a new command prompt window
    if os.name == 'nt':  # For Windows
        command = f'cmd /k "python "{file_path}" & pause"'
    else:  # For macOS/Linux
        command = f'x-terminal-emulator -e python3 "{file_path}"'
    
    # Execute the command
    try:
        subprocess.Popen(command, shell=True)
    except Exception as e:
        print(f"Error running script: {e}")
    
    # Exit the current script
    exit()

if __name__ == "__main__":
    select_and_run_script()