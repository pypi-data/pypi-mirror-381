import os
import shutil
import subprocess
import sys
import platform

def run_in_wsl(cmd, project_dir):
    wsl_project_dir = "/mnt/" + project_dir[0].lower() + project_dir[2:].replace("\\", "/")
    full_cmd = f"cd '{wsl_project_dir}' && {cmd}"
    return subprocess.check_call(["wsl", "bash", "-c", full_cmd])

def ensure_wsl_setup(project_dir):
    print("Check WSL setup")
    try:
        run_in_wsl("python3 --version", project_dir)
    except subprocess.CalledProcessError:
        print("Installing Python and building tools")
        run_in_wsl("sudo apt update && sudo apt install -y python3 python3-pip python3-venv build-essential cmake", project_dir)

    if not os.path.exists(os.path.join(project_dir, "venv")):
        print("Creating virtualenv...")
        run_in_wsl("python3 -m venv venv", project_dir)

    #install flet
    print("Installing Flet")
    run_in_wsl("source venv/bin/activate && pip install --upgrade pip flet", project_dir)


def build():
    """
    Build cellsepi with flet build platform -v
    """
    #goto cellsepi folder
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    #check which system is used
    system = platform.system().lower()
    if system == "windows":
        ensure_wsl_setup(project_dir)
        try:
            run_in_wsl("source venv/bin/activate && python3 -m flet.cli build linux -v", project_dir)
            print("Flet Build success")
        except subprocess.CalledProcessError as e:
            print(f"Flet build failed in WSL: {e}")
            sys.exit(1)
        return
    elif system == "darwin":
        target = "macos"
    elif system == "linux":
        target = "linux"
    else:
        print("Flet build failed: unknown system")
        sys.exit(1)

    #try to build cellsepi
    try:
        subprocess.check_call([sys.executable, "-m", "flet.cli", "build", target, "-v"])
    except subprocess.CalledProcessError as e:
        print(f"Flet build failed: {e}")
        sys.exit(1)
