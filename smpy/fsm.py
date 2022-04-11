from .statemachine import StateMachineContext, State, Listener
from .parser import JSONParser, YAMLParser


class FiniteStateMachineBuilder:
    """
        Builder class to build a state machine through
        configuration files.
    """

    def __init__(self, config_file_path:str) -> None:
        """
            Description:
                Creates a builder object, which uses parsers
                to build a `FiniteStateMachine`.
        """
        self.__parser = None
        extension = config_file_path.split('.')[-1]
        if extension == 'json':
            self.__parser = JSONParser(config_file_path)
        if extension == 'yaml' or extension == 'yml':
            self.__parser = YAMLParser(config_file_path)


    def build(self) -> dict:
        """
            Description:
                Creates the components of the state machine
                by using parsers.

            Return:
                - `dict` : components of the `FiniteStateMachine`.
        """
        return {
            'machine_id': self.__parser.parse_machine_id(),
            'auto_startup': self.__parser.parse_auto_startup(),
            'variables': self.__parser.parse_variables(),
            'states': self.__parser.parse_states(),
            'transitions': self.__parser.parse_transitions(),
            'listener': self.__parser.parse_listener()
        }


class FiniteStateMachine:
    """
        Represents the `FiniteStateMachine` structure with, `StateMachineContext`,
        `State`, `Transition`, `Action`, `Event` and `Listener` objects.
    """

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
        builder = FiniteStateMachineBuilder(config_file_path)
        components = builder.build()
        return components


    def __init__(self, config_file_path:str=None) -> None:
        """
            Description:
                Creates an FSM. It can be built through a
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
                state as initial state S_INIT.
        """
        # TODO : execute initial transition
        # TODO : execute initial listener

        # TODO : set the initial state as current state
        # TODO : execute entry_action
        # TODO : execute inner_action


    def send_event(self, event:str) -> None:
        """
            Description:
                Sends an event to the state machine and triggers a
                transition if valid.

            Arguments:
                - event : `str` - event object (str for now).
        """
        # TODO : find corresponding transition, if any
        # TODO : execute exit_action
        # TODO : execute transition
        # TODO : execute listener
        
        # TODO : set last_event as event
        # TODO : set last_state as current_state
        # TODO : set current_state as destination_state
        # TODO : execute entry_action
        # TODO : execute inner_action


    def check_event(self, event:str) -> bool:
        """
            Description:
                Checks if the given event can trigger the state machine,
                but not execute actions.

            Arguments:
                - event : `str` - event object (str for now).
            
            Return:
                - `bool` : True if the event can trigger the state machine.
        """
        # TODO : find corresponding transition, if any


    """
        Getters
    """
    def get_machine_id(self) -> str:
        return self.__machine_id

    def get_auto_startup(self) -> bool:
        return self.__auto_startup

    def get_context(self) -> StateMachineContext:
        return self.__context

    def get_states(self) -> set:
        return self.__states

    def get_transitions(self) -> set:
        return self.__transitions

    def get_listener(self) -> Listener:
        return self.__listener
