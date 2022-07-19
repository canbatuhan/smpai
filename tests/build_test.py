import sys
sys.path.append("..")

from smpy import FiniteStateMachine

machine = FiniteStateMachine('../docs/example_config.json')
print(machine.get_machine_id())
