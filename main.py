import os
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog
from urllib.parse import urlparse

# Shared variables for online functionality
installed_reqs = []
missing_reqs = []

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

def safe_git_checkout(repo_url):
    repo_name = os.path.splitext(os.path.basename(urlparse(repo_url).path))[0]
    if os.path.exists(repo_name):
        print(f"\n[!] Folder '{repo_name}' already exists. Cleaning it...")
        try:
            subprocess.run(["git", "clean", "-xdf"], cwd=repo_name, check=True)
            subprocess.run(["git", "reset", "--hard"], cwd=repo_name, check=True)
            subprocess.run(["git", "pull"], cwd=repo_name, check=True)
        except subprocess.CalledProcessError:
            print("[X] Failed to clean/reset the existing repo.")
            input("Press Enter to exit.")
            sys.exit(1)
    else:
        print("[+] Cloning repository...")
        try:
            subprocess.run(["git", "clone", repo_url], check=True)
        except subprocess.CalledProcessError:
            print("[X] Git clone failed. Make sure Git is installed and the link is correct.")
            input("Press Enter to exit.")
            sys.exit(1)
    return repo_name

def check_and_store_requirements(requirements_path):
    global installed_reqs, missing_reqs
    try:
        import pkg_resources
    except ImportError:
        print("[X] Missing setuptools. Run: pip install setuptools")
        input("Press Enter to exit.")
        sys.exit(1)

    with open(requirements_path, "r") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    installed_packages = {pkg.key for pkg in pkg_resources.working_set}

    for req in requirements:
        pkg_name = req.split("==")[0].lower()
        if pkg_name in installed_packages:
            installed_reqs.append(req)
        else:
            missing_reqs.append(req)

def install_missing_requirements():
    global missing_reqs
    if not missing_reqs:
        print("\n[✓] All requirements already installed.")
        return
    for req in missing_reqs[:]:
        print(f"[!] {req} is missing.")
        confirm = input(f"Install '{req}'? (y/n): ").strip().lower()
        if confirm == "y":
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", req])
                installed_reqs.append(req)
                missing_reqs.remove(req)
            except subprocess.CalledProcessError:
                print(f"[X] Failed to install: {req}")
        else:
            print(f"[-] Skipped: {req}")

def list_files(repo_dir):
    files = [f for f in os.listdir(repo_dir) if os.path.isfile(os.path.join(repo_dir, f))]
    files.append("🔧 View Requirements to Install")
    files.append("✅ View Already Installed Requirements")
    return files

def display_menu(files):
    print("\n📁 Repository Contents:")
    for i, f in enumerate(files, start=1):
        print(f"{i}. {f}")
    return files

def handle_file_selection(repo_dir, files):
    try:
        choice = int(input("\nEnter file number to open/run: ").strip())
        if choice < 1 or choice > len(files):
            print("[X] Invalid selection.")
            return False  # loop again
        selected = files[choice - 1]
        path = os.path.join(repo_dir, selected)

        if selected.lower().endswith((".txt", ".md")):
            print(f"\n--- {selected} ---")
            with open(path, "r", encoding="utf-8") as f:
                print(f.read())

        elif selected == "main.py":
            print("\n[▶] Launching 'main.py' in new terminal...\n")
            subprocess.Popen(
                ['start', 'cmd', '/k', 'python main.py'],
                cwd=repo_dir,
                shell=True
            )
            sys.exit(0)

        elif selected.startswith("🔧"):
            print("\n[🔧 Requirements To Install]")
            if not missing_reqs:
                print("✔ All requirements are already installed.")
            else:
                for req in missing_reqs:
                    print(f"• {req}")
            install = input("Do you want to install missing requirements? (y/n): ").strip().lower()
            if install == 'y':
                install_missing_requirements()

        elif selected.startswith("✅"):
            print("\n[✅ Already Installed Requirements]")
            if not installed_reqs:
                print("None installed yet.")
            else:
                for req in installed_reqs:
                    print(f"• {req}")

        else:
            print("[!] This file can't be opened or run directly.")

    except (ValueError, IndexError):
        print("[X] Invalid input.")
    return True  # loop again

def online_mode():
    print("🔗 GitHub Repo Runner Tool")
    repo_url = input("Enter GitHub repository URL: ").strip()

    if not repo_url:
        print("No URL provided.")
        return

    repo_name = safe_git_checkout(repo_url)

    req_file = os.path.join(repo_name, "requirements.txt")
    if os.path.exists(req_file):
        check_and_store_requirements(req_file)
    else:
        print("[-] No requirements.txt found.")

    while True:
        files = list_files(repo_name)
        display_menu(files)
        should_continue = handle_file_selection(repo_name, files)
        if not should_continue:
            break

def main_menu():
    print("📂 Python Script Runner")
    print("1. Run a local Python script (offline) - DEFAULT")
    print("2. Clone and run from GitHub repository (online)")
    print("3. Exit")
    
    choice = input("Select an option (1-3, or press Enter for offline mode): ").strip()
    
    if choice == "" or choice == "1":
        select_and_run_script()
    elif choice == "2":
        online_mode()
    elif choice == "3":
        sys.exit(0)
    else:
        print("Invalid choice. Defaulting to offline mode...")
        select_and_run_script()

if __name__ == "__main__":
    main_menu()