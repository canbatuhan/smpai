from .parser import JSONParser, YAMLParser


class StateMachineBuilder:
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
