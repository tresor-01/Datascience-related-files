# setup_env.py
import os
import subprocess
import sys

# Step 1: Create virtual environment
env_dir = ".env"
print(f"Creating virtual environment at {env_dir}...")
subprocess.run([sys.executable, "-m", "venv", env_dir])

# Step 2: Activate environment and install packages
# Define most used packages
packages = [
    "numpy", "pandas", "requests", "matplotlib", "scikit-learn",
    "flask", "django", "beautifulsoup4", "seaborn", "jupyter"
]

# Use the env pip to install packages
pip_path = os.path.join(env_dir, "Scripts", "pip") if os.name == 'nt' else os.path.join(env_dir, "bin", "pip")

print(f"Installing packages: {' '.join(packages)}...")
subprocess.run([pip_path, "install"] + packages)

print("✅ Virtual environment is ready with common libraries installed.")
