from typing import Any
import subprocess


def __generate_command(module:str, function:str, **kwargs) -> str:
    """
        Description:
            Generates a one-line python script to run the
            given function in the given module
        
        Arguments:
            - module : `str`, name of the module
            - function : `str`, name of the function
            - kwargs : `dict`, specific arguments with keywords

        Return:
            - `str` : generated command to run the function
    """
    arguments = ""
    for key, value in kwargs.items():
        arguments += "{}={},".format(key, value)

    return """python -c "from {} import {}; print({}({}))""".format(
        module, function, function, kwargs)


def __run_command(command:str) -> str:
    """
        Description:
            Runs the command previously generated and
            capture the output (via. print function used
            in the generated command)

        Arguments:
            - command : `str`, previously generated command

        Return:
            - `str` : captured ouput from command line (can be casted)
    """
    return subprocess.run(
        args=command,
        capture_output=True,
        shell=True,
        universal_newlines=True
    ).stdout


class Action:
    """
        Represents the action component of a finite state machine.
        In actions, user-defined functions are executed.
    """

    def __init__(self, action_config:dict) -> None:
        """
            Description:
                Creates an Action object that runs the given function.

            Arguments:
                - action_config : `dict`, configuration for the action
        """
        self.__module = action_config.get('module')
        self.__function = action_config.get('function')
        self.__arguments = action_config.get('arguments')


    def __str__(self) -> str:
        """
            Description:
                Representation an Action object as string 
        """
        return "[Module: {}, Function {}]".format(
            self.__module, self.__function)


    def execute(self) -> str:
        """
            Description:
                Executes the function embedded in action and returns
                the output value as STRING, for now.

            Arguments:
                - **kwargs : `dict`, specific arguments with keywords
        """
        return __run_command(
            __generate_command(
                module=self.__module,
                function=self.__function,
                kwargs=self.__arguments
            )
        )
