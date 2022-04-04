from components import StateMachineContext, State, Action, Listener
from smpy.fsm.builder import StateMachineBuilder

class FiniteStateMachine:
    """
        Represents the `FiniteStateMachine` structure with, `StateMachineContext`,
        `State`, `Transition`, `Action`, `Event` and `Listener` objects.
    """

    def __init__(self, config_file_path:str=None) -> None:
        """
            Description:
                Creates an FSM. It ca be built through a
                configuration file.

            Arguments:
                - config_file_path : `str` path of the configration
                file with extension .json
        """
        if config_file_path is not None:
            components = self.__build_with_config(config_file_path)
            self.__machine_id = components['id']
            self.__auto_startup = components['autostartup']

            self.__context = StateMachineContext()
            self.__context.set_variables(components['variables'])

            self.__states = components['states']
            self.__initial_state = "S_INIT"
            self.__final_state = "S_FINAL"
            
            self.__transitions = components['transitions']
            self.__listener = components['listener']


    def __build_with_config(self, config_file_path:str) -> dict:
        """
            Description:
                Builds the FSM with the given configuration, read
                from the configuration file

            Arguments:
                - config_file_path : `str` - configuration file for
                the `FiniteStateMachine`

            Return:
                - `dict` : components of the `FiniteStateMachine`
        """
        builder = StateMachineBuilder(config_file_path)
        components = builder.build()
        return components
        

    def start(self) -> None:
        pass


    def send_event(self) -> None:
        pass
