import os
from typing import Any


class Action:
    """
        Represents the action component of a finite state machine.
        In actions, user-defined functions are executed.
    """

    def __init__(self, function_path:str) -> None:
        """
            Description:
                Creates an Action object that runs the given function.

            Arguments:
                - function_path : `str`, it will be executed in the action
        """
        self.__function_path = function_path

    def execute(self) -> Any:
        return os.system('python {}'.format(self.__function_path))
