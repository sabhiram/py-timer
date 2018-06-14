# py-timer

A super simple way to measure code execution time in python.

## Install

```sh
sudo python setup.py install
```

## Usage

```python
import time
from pytimer import PyTimer

if __name__ == "__main__":
    with PyTimer("Task A"):
        time.sleep(1)
```

This will generate something like:
```
Task A took 1.003875
```

The timer can also be disabled by setting the `enable` flag in the constructor to `False` like so:

```python
with PyTimer("Task A", enabled=False):
    time.sleep(1)
```

Feel free to include this as a class in your script / application, or install this using the above install method.

## Example

See file: `example/example.py`.
