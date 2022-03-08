from action import Action
from state import State

class Transition:
    """
        Represents the transition component of a finite state machine.
        In transitions actions can be executed.
    """

    def __init__(self, source:State, destination:State, action:Action=None) -> None:
        """
            Description:
                Creates a Transition object that changes the current state,
                from `source` to `destination`.

            Arguments:
                - source : `State`, state that the transition starts
                - destination : `State`, state that the transition ends
                - action : `Action`, action that will be executing during transition

        """
        self.__source = source
        self.__destination = destination
        self.__action = action

    
    def __str__(self) -> str:
        """
            Description:
                Representation of a Transation object as string
        """
        return "[Source: {}, Destination: {}, Action: {}]".format(
            self.__source, self.__destination, self.__action)


    def execute(self) -> bool:
        pass
    