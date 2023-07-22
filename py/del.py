import subprocess

# Replace "app_name" with the name of the app you want to uninstall
app_name = "C:\Program Files (x86)\Honeygain\Honeygain.exe"

# Execute the command to uninstall the app using winget
subprocess.run(["winget", "uninstall", app_name], check=True)