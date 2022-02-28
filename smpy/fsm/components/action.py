from typing import Any


class Action:
    """
        Represents the action component of a finite state machine.
        In actions, user-defined functions are executed.
    """

    def __init__(self, function:function) -> None:
        """
            Description:
                Creates an Action object that runs the given function.

            Arguments:
                - function : `function`, it will be executed in the action
        """
        self.__function = function

    def execute(self) -> Any:
        return self.__function
