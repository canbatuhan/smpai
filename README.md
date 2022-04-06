<h1>smpy - State Machine Framework</h1>

<div>
    <p>smpy is a framework to configure, build and run different types of state machines with custom states and custom actions. In smpy, aim is to provide an environment, in where the programmer is able to;</p>
    
    <ul>
      <li>Configure state machines easily, through configuration files such as JSON, YAML, etc.</li>
      <li>Build state machines in the background, so the programmer will not be dealing with any unnecessary coding.</li
      <li>Run state machines by sending events (can be custom objects, or just strings) and execute custom actions (pre-written packages, modules and functions) while running.</li>
    </ul>
    
    <div>
        <h2>Different Types Of State Machines</h2>
        <p>For now, there is only one type of state machine defined in smpy.</p>
        <ul>
            <li>
                <dt>Finite-State Machine</dt>
                <dd>It is a type of state machine which has a finite number of states. In Finite-State Machine, transitions are triggered by events. Therefore, it is better to use a Finite-State Machine in programs that are event-driven.
            </li>
        </ul>
    </div>
  
    <div>
        <h2>Configuring A State Machine</h2>
        <p>For now, there is only one way to build a state machine in smpy.</p>
        <ul>
            <li>
                <dt>Configuring A State Machine Through JSON File</dt>
                <dd>Using JSON configuration files is bit of uncomfortable for the programmer, however it is still easy to configure and parse in the background.</dd>
            </li>
        </ul>
    </div>
</div>
