import sys
sys.path.append("..")

from smpy import FiniteStateMachine

machine = FiniteStateMachine('../docs/example_config.json')
print("[MACHINE ID] -", machine.get_machine_id())
print("[VARIABLES] -",machine.get_context().get_variables())