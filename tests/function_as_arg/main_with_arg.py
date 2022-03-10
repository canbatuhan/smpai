import os
import subprocess

module_name = 'src.summation'
func_name = 'sum'

def generate_command(module_name, func_name, params, *args):
    keyword_args = ""
    for index, param in enumerate(params):
        keyword_args += "{}={},".format(param, args[index])
    return f"""python -c "from {module_name} import {func_name}; print({func_name}({keyword_args}))"""

def run_command(command):
    return subprocess.run(
        args=command,
        capture_output=True,
        shell=True,
        universal_newlines=True
    ).stdout

def main_main(*args):
    result = run_command(generate_command(module_name, func_name, ["num1", "num2"], *args))
    print(result)

def main(*args):
    main_main(*args)

if __name__=="__main__":
    main(31, 42)