import os
import subprocess

package = 'src'
module = 'summation'
function = 'sum'
params = ["num1", "num2"]

def generate_command(package, module, function, params, *args):
    print(args)
    keyword_args = ""
    for index, param in enumerate(params):
        keyword_args += "{}={},".format(
            param, args[index])
            
    return f"""python -c "from {package}.{module} import {function}; print({function}{args})"""

def run_command(command):
    return subprocess.run(
        args=command,
        capture_output=True,
        shell=True,
        universal_newlines=True
    ).stdout

def main(*args):
    command = generate_command(package, module, function, params, *args)
    print(run_command(command))

if __name__=="__main__":
    main(31, 42)
