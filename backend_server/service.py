"""Backend Server"""
import os
import sys
import operations

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

# import utils packages
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

import mongodb_client #pylint: disable = import-error, wrong-import-position

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

def add(num1, num2):
    """Test Method"""
    print("Add is called with %d and %d " %(num1, num2))
    return num1 + num2

def get_one_news():
    """Get News Method"""
    print("get_one_news is called.")
    return operations.getOneNews()

RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(get_one_news, 'get_one_news')

print("Starting RPC server")

RPC_SERVER.serve_forever()
