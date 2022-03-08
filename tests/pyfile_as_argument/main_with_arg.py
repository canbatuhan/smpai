import os
import subprocess

module_name = 'src.summation'
func_name = 'sum'

def generate_command(module_name, func_name, *args):
    return f"""python -c "from {module_name} import {func_name}; print({func_name}({args}))"""

if __name__=="__main__":
    value = subprocess.run(
        args=generate_command(module_name, func_name),
        capture_output=True,
        shell=True,
        universal_newlines=True
    ).stdout