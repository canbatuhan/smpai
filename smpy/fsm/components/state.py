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
                - entry_action : `Action`, entry action of the state
                - inner_action : `Action`, inner action of the state
                - exit_action : `Action`, exit action of the state
        """
        self.__state_id = state_id
        self.__entry_action = entry_action
        self.__inner_action = inner_action
        self.__exit_action = exit_action


    def __str__(self) -> str:
        """
            Description:
                Representation of a State object as string.
        """
        return "[StateID: {}, EntryAction: {}, InnerAction: {}, ExitAction: {}]".format(
            self.__state_id, self.__entry_action, self.__inner_action, self.__exit_action)


    """
        Getters
    """
    def get_id(self) -> str:
        return self.__state_id

    def get_actions(self) -> dict:
        return {
            'entry_action': self.__entry_action,
            'inner_action': self.__inner_action,
            'exit_action': self.__exit_action
        }
