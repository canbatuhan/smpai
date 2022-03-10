import subprocess
from action import Action
from state import State

class Listener():
    """
        Represents the Listener component of a finite state machine.
        It follows what is happening in the state machine.
    """

    def __init__(self, package:str=None, module:str=None, function:str=None, params:dict=None) -> None:
        """
            Description:
                Creates a Listener object that runs the given function

            Arguments:
                - package : `str`, name of the package
                - module : `str`, name of the module
                - function : `str`, name of the function
                - arguments : `dict`, specific arguments with keywords
        """
        self.__action = None
        self.__custom_condition = package==None or module==None or function==None or params==None
        
        if self.__custom_condition:
            self.__action = Action(
                package=package,
                module=module,
                function=function,
                params=params
            )

    
    def __default_execution(self, from_state:State, to_state:State, event:object) -> None:
        if from_state == None: print("-- INIT -->\t{}".format("", event, to_state))
        else: print("{}\t-- {} -->\t{}".format(from_state, event, to_state))


    def execute(self, from_state:State, to_state:State, event:object, *args) -> None:
        if self.__action != None: print(self.__action.execute(*args))
        else: self.__default_execution(from_state, to_state, event)
