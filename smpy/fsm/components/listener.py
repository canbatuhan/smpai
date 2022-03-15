from action import Action
from state import State
from transition import Transition


class Listener():
    """
        Represents the Listener component of a `FiniteStateMachine`.
        It follows what is happening in the state machine.
    """

    def __init__(self, package:str=None, module:str=None, function:str=None, params:set=None) -> None:
        """
            Description:
                Creates a Listener object that runs the given function.

            Arguments:
                - package : `str` - name of the package of the user-defined function
                - module : `str` - name of the module of the user-defined function
                - function : `str` - name of the user-defined function
                - params : `set` - set of parameter names, they must be variables
                stored in `StateMachineContext`
        """
        self.__action = None
        self.__custom_condition = package==None or module==None or function==None
        
        if self.__custom_condition:
            self.__action = Action(
                package=package,
                module=module,
                function=function,
                params=params
            )

    
    def __default_execution(self, transition:Transition) -> None:
        """
            Description:
                Executes the `Listener` object as default. It basically echos
                what state change is happened.

            Arguments:
                - transition : `Transition` - last transition executed 
        """
        if transition.get_source() == None:
            print("{}\t-- {} -->\t{}".format(
                " ", "INIT", transition.get_destination().get_id()))

        else:
            print("{}\t-- {} -->\t{}".format(
                transition.get_source().get_id(),
                transition.get_event(),
                transition.get_destination().get_id()))


    def execute(self, transition:Transition, **kwargs) -> None:
        """
            Description:
                Executes the `Listener` object. If a custom `Action` is defined
                as `Listener` executor, then this action is executed. Otherwise,
                default execution (`__default_execution(transition:Transition)`)
                will be held. 

            Arguments:
                - transition : `Transition` - last transition executed
                - **kwargs : `dict` - specific function parameters, they must be
                variables stored in `StateMachineContext

        """
        if self.__action != None: print(self.__action.execute(transition=transition, **kwargs))
        else: self.__default_execution(transition)
