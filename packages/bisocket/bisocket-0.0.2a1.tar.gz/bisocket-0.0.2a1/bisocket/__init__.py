# Import modules from subpackages
try:
    from .cython import c_main as main 
except:
    from . import main

try:
    from .cython.c_main import Client, Server, Message, ServerRequest, server_handler_example
except:
    from .main import Client, Server, Message, ServerRequest, server_handler_example

# Define the public API
__all__ = [
    'main',
]
