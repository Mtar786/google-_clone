import os
import subprocess
import sys

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error executing command: {command}")
        print(f"Error: {error.decode()}")
        sys.exit(1)
    return output.decode()

def main():
    # Create Django project
    run_command("django-admin startproject backend .")

    # Create apps
    run_command("python manage.py startapp accounts")
    run_command("python manage.py startapp posts")
    run_command("python manage.py startapp circles")
    run_command("python manage.py startapp notifications")

    print("Django project structure created successfully!")

if __name__ == "__main__":
    main()