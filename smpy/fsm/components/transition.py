from action import Action
from state import State

class Transition:
    def __init__(self, source:State, destination:State, action:Action=None) -> None:
        pass

    def execute(self) -> bool:
        pass
    