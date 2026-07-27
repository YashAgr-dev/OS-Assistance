import subprocess
import os

# ======================================
# Developer Assistant Functions
# ======================================

# Open VS Code
def open_vscode():
    subprocess.Popen("code")

# Open Cursor AI
def open_cursor():
    subprocess.Popen("cursor")

# Open Android Studio
def open_android_studio():
    subprocess.Popen("studio64")

# Open PyCharm
def open_pycharm():
    subprocess.Popen("pycharm64")

# Open IntelliJ IDEA
def open_intellij():
    subprocess.Popen("idea64")

# Open Eclipse
def open_eclipse():
    subprocess.Popen("eclipse")

# Open Git Bash
def open_git_bash():
    subprocess.Popen(r"C:\Program Files\Git\git-bash.exe")

# Open Command Prompt
def open_cmd():
    subprocess.Popen("cmd")

# Open PowerShell
def open_powershell():
    subprocess.Popen("powershell")

# Open Windows Terminal
def open_terminal():
    subprocess.Popen("wt")

# Create Python File
def create_python_file(filename):
    if not filename.endswith(".py"):
        filename += ".py"

    with open(filename, "w") as file:
        file.write("# Python File\n")

    print("Python file created.")

# Create HTML File
def create_html_file(filename):
    if not filename.endswith(".html"):
        filename += ".html"

    with open(filename, "w") as file:
        file.write("<!DOCTYPE html>\n<html>\n</html>")

    print("HTML file created.")

# Create CSS File
def create_css_file(filename):
    if not filename.endswith(".css"):
        filename += ".css"

    with open(filename, "w") as file:
        pass

    print("CSS file created.")

# Create JavaScript File
def create_js_file(filename):
    if not filename.endswith(".js"):
        filename += ".js"

    with open(filename, "w") as file:
        pass

    print("JavaScript file created.")

# Run Python File
def run_python_file(filename):
    subprocess.Popen(["python", filename])

# Run C Program
def run_c_file(filename):
    exe = filename.replace(".c", ".exe")
    subprocess.run(["gcc", filename, "-o", exe])
    subprocess.Popen(exe)

# Run Java Program
def run_java_file(filename):
    subprocess.run(["javac", filename])
    classname = filename.replace(".java", "")
    subprocess.Popen(["java", classname])

# Create Virtual Environment
def create_virtual_environment(name):
    subprocess.Popen(["python", "-m", "venv", name])

# Activate Virtual Environment (prints command)
def activate_virtual_environment(name):
    print(f"{name}\\Scripts\\activate")

# Install Python Package
def install_package(package):
    subprocess.Popen(["pip", "install", package])

# Uninstall Package
def uninstall_package(package):
    subprocess.Popen(["pip", "uninstall", "-y", package])

# Upgrade Package
def upgrade_package(package):
    subprocess.Popen(["pip", "install", "--upgrade", package])

# Freeze Requirements
def freeze_requirements():
    subprocess.Popen("pip freeze > requirements.txt", shell=True)

# Open Current Project
def open_project(path):
    os.startfile(path)

# Open Current Folder in VS Code
def open_folder_vscode(path):
    subprocess.Popen(["code", path])

# Git Init
def git_init():
    subprocess.Popen("git init", shell=True)

# Git Status
def git_status():
    subprocess.Popen("git status", shell=True)

# Git Add
def git_add():
    subprocess.Popen("git add .", shell=True)

# Git Commit
def git_commit(message):
    subprocess.Popen(f'git commit -m "{message}"', shell=True)

# Git Push
def git_push():
    subprocess.Popen("git push", shell=True)

# Git Pull
def git_pull():
    subprocess.Popen("git pull", shell=True)

# Git Clone
def git_clone(repo):
    subprocess.Popen(f"git clone {repo}", shell=True)

# Open localhost
def open_localhost():
    subprocess.Popen("start http://localhost:3000", shell=True)

# Open GitHub
def open_github():
    subprocess.Popen("start https://github.com", shell=True)

# Open Stack Overflow
def open_stackoverflow():
    subprocess.Popen("start https://stackoverflow.com", shell=True)

# Open LeetCode
def open_leetcode():
    subprocess.Popen("start https://leetcode.com", shell=True)


# ==========================================
# Git Automation Functions
# ==========================================

# Git Init
def git_init():
    subprocess.run("git init", shell=True)

# Git Status
def git_status():
    subprocess.run("git status", shell=True)

# Git Add All Files
def git_add():
    subprocess.run("git add .", shell=True)

# Git Add Specific File
def git_add_file(filename):
    subprocess.run(f'git add "{filename}"', shell=True)

# Git Commit
def git_commit(message):
    subprocess.run(f'git commit -m "{message}"', shell=True)

# Git Push
def git_push():
    subprocess.run("git push", shell=True)

# Git Pull
def git_pull():
    subprocess.run("git pull", shell=True)

# Git Clone
def git_clone(repository):
    subprocess.run(f'git clone "{repository}"', shell=True)

# Git Branch
def git_branch():
    subprocess.run("git branch", shell=True)

# Git Checkout Branch
def git_checkout(branch):
    subprocess.run(f'git checkout "{branch}"', shell=True)

# Create New Branch
def git_create_branch(branch):
    subprocess.run(f'git checkout -b "{branch}"', shell=True)

# Delete Branch
def git_delete_branch(branch):
    subprocess.run(f'git branch -d "{branch}"', shell=True)

# Git Merge
def git_merge(branch):
    subprocess.run(f'git merge "{branch}"', shell=True)

# Git Fetch
def git_fetch():
    subprocess.run("git fetch", shell=True)

# Git Log
def git_log():
    subprocess.run("git log --oneline", shell=True)

# Git Diff
def git_diff():
    subprocess.run("git diff", shell=True)

# Git Stash
def git_stash():
    subprocess.run("git stash", shell=True)

# Git Stash Pop
def git_stash_pop():
    subprocess.run("git stash pop", shell=True)

# Git Reset
def git_reset():
    subprocess.run("git reset --hard", shell=True)

# Git Remote
def git_remote():
    subprocess.run("git remote -v", shell=True)

# Add Remote Repository
def git_add_remote(name, url):
    subprocess.run(f'git remote add {name} "{url}"', shell=True)

# Remove Remote
def git_remove_remote(name):
    subprocess.run(f'git remote remove {name}', shell=True)

# Git Tag
def git_tag():
    subprocess.run("git tag", shell=True)

# Create Tag
def git_create_tag(tag):
    subprocess.run(f'git tag "{tag}"', shell=True)

# Push Tags
def git_push_tags():
    subprocess.run("git push --tags", shell=True)

# Git Version
def git_version():
    subprocess.run("git --version", shell=True)


# ======================================
# Developer Assistant Functions
# ======================================

# Open VS Code
def open_vscode():
    subprocess.Popen("code")

# Open Cursor AI
def open_cursor():
    subprocess.Popen("cursor")

# Open Android Studio
def open_android_studio():
    subprocess.Popen("studio64")

# Open PyCharm
def open_pycharm():
    subprocess.Popen("pycharm64")

# Open IntelliJ IDEA
def open_intellij():
    subprocess.Popen("idea64")

# Open Eclipse
def open_eclipse():
    subprocess.Popen("eclipse")

# Open Git Bash
def open_git_bash():
    subprocess.Popen(r"C:\Program Files\Git\git-bash.exe")

# Open Command Prompt
def open_cmd():
    subprocess.Popen("cmd")

# Open PowerShell
def open_powershell():
    subprocess.Popen("powershell")

# Open Windows Terminal
def open_terminal():
    subprocess.Popen("wt")

# Create Python File
def create_python_file(filename):
    if not filename.endswith(".py"):
        filename += ".py"

    with open(filename, "w") as file:
        file.write("# Python File\n")

    print("Python file created.")

# Create HTML File
def create_html_file(filename):
    if not filename.endswith(".html"):
        filename += ".html"

    with open(filename, "w") as file:
        file.write("<!DOCTYPE html>\n<html>\n</html>")

    print("HTML file created.")

# Create CSS File
def create_css_file(filename):
    if not filename.endswith(".css"):
        filename += ".css"

    with open(filename, "w") as file:
        pass

    print("CSS file created.")

# Create JavaScript File
def create_js_file(filename):
    if not filename.endswith(".js"):
        filename += ".js"

    with open(filename, "w") as file:
        pass

    print("JavaScript file created.")

# Run Python File
def run_python_file(filename):
    subprocess.Popen(["python", filename])

# Run C Program
def run_c_file(filename):
    exe = filename.replace(".c", ".exe")
    subprocess.run(["gcc", filename, "-o", exe])
    subprocess.Popen(exe)

# Run Java Program
def run_java_file(filename):
    subprocess.run(["javac", filename])
    classname = filename.replace(".java", "")
    subprocess.Popen(["java", classname])

# Create Virtual Environment
def create_virtual_environment(name):
    subprocess.Popen(["python", "-m", "venv", name])

# Activate Virtual Environment (prints command)
def activate_virtual_environment(name):
    print(f"{name}\\Scripts\\activate")

# Install Python Package
def install_package(package):
    subprocess.Popen(["pip", "install", package])

# Uninstall Package
def uninstall_package(package):
    subprocess.Popen(["pip", "uninstall", "-y", package])

# Upgrade Package
def upgrade_package(package):
    subprocess.Popen(["pip", "install", "--upgrade", package])

# Freeze Requirements
def freeze_requirements():
    subprocess.Popen("pip freeze > requirements.txt", shell=True)

# Open Current Project
def open_project(path):
    os.startfile(path)

# Open Current Folder in VS Code
def open_folder_vscode(path):
    subprocess.Popen(["code", path])

# Git Init
def git_init():
    subprocess.Popen("git init", shell=True)

# Git Status
def git_status():
    subprocess.Popen("git status", shell=True)

# Git Add
def git_add():
    subprocess.Popen("git add .", shell=True)

# Git Commit
def git_commit(message):
    subprocess.Popen(f'git commit -m "{message}"', shell=True)

# Git Push
def git_push():
    subprocess.Popen("git push", shell=True)

# Git Pull
def git_pull():
    subprocess.Popen("git pull", shell=True)

# Git Clone
def git_clone(repo):
    subprocess.Popen(f"git clone {repo}", shell=True)

# Open localhost
def open_localhost():
    subprocess.Popen("start http://localhost:3000", shell=True)

# Open GitHub
def open_github():
    subprocess.Popen("start https://github.com", shell=True)

# Open Stack Overflow
def open_stackoverflow():
    subprocess.Popen("start https://stackoverflow.com", shell=True)

# Open LeetCode
def open_leetcode():
    subprocess.Popen("start https://leetcode.com", shell=True)    

