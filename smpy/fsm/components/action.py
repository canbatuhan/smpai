import subprocess


class Action:
    """
        Represents the action component of a `FiniteStateMachine`.
        In actions, user-defined functions are executed.
    """

    def __init__(self, package:str, module:str, function:str, params:set) -> None:
        """
            Description:
                Creates an Action object that runs the given function.

            Arguments:
                - package : `str` - name of the package of the user-defined function
                - module : `str` - name of the module of the user-defined function
                - function : `str` - name of the user-defined function
                - params : `set` - set of parameter names, they must be variables
                stored in `StateMachineContext`
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


    def __generate_command(self, **kwargs) -> str:
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
        for key, value in kwargs.items():
            if isinstance(value, str):
                arguments += "{}='{}',".format(
                    key, value)
            else:
                arguments += "{}={},".format(
                    key, value)

        return """python -c "from {}.{} import {}; print({}({}))""".format(
            self.__package, self.__module, self.__function, self.__function, arguments)


    def __run_command(self, runner_cmd) -> str:
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


    def execute(self, **kwargs) -> str:
        """
            Description:
                Executes the function embedded in action and returns the output
                as STRING, just for now.

            Arguments:
                - **kwargs : `dict` - specific function parameters, they must be
                variables stored in `StateMachineContext

            Return:
                - `str` : captured output from the execution of the function
        """
        return self.__run_command(self.__generate_command(**kwargs))
