from action import Action

class State:
    """
        Represents the state component of a finite state machine.
        It has three different types of actions; `exit_action`, `entry_action`,
        exit_action.
    """

    def __init__(self, state_id:str, entry_action:Action=None, inner_action:Action=None, exit_action:Action=None) -> None:
        """
            Description:
                Creates a State object with given parameters.

            Arguments:
                - state_id : `str`, unique ID of the state
                - entry_action : `Action`, it will be executed before entering the state
                - inner_action : `Action`, it will be executed inside of the state
                - exit_action : `Action`, it will be executed after exiting the state
        """
        self.__state_id = state_id
        self.__entry_action = entry_action
        self.__inner_action = inner_action
        self.__exit_action = exit_action
