# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:40:24 2021

@author: Reza
"""

from functools import wraps
from time import time

def measure_time(func):
    print("-----------------------------------------------------------------")
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"\nTotal execution time: {end_ if end_ > 0 else 0} ms \n \n")
    return _time_it



