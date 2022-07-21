import sys
sys.path.append('.')
from smpy import FiniteStateMachine

machine = FiniteStateMachine('docs/example_config.json')
machine.send_event("EI1")
machine.send_event("E1F")