# smpy - State Machine Framework

`smpy` is a framework to configure, build and run different types of state machines with custom states and custom actions. In this framework, aim is to provide an environment, in where the programmer is able to;

- Configure state machines easily, through configuration files such as `JSON` and `YAML`.
- Build state machines in the background, so the programmer will not be dealing with any unnecessary coding.
- Run state machines and execute custom actions (pre-written packages, modules and functions) while running.

## Context

  #### [Different Types Of State Machines](#different-types-of-state-machines-1)
  #### [Configuring A State Machine](#configuration-a-state-machine-1)
  #### [Building In The Background](#building-in-the-background-1)
  #### [Using Custom Actions](#using-custom-actions-1)
  #### [Running A State Machine](#running-a-state-machine-1)

## Different Types Of State Machines

For now, there is only one type of state machine defined in `smpy`, named `Finite-State Machine`.


### Finite-State Machine

It is a type of state machine which has a finite number of states. In `Finite-State Machine`, transitions are triggered by events. Therefore, it is better to use a this type of a state machine in the programs that are event-driven.


## Configuring A State Machine

In smpy, a state machine can be configured through a single `JSON` or `YAML` file. A state machine also can be configured through multiple configuration files by splitting the state machine configuration into sections.

### Configuring State Machines Through A Single File

Using configuration files is a bit uncomfortable for the programmer, however it is still easy to parse these files in the background with `Python`. A state machine can be built through a single `JSON` or `YAML` file easily, but there are some configurations rules that the programmer should consider.

### Configuring State Machines Through Multiple Files

For more complex state machines, using multiple configuration files would be more easy for the programmer to configure a state machine. Single configuration files for each section such as `states.yaml`, `transitions.yaml`, etc can be configured, later these configuration files can be imported in a main configuration file.

