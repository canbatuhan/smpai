import json
import yaml
from smpy.components import Action, Listener, State, Transition


class Parser:
    """
        Parser to build a state machine by reading inputs
        from a configuration file.
    """

    def __init__(self) -> None:
        self.config = dict()

    def parse_machine_id(self) -> str:
        """
            Description:
                Parse the unique ID of the state machine.

            Return: 
                - `str` : unique ID of the state machine.
        """
        return self.config['profile']['machine_id']

    def parse_auto_startup(self) -> bool:
        """
            Description:
                Parse the auto startup information of the
                state machine.

            Return:
                - `bool` : True, if the state machine will start
                as it created, false otherwise.
        """
        return self.config['profile']['auto_startup']

    def parse_variables(self) -> dict:
        """
            Description:
                Parse the variables given in the configuration
                configuration file.

            Return:
                - `dict` : dictionary storing variables with keys.
        """
        variables = dict()

        for variable in self.config['variables']:
            key = variable['key']
            initial_value = variable['value']
            data_type = variable['type']

            if data_type == 'str':
                initial_value = str(initial_value)

            elif data_type == 'int':
                initial_value = int(initial_value)

            elif data_type == 'float':
                initial_value = float(initial_value)

            variables[key] = initial_value

        return variables

    def parse_states(self) -> set:
        """
            Description:
                Parse the states given in the configuration
                configuration file.

            Return:
                - `dict` : set storing `State` objects.
        """
        states = set()

        for state in self.config['states']:
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

    def parse_transitions(self) -> set:
        """
            Description:
                Parse the transitions given in the configuration
                configuration file.

            Return:
                - `dict` : set storing `Transition` objects.
        """
        transitions = set()

        for transition in self.config['transitions']:
            source = transition['source']
            destination = transition['destination']
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

    def parse_listener(self) -> Listener:
        """
            Description:
                Parse the listener given in the configuration
                configuration file.

            Return:
                - `dict` : state machine's `Listener` object.
        """
        listener = Listener()

        if self.config['listener'] is not None:
            listener = Listener(
                    package = self.config['listener']['package'],
                    module = self.config['listener']['module'],
                    function = self.config['listener']['function'],
                    params = self.config['listener']['params'])

        return listener


class JSONParser(Parser):
    def __init__(self, file_path:str) -> None:
        """
            Description:
                Creates a `JSONParser` object in order to parse
                JSON file storing configuration data of a state
                machine.

            Arguments:
                - file_path : `str` - path of the configuration file.
        """
        self.config = json.load(open(file_path, 'r'))


class YAMLParser(Parser):
    def __init__(self, file_path:str) -> None:
        """
            Description:
                Creates a `YAMLParser` object in order to parse
                YAML file storing configuration data of a state
                machine.

            Arguments:
                - file_path : `str` - path of the configuration file.
        """
        self.config = yaml.safe_load(open(file_path, 'r'))


class MultiConfigParser(Parser):
    def __init__(self, file_path:str) -> None:
        """
            Description:
                Creates a `MultiConfigParser` object in order to parse
                multiple configuration files storing configuration data
                of a state machine.

            Arguments:
                - file_path : `str` - path of the configuration file.
        """
        pass
