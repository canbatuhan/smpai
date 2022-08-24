from smpy.components import StateMachineContext, Listener, Transition
from smpy.builder import StateMachineBuilder
from smpy.components.state import State


class FiniteStateMachine:
    """
        Represents the `FiniteStateMachine` structure with, `StateMachineContext`,
        `State`, `Transition`, `Action`, `Event` and `Listener` objects.
    """

    def __init__(self, config_file_path:str) -> None:
        """
            Description:
                Creates an FSM. It can be built through a
                configuration file.

            Arguments:
                - config_file_path : `str` path of the configration
                file with extension .json
        """
        components = self.__build_with_config(config_file_path)
        
        self.__machine_id = components['machine_id']
        self.__auto_startup = components['auto_startup']
        self.__context = StateMachineContext(components['variables'])
        self.__states = components['states']
        self.__transitions = components['transitions']
        self.__listener = components['listener']

        for state in self.__states:
            if state.get_id() == 'S_INIT': self.__initial_state = state
            elif state.get_id() == 'S_FINAL': self.__final_state = state
        if self.__auto_startup: self.start()


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


    def __execute_and_update(self, executable) -> None:
        """
            Description:
                Executes and executable object then updates
                state machine variables
  
            Arguments:
                - executable : `Action` or `Transition` - will be
                executed
        """
        results = executable.execute(self.__context)   
        if results is None: return
        for key, value in results.items(): self.__context.get_variables()[key] = value


    def __update_variables(self, event, transition:Transition, state:State) -> None:
        """
            Description:
                Updates the state machine variables last event, last transition
                and current state
            
            Arguments:
                - event : `Any` - event triggered the transition
                - transition : `Transition` - last triggered transition
                - state : `State` current state of the state machine
        """
        self.__context.set_last_event(event)
        self.__context.set_last_transition(transition)
        self.__context.set_current_state(state)


    def __execute_before_transition(self):
        pass


    def __execute_after_transition(self):
        pass


    def start(self) -> None:
        """
            Description:
                Initialize the state machine by setting the current
                state as initial state S_INIT.
        """
        initial_transition = Transition(None, self.__initial_state, "INIT", None)

        # Execute transition
        self.__execute_and_update(initial_transition)

        # Execute listener
        self.__listener.execute(initial_transition)

        # Update variables
        self.__update_variables("INIT", initial_transition, self.__initial_state)

        # Execute the initial state actions in order
        state_actions = self.__context.get_current_state().get_actions()
        if state_actions['entry_action'] != None:
            self.__execute_and_update(state_actions['entry_action'])
        if state_actions['inner_action'] != None:
            self.__execute_and_update(state_actions['inner_action'])


    def send_event(self, event:object) -> None:
        """
            Description:
                Sends an event to the state machine and triggers a
                transition if valid.

            Arguments:
                - event : `str` - event object (str for now).
        """
        # Seek for a transition
        transition = None
        for transition_ in self.__transitions:
            if transition_.get_source() == self.__context.get_current_state():
                if transition_.get_event() == event:
                    transition = transition_
                    break
        
        # If not found pass
        # TODO : Some explanation is needed
        if transition == None: pass

        # If found, execute exit action
        state_actions = self.__context.get_current_state().get_actions()
        if state_actions['exit_action'] != None:
            self.__execute_and_update(state_actions['exit_action'])

        # Execute transition
        self.__execute_and_update(transition)

        # Execute Listener
        self.__listener.execute(transition)
        
        # Update variables
        self.__update_variables(event, transition, transition.get_destination())

        # Execute actions in order
        state_actions = self.__context.get_current_state().get_actions()
        if state_actions['entry_action'] != None:
            self.__execute_and_update(state_actions['entry_action'])
        if state_actions['inner_action'] != None:
            self.__execute_and_update(state_actions['inner_action'])


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
        for transition_ in self.__transitions:
            if transition_.get_source() == self.__context.get_current_state():
                if transition_.get_event() == event:
                    return True
        return False


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
