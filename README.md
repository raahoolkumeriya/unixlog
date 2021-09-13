A simple unix style logging in color format. Light weight library for Color formating.

## Features
- Include warning, error, info, debug, success, trace
- Light weight import
- unix style format

## Installation
```pip install unixlog```

## Examples 

```>>> from unixlog import error, warning, info, success, trace, debug

>>> print(error("This error text"))

[  ERROR  ] This error text

>>> error("This error text")

'\x1b[91m[  ERROR  ] This error text\x1b[0m'```
