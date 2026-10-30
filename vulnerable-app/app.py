import subprocess

# Deliberately insecure examples for security testing.
password = "demo-password-123"

def run_command(user_input):
    subprocess.run(user_input, shell=True)
