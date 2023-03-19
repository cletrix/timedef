# Timedef

This package provides a decorator function `timedef` that can be used to measure the execution time of other functions in Python.

## Installation

You can install this package using pip:

```pip install timedef```


## Usage

To use the `timedef` decorator, simply import it from the package and apply it to the function you want to measure:

```python
from timedef import timedef

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
@timedef
def show(value: int):
    result = fibonacci(value)
    print(f"result fibonacci:{result}")

show(1)
show(10)
show(20)

```
When you run my_function, the decorator will print the execution time in seconds to the console.

License
This package is licensed under the MIT License 
