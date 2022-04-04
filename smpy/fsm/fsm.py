from components import StateMachineContext, Listener

class FiniteStateMachine:
    """
        Represents the `FiniteStateMachine` structure with, `StateMachineContext`,
        `State`, `Transition`, `Action`, `Event` and `Listener` objects.
    """

    def __init__(self, config_file_path:str=None) -> None:
        """
            Description:
                Creates an unbuilt FSM. It can built through
                an configuration file.

            Arguments:
                - config_file_path : `str` - path of the configuration file
        """
        self.__config_file_path = config_file_path
        self.__machine_id = None
        self.__auto_startup = None
        self.__initial_state = None
        self.__final_state = None
        self.__context = StateMachineContext()
        self.__states = set()
        self.__transitions = set()
        self.__listener = Listener()


    def __build_with_configuration(self, configuration:dict) -> None:
        """
            Description:
                Builds the FSM with the given configuration, read
                from the configuration file

            Arguments:
                - configuration : `dict` - configuration data for
                the `FiniteStateMachine`
        """
        pass


    def build(self) -> None:
        pass
    

    def start(self) -> None:
        pass


    def send_event(self) -> None:
        pass
