import subprocess

from click import argument


def __generate_command(package:str, module:str, function:str, **kwargs) -> str:
    """
        Description:
            Generates a one-line python script to run the
            given function in the given module
        
        Arguments:
            - package: `str`, name of the package
            - module : `str`, name of the module
            - function : `str`, name of the function
            - **kwargs : `dict`, specific function parameters

        Return:
            - `str` : generated command to run the function
    """
    arguments = ""
    for key, value in kwargs.items():
        arguments += "{}={},".format(
            key, value)

    return """python -c "from {}.{} import {}; print({}({}))""".format(
        package, module, function, function, arguments)


def __run_command(command:str) -> str:
    """
        Description:
            Runs the command previously generated and
            capture the output (via. print function used
            in the generated command).

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

    def __init__(self, package:str, module:str, function:str, params:set) -> None:
        """
            Description:
                Creates an Action object that runs the given function.

            Arguments:
                - package : `str`, name of the package
                - module : `str`, name of the module
                - function : `str`, name of the function
                - params : `set`, set of parameters
        """
        self.__package = package
        self.__module = module
        self.__function = function
        self.__params = params


    def __str__(self) -> str:
        """
            Description:
                Representation an Action object as string 
        """
        return "[Package: {}, Module: {}, Function: {}, Params: {}]".format(
            self.__package, self.__module, self.__function, self.__params)


    def execute(self, **kwargs) -> str:
        """
            Description:
                Executes the function embedded in action and returns
                the output value as STRING, for now.

            Arguments:
                - **kwargs : `dict`, specific function parameters
        """
        return __run_command(
            __generate_command(
                package=self.__package,
                module=self.__module,
                function=self.__function,
                **kwargs
            )
        )
