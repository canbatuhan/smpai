import sys
sys.path.append('..')

from smpy import FiniteStateMachine

sm_single = FiniteStateMachine('../docs/single_file/sm_config.yaml')
print(sm_single.get_machine_id())

sm_multiple = FiniteStateMachine('../docs/multiple_files/sm_config.yaml')
print(sm_multiple.get_machine_id())