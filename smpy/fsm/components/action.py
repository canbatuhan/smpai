import os
from typing import Any


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
        self.__mmodule_name = action_config.get('module')
        self.__function_name = action_config.get('function')

    def __generate_command():
        pass
    
    def execute(self) -> Any:
        pass
