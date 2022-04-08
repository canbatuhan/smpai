import sys
sys.path.append('..')

from smpy.fsm import FiniteStateMachine
sm = FiniteStateMachine('../docs/example_config.json')

print(sm.get_machine_id())