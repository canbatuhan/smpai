import subprocess
import json


def __generate_command(package, module, function, parameters_to_send) -> str:
        """
            Description:
                Generates a one-line python script to run the given function
                implemented in the given module of the given package
            
            Arguments:
                - **kwargs : `dict` - specific function parameters, they must be
                variables stored in `StateMachineContext`

            Return:
                - `str` : generated command to run the user-defined function
        """
        arguments = ""
        for key, value in parameters_to_send.items():
            if isinstance(value, str): arguments += "{}='{}',".format(key, value)
            else: arguments += "{}={},".format(key, value)

        print("""python -c "from {}.{} import {}; print({}({}))""".format(
            package, module, function, function, arguments))

        return """python -c "from {}.{} import {}; print({}({}))""".format(
            package, module, function, function, arguments)


def __run_command(runner_cmd) -> str:
    """
        Description:
            Runs the command previously generated and capture the output
            (via. print function used in the generated command).

        Arguments:
            - runner_cmd : `str` - commands generated with the given parameters

        Return:
            - `str` : captured output from command line (can be casted)
    """
    return subprocess.run(
        args=runner_cmd,
        capture_output=True,
        shell=True,
        universal_newlines=True
    ).stdout


# sm.get_variables()
VARIABLES = {
    "age": 42,
    "gender": "female"
}

if __name__ == "__main__":
    json_file = open('resources/action.json')
    action_config = json.load(json_file)

    # There is something like this in back-end
    parameters_to_send = dict()
    for key in action_config.get('params'):
        parameters_to_send.update({key: VARIABLES.get(key)})

    # Action object does this
    return_value = __run_command(
        __generate_command(
            action_config.get('package'),
            action_config.get('module'),
            action_config.get('function'),
            parameters_to_send
        )
    )

    print(return_value)