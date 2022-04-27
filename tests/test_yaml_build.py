import sys
sys.path.append('..')

from smpy import FiniteStateMachine

sm_single = FiniteStateMachine('../docs/single_file/sm_config.yaml')
print(sm_single.get_machine_id())