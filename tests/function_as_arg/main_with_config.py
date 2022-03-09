import json
import os
import subprocess


json_file = 'resources/pyfile.json'

def generate_command(module_name, func_name, **kwargs):
    arguments = ""
    for key, value in kwargs.items(): arguments += f"{key}={value},"
    return f"""python -c "from {module_name} import {func_name}; print({func_name}({arguments}))"""

def run_command(command):
    return float(subprocess.run(
        args=command,
        capture_output=True,
        shell=True,
        universal_newlines=True
    ).stdout)


if __name__=="__main__":
    functions = json.load(open(json_file, "r"))
    
    sum_func = functions["sum_func"]
    mul_func = functions["mul_func"]

    sum_cmd = generate_command(sum_func["module"], sum_func["function"])
    mul_func = generate_command(mul_func["module"], mul_func["function"])

    sum_result = run_command(sum_cmd)
    mul_result = run_command(mul_func)

    print("Sum: {}".format(sum_result))
    print("Mul: {}".format(mul_result))

    final_result = sum_result + mul_result
    print("Result: {}".format(final_result))
