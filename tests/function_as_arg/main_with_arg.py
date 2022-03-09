import os
import subprocess

module_name = 'src.summation'
func_name = 'sum'

def generate_command(module_name, func_name, *args):
    return f"""python -c "from {module_name} import {func_name}; print({func_name}({args}))"""

def run_command(command):
    return subprocess.run(
        args=command,
        capture_output=True,
        shell=True,
        universal_newlines=True
    ).stdout

if __name__=="__main__":
    result = run_command(generate_command(module_name, func_name))