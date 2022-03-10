from components import StateMachineContext, Listener

class FiniteStateMachine:
    """
        Represents the Finite State Machine structure with,
        context, states, transitions, actions and a listener.
        It can be built through configuration file.
    """

    def __init__(self, config_file_path:str) -> None:
        """
            Description:
                Creates an unbuilt FSM. It can built through
                an configuration file.

            Arguments:
                - config_file_path : `str`, path of the configuration file
        """
        self.__config_file_path = config_file_path
        self.__context = StateMachineContext()
        self.__states = set()
        self.__transitions = set()
        self.__actions = set()
        self.__listener = Listener()


    def __build_with_configuration(self, configuration:dict) -> None:
        """
            Description:
                Builds the FSM with the given configuration, read
                from the configuration file

            Arguments:
                - configuration : `dict`, config data of FSM
        """
        pass


    def build(self) -> None:
        pass
    

    def start(self) -> None:
        pass


    def send_event(self, event:object) -> bool:
        pass
