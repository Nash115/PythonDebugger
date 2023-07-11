# PythonDebugger
A python program that allows you to easily debug pythons programs and see the history of values of desired variables.

## How to use

### Setup

[Download the lastest version of the debugger](https://github.com/Nash115/PythonDebugger/releases)

Import the debugger in your program : (It must be in the same folder as your program) and create an instance of the Debug class
```
import debugger

debug = debugger.Debug()
```

### Code examples

<table>
<tr>
<td>Code</td>
<td>Output</td>
</tr>

<tr>
<td>

```python
import debugger

variable_1 = 0
variable_2 = "Hello, world!"

debug = debugger.Debug()
debug.addVariables(["variable_1","variable_2"])
debug.maxLenOfLogs = 10 # Defines the number of maximum values in the history of variables
debug.logEqualsValues = False # Defines if a value should be added to the history if it has not been modified since the last refresh.

for i in range(100000):
    variable_1 += 1
    debug.update()
debug.show()
```

</td>
<td>

```
########## variable_1 ##########
 - 99991
 - 99992
 - 99993
 - 99994
 - 99995
 - 99996
 - 99997
 - 99998
 - 99999
 - 100000

########## variable_2 ##########
 - Hello, world!

```

</td>
</tr>
</table>

## API Reference

### Settings variables :

- ```maxLenOfLogs (initial: 10)``` The max lengh of the history for each variables
- ```logEqualsValues (initial: True)``` Defines if a value should be added to the history if it has not been modified since the last refresh.
- ```oneLineValues (initial: False)``` Defines whether the result should be displayed as a tab, in a single line


### Functions :

- ```addVariables(list)``` Add a list of variables to debug them
- ```addVar(str)``` Add a single variable to add to the list of variables to debug
- ```removeVar(str)``` Remove a single variable from the list of variables to debug
- ```update()``` Update the history of all the variables
- ```show()``` Show the result of the debbuging session (show the history of all the variables)