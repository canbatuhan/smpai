# smpy - State Machine Framework
smpy is a framework to configure, build and run different types of state machines with custom states and custom actions. In smpy, aim is to provide an environment, in where the programmer is able to;

- Configure state machines easily, through configuration files such as JSON and YAML.
- Build state machines in the background, so the programmer will not be dealing with any unnecessary coding.
- Run state machines and execute custom actions (pre-written packages, modules and functions) while running.

## Context
  #### [Different Types Of State Machines](#different-types-of-state-machines-1)
  #### [Configuring A State Machine](#configuration-a-state-machine-1)
  #### [Building In The Background](#building-in-the-background-1)
  #### [Using Custom Actions](#using-custom-actions-1)
  #### [Running A State Machine](#running-a-state-machine-1)

## Different Types Of State Machines
For now, there is only one type of state machine defined in smpy.

### Finite-State Machine
It is a type of state machine which has a finite number of states. In a Finite-State Machine implemented in smpy, transitions are triggered by events. Therefore, it is better to use a Finite-State Machine in programs that are event-driven.


## Configuring A State Machine
In smpy, a state machine can be configured through a single JSON or YAML file. A state machine also can be configured through multiple JSON or YAML files by splitting the state machine configuration into sections.

### Configuring State Machines Through A Single JSON File
Using JSON configuration files is a bit uncomfortable for the programmer, however it is still easy to configure and parse JSON files in the background. A state machine can be built through a single JSON file easily, but there are some configurations rules that the programmer should consider. An example JSON file would have the following structure;

    `
    {
        "profile": {
            "machine_id": "An Example Machine",
            "auto_startup": true
        },

        "variables": [
            {
                "key": "handsome",
                "value": "Racoon",
                "type": "str"
            }
        ]

        "states": [
            {
                "id": "S_INIT",
                "entry_action": null,
                "inner_action": null,
                "exit_action": null
            }
            
            ...
            
            {
                "id": "S_FINAL",
                "entry_action": null,
                "inner_action": {
                    "package": "image_proc",
                    "module": "object_detection",
                    "function": "detect_awsome_racoons",
                    "params": ["handsome"]
                },
                "exit_action": null
            }
        ],

        "transitions": [
            {
                "source": "S_INIT",
                "destination": "S_FINAL",
                "event": "EI1",
                "action": null
            }
            
            ...
        ],

        "listener": null
    }
    `

### Configuring State Machines Through Multiple JSON Files
For more complex state machines, using multiple JSON files would be more easy for the programmer to configure a state machine. JSON files for each section such as _states_, _transitions_, etc. later these configuration files can be imported in a main JSON file, for example _sm_config.json_
