# smpai - State Machine Framework
`smpai` is a framework to configure, build and run different types of state machines with custom states and custom actions. In this framework, aim is to provide an environment, in where the programmer is able to;

- Configure state machines easily, through configuration files such as `JSON` and `YAML`.
- Build state machines in the background, so the programmer will not be dealing with any unnecessary coding.
- Run state machines and execute custom actions (pre-written packages, modules and functions) while running.


## Context
  #### [Different Types Of State Machines](#different-types-of-state-machines-1)
  #### [Configuring A State Machine](#configuring-a-state-machine-1)
  #### [Building In The Background](#building-in-the-background-1)
  #### [Using Custom Actions](#using-custom-actions-1)
  #### [Running A State Machine](#running-a-state-machine-1)


## Different Types Of State Machines
For now, there is only one type of state machine defined in `smpai`, named `FiniteStateMachine`.

### Finite-State Machine
It is a type of state machine which has a finite number of states. In `FiniteStateMachine`, transitions are triggered by events. Therefore, it is better to use this type of a state machine in the programs that are event-driven.


## Configuring A State Machine
`smpai` provides that a state machine can be configured through a single file. A state machine can also be configured through multiple configuration files by splitting the state machine configurations into sections.

### Configuring State Machines Through A Single File
Using configuration files is a bit uncomfortable for the programmer, however it is still easy to parse these files in the background. A state machine can be built through a single file easily, but there are some configurations rules that the programmer should consider.

In `sm-py`, there are built-in parsers written for `JSON` and `YAML` files. Therefore, it is available for the user to pass configuration files with these extensions as an argument when building a state machine. For now, user is not able to write a custom parser. However, it is planned to be a feature in the stable release.

### Configuring State Machines Through Multiple Files
For more complex state machines, using multiple configuration files would be more easy for the programmer to configure a state machine. Single configuration files for each section such as `states.yaml`, `transitions.yaml`, etc can be configured, later these configuration files can be imported in a main configuration file. Multiple configuration files are handled with an `XML` parser. With this built-in parser, configuration files with different extension can bu used together.


## Building In The Background
In order to build state machines, `smpai` parses configuration inputs given by the programmer. State machine is built when the programmer create a `StateMachine` object. Building a state machine is not a consideration for the user in `smpai`. However as a further step, a builder class will be written to make the programmer able to built a statemachine with code.


## Using Custom Actions
`smpai` provides an option for the programmer to use pre-written function in a state machine. In the configuration file, package, module and function name must be given to use a function as a executable object (`Action` or `Transition`) in the state machine


## Running A State Machine
For now there is only one type of a state machine in `smpai` called `FiniteStateMachine`. In this type of state machine, transitions are triggered by events, therefore while running the state machine. User should send events to the state machine. Also there is an option such that the programmer checks if the incoming event triggers the state machine or not. 
