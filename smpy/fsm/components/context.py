from state import State
from transition import Transition
from listener import Listener

class StateMachineContext:
    """
        State machine context stores information related to
        the current situation of the state machine and stores
        machine specific variables (defined by the programmer)
    """

    def __init__(self) -> None:
        """
            Description:
                Creates a StateMachineContext object
        """
        self.__machine_id = None
        self.__auto_start = None
        self.__current_state = None
        self.__last_event = None
        self.__last_transition = None
        self.__variables = dict()
        self.__states = set()
        self.__transitions = set()
        self.__actions = set()
        self.__listener = Listener()

    """
        Getters
    """
    def get_id(self) -> str:
        return self.__machine_id

    def get_auto_start(self) -> bool:
        return self.__auto_start

    def get_current_state(self) -> State:
        return self.__current_state

    def get_last_event(self) -> object:
        return self.__last_event

    def get_last_transition(self) -> Transition:
        return self.__last_transition

    def get_variables(self) -> dict: 
        return self.__variables

    def get_states(self) -> set:
        return self.__states

    def get_transitions(self) -> set:
        return self.__transitions

    def get_actions(self) -> set:
        return self.__actions

    def get_listener(self) -> Listener:
        return self.__listener


    """
        Setters
    """
    def set_id(self, machine_id:str) -> None:
        self.__machine_id = machine_id

    def set_auto_start(self, auto_start:bool) -> None:
        self.__auto_start = auto_start

    def set_current_state(self, state:State) -> None:
        self.__current_state = state

    def set_last_event(self, event:object) -> None:
        self.__last_event = event

    def set_last_transition(self, transition:Transition) -> None:
        self.__last_transition = transition

    def set_variables(self, variables:dict) -> None:
        self.__variables = variables

    def set_states(self, states:set) -> None:
        self.__states = states

    def set_transitions(self, transitions:set) -> None:
        self.__transitions = transitions

    def set_actions(self, actions:set) -> None:
        self.__actions = actions

    def set_listener(self, listener:Listener) -> None:
        self.__listener = listener
