import subprocess
from action import Action
from state import State

class Listener():
    """
        Represents the Listener component of a finite state machine.
        It follows what is happening in the state machine.
    """

    def __init__(self) -> None:
        """
            Description:
                Creates a default Listener object (without a custom action)
        """
        self.__action = None


    def __init__(self, package: str, module: str, function: str, params: dict) -> None:
        """
            Description:
                Creates a Listener object that runs the given function

            Arguments:
                - package : `str`, name of the package
                - module : `str`, name of the module
                - function : `str`, name of the function
                - arguments : `dict`, specific arguments with keywords
        """
        self.__action = Action(
            package=package,
            module=module,
            function=function,
            params=params
        )

    
    def __default_execution(self, from_state:State, to_state:State, event:object) -> None:
        if from_state == None: print("-- INIT -->\t{}".format("", event, to_state))
        else: print("{}\t-- {} -->\t{}".format(from_state, event, to_state))


    def execute(self, from_state:State, to_state:State, event:object, *args) -> None:
        if self.__action != None: print(self.__action.execute(*args))
        else: self.__default_execution(from_state, to_state, event)
