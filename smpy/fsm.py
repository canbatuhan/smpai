from smpy.statemachine.components.transition import Transition
from .statemachine.components import StateMachineContext, State, Listener
from .statemachine.builder import StateMachineBuilder

class FiniteStateMachine:
    """
        Represents the `FiniteStateMachine` structure with, `StateMachineContext`,
        `State`, `Transition`, `Action`, `Event` and `Listener` objects.
    """

    def __build_with_config(config_file_path:str) -> dict:
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


    def __init__(self, config_file_path:str=None) -> None:
        """
            Description:
                Creates an FSM. It ca be built through a
                configuration file.

            Arguments:
                - config_file_path : `str` path of the configration
                file with extension .json
        """
        self.__machine_id = str()
        self.__auto_startup = bool()
        self.__context = StateMachineContext()
        self.__states = set()
        self.__transitions = set()
        self.__listener = Listener()
        self.__initial_state = State()
        self.__final_state = State()

        if config_file_path is not None:
            components = self.__build_with_config(config_file_path)
            self.__machine_id = components['machine_id']
            self.__auto_startup = components['auto_startup']
            self.__context.set_variables(components['variables'])
            self.__states = components['states']
            self.__transitions = components['transitions']
            self.__listener = components['listener']

        for state in self.__states:
            if state.get_id() == 'S_INIT':
                self.__initial_state = state
            elif state.get_id() == 'S_FINAL':
                self.__final_state = state

        if self.__auto_startup:
            self.start()


    def start(self) -> None:
        """
            Description:
                Initialize the state machine by setting the current
                state as initial state S_INIT
        """


    def send_event(self, event:str) -> None:
        """
            Description:
                Sends an event to the state machine and triggers a
                transition if valid.

            Arguments:
                - event : `str` - event object (str for now)

            Return:
                - `bool` : True if transition is triggered, otherwise
                returns False
        """
        pass
