from .action import Action
from .state import State

class Transition:
    """
        Represents the transition component of a `FiniteStateMachine`.
        In transitions `Action` objects can be executed.
    """

    def __init__(self, source:State, destination:State, event:object, action:Action=None) -> None:
        """
            Description:
                Creates a Transition object that changes the current state,
                from `source` to `destination`.

            Arguments:
                - source : `State` - state that the transition starts.
                - destination : `State` - state that the transition ends.
                - event : `object` - event triggering the transition.
                - action : `Action` - action that will be executing during transition.

        """
        self.__source = source
        self.__destination = destination
        self.__event = event
        self.__action = action


    """
        Getters
    """
    def get_source(self) -> State:
        return self.__source

    def get_destination(self) -> State:
        return self.__destination

    def get_event(self) -> object:
        return self.__event

    def get_action(self) -> Action:
        return self.__action

    def execute(self, context) -> dict:
        if self.__action != None:
            return_value = self.__action.execute(context)
            return return_value
    