class State:
    """
        Represents the state component of a `FiniteStateMachine`.
        It has three different types of `Action` objects; `exit_action`,
        `entry_action` and `exit_action`.
    """

    def __init__(self, state_id:str=None, entry_action=None, inner_action=None, exit_action=None) -> None:
        """
            Description:
                Creates a State object with given parameters.

            Arguments:
                - state_id : `str` - unique ID of the state.
                - entry_action : `Action` - entry action of the state.
                - inner_action : `Action` - inner action of the state.
                - exit_action : `Action` - exit action of the state.
        """
        self.__state_id = state_id
        self.__entry_action = entry_action
        self.__inner_action = inner_action
        self.__exit_action = exit_action

    def __hash__(self) -> int:
        return hash(self.__state_id)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, State):
            if __o.get_id() == self.__state_id:
                return True
        return False

    """
        Getters
    """
    def get_id(self) -> str:
        return self.__state_id

    def get_actions(self) -> dict:
        return {'entry_action': self.__entry_action,
                'inner_action': self.__inner_action,
                'exit_action': self.__exit_action}
