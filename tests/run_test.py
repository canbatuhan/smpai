import sys
sys.path.append('.')
from smpai import FiniteStateMachine

machine = FiniteStateMachine('docs/example_config.json')

for _ in range(5):
    machine.send_event("EI1")
    machine.send_event("E1I")

machine.send_event("EI1")
machine.send_event("E1F")