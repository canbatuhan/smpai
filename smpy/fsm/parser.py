from components import Action, Listener, State, Transition


class JSONParser:
    """
        Parser to build a state machine by reading inputs
        from a .json file.
    """

    def __init__(self) -> None:
        pass


    def parse_variables(self, variables_config:list) -> dict:
        """
            Description:
                Parse the variables given in the .json
                configuration file.

            Arguments:
                - variables_config : `dict` - configraution data
                for the variables of the state machine.

            Return:
                - `dict` : dictionary storing variables with keys.
        """
        variables = dict()

        for variable in variables_config:
            key = variable['key']
            initial_value = variable['initial_value']
            data_type = variable['type']

            if data_type == 'str':
                initial_value = str(initial_value)

            elif data_type == 'int':
                initial_value = int(initial_value)

            elif data_type == 'float':
                initial_value = float(initial_value)

            variables[key] = initial_value

        return variables


    def parse_states(self, states_config:list) -> set:
        """
            Description:
                Parse the states given in the .json
                configuration file

            Arguments:
                - states_config : `list` - configraution data
                for the states of the state machine

            Return:
                - `dict` : set storing `State` objects
        """
        states = set()

        for state in states_config:
            state_id = state['id']
            entry_action = state['entry_action']
            inner_action = state['inner_action']
            exit_action = state['exit_action']
            
            if entry_action is not None:
                entry_action = Action(
                    package = entry_action['package'],
                    module = entry_action['module'],
                    function = entry_action['function'],
                    params = entry_action['params'])

            if inner_action is not None:
                inner_action = Action(
                    package = inner_action['package'],
                    module = inner_action['module'],
                    function = inner_action['function'],
                    params = inner_action['params'])

            if exit_action is not None:
                exit_action = Action(
                    package = exit_action['package'],
                    module = exit_action['module'],
                    function = exit_action['function'],
                    params = exit_action['params'])

            states.add(State(state_id, entry_action, inner_action, exit_action))

        return states


    def parse_transitions(self, transitions_config:list) -> set:
        """
            Description:
                Parse the transitions given in the .json
                configuration file

            Arguments:
                - transitions_config : `list` - configraution data
                for the states of the state machine

            Return:
                - `dict` : set storing `Transition` objects
        """
        transitions = set()

        for transition in transitions_config:
            source = transition['source']
            destination = transition['source']
            event = transition['event']
            action = transition['action']

            if action is not None:
                action = Action(
                    package = action['package'],
                    module = action['module'],
                    function = action['function'],
                    params = action['params'])

            transitions.add(Transition(source, destination, event, action))
        
        return transitions


    def parse_listener(self, listener_config:dict) -> Listener:
        """
            Description:
                Parse the listener given in the .json
                configuration file

            Arguments:
                - listener_config : `dict` - configraution data
                for the listener of the state machine

            Return:
                - `dict` : state machine's `Listener` object
        """
        listener = Listener()

        if listener_config is not None:
            listener = Listener(
                    package = listener_config['package'],
                    module = listener_config['module'],
                    function = listener_config['function'],
                    params = listener_config['params'])

        return listener
