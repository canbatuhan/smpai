import json


def build(file_path):
    config = json.load(open(file_path))
    
    # Profile Parser
    machine_id = config['machine_id']
    auto_startup = config['auto_startup']
    print('\nPROFILE')
    print('[Profile] MachineID: {} AutoStartup: {}'.format(
        machine_id, auto_startup))

    # Context Parser
    print('\nCONTEXT')
    for variable in config['variables']:
        key = variable['key']
        initial_value = variable['value']
        print('[Variable] Key: {} Value: {}'.format(
            key, initial_value))
    
    # State Parser
    print('\nSTATE')
    for state in config['states']:
        id = state['id']
        entry_action = state['entry_action']
        inner_action = state['inner_action']
        exit_action = state['exit_action']
        print('[State] ID: {}\tEntryAction: {} InnerAction: {}ExitAction: {}'.format(
            id, entry_action, inner_action, exit_action))

    # Tranistion Parser
    print('\nTRANSITION')
    for transition in config['transitions']:
        source = transition['source']
        destination = transition['destination']
        event = transition['event']
        action = transition['action']
        print('[Transition] {} - {}({}) -> {}'.format(
            source, event, action, destination))

    # Listener Parser
    print('\nLISTENER')
    listener = config['listener']
    print('[Listener] Action: {}'.format(listener))


if __name__=="__main__":
    build('resources/sm.json')
