import subprocess

def run_command(user_input):
    subprocess.run(
        ["echo", user_input],
        shell=False,
        check=True
    )
