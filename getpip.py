import os
import subprocess
import urllib.request

# Define the URL for get-pip.py
url = "https://bootstrap.pypa.io/get-pip.py"
script_name = "get-pip.py"

# Download the get-pip.py script
urllib.request.urlretrieve(url, script_name)

# Change permissions to make the script executable
os.chmod(script_name, 0o755)  # Adds execute permissions

# Run the get-pip.py script
subprocess.run(['python3', os.path.abspath(script_name)])

# Cleanup: remove the get-pip.py script after installation
os.remove(script_name)

print("pip installation complete.")
