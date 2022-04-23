import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done")
print(f"Installing packages...{RESET_ALL}")

subprocess.call(['conda', 'env', 'create','--file','environment.yml'])

print(f"{MESSAGE_COLOR}Done!")