import json
from .parser import JSONParser


class StateMachineBuilder:
    """
        Builder class to build a state machine through
        configuration files.
    """

    def __init__(self, config_file_path:str) -> None:
        """
            Description:
                Creates a builder object, which uses parsers
                to build a `FiniteStateMachine`
        """
        self.__config_file_path = config_file_path
        self.__parser = None
        extension = config_file_path.split('.')[-1]
        if extension == 'json':
            self.__parser = JSONParser()


    def build(self) -> dict:
        """
            Description:
                Creates the components of the state machine
                by using parsers.

            Return:
                - `dict` : components of the `FiniteStateMachine`.
        """
        config = json.load(open(self.__config_file_path, 'r'))

        return {
            'machine_id': config['machine_id'],
            'auto_startup': config['auto_startup'],
            'variables': self.__parser.parse_variables(config['variables']),
            'states': self.__parser.parse_states(config['states']),
            'transitions': self.__parser.parse_transitions(config['transitions']),
            'listener': self.__parser.parse_listener(config['listener'])
        }
