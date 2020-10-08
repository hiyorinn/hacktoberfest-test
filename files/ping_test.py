from argparse import ArgumentParser
from multiprocessing import cpu_count
from multiprocessing import Pool
from functools import wraps
from itertools import product

import os
import re

def thread(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pool = Pool(cpu_count() * 10)
        host = params.host
        return pool.map(func, host)
    return wrapper

@thread
def ping(host):
    print os.popen('fping -t{} {}'.format(params.timeout, host)).read(),

if __name__ == "__main__":
    parser = ArgumentParser(description='Multithread Ping Test Connection')
    parser.add_argument('host', nargs='+', metavar='host', type=str, help='Host')
    parser.add_argument('--range', '-r', help='Range mode', action='store_true')
    parser.add_argument('--timeout', '-t', metavar='timeout', type=str, help='Timeout in milisecond', default='100')
    
    global params
    params = parser.parse_args()

    ping()