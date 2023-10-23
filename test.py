import calendar
import datetime
import pandas as pd
import numpy as np
import os
import pandas as pd
from pprint import pprint
import requests
import time

import functools

from multiprocessing import Process
from threading import Thread
from queue import Queue

"""
def worker(q, lock):
    while True:
        value = q.get()

        # processing...
        print(f" in {curr}")
q = Queue()
num_threads = 2

for i in range(num_threads):
    thread = Thread(target = )
    thread.daemon = True
    thread.start()

q.task_done()
q.join()
"""

"""
def firstn(n_loop):
    number_list = []
    number       = 0

    while number < n_loop:
        number_list.append(number)
        number += 1

    return number_list

def firstn_generator(n_loop): # more memory efficient as it does not save all the numbers in the num_list
    number = 0

    while number < n_loop:
        yield number
        number += 1

list_a = firstn(10)
print(list_a)

list_b = firstn_generator(10)
print(list_b)

def fibonacci(limit):
    # 0, 1, 1, 2, 3, 5, 8, 13, ...
    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a + b

fib_list = fibonacci(30)

for i in fib_list:
    print(i)

mygenerator      = {i for i in range(10) if i % 2 == 0}
mygenerator_list = [i for i in range(10) if i % 2 == 0]

for i in mygenerator:
    print(i)

print(mygenerator_list)
"""
"""
def repeat(num_times):
    def decorat_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)

            return result
        return wrapper
    return decorat_repeat

@repeat(num_times = 10)
def greet(name):
    print(f'Hello {name}')

greet("Alex")

print("*****")



def start_end_decorator(function):

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print('Start')
        result = function(*args, **kwargs)
        print('End')

        return result

    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

# print_name = start_end_decorator(print_name)
# print_name()

@start_end_decorator
def add_5(x):
    return x + 5

result = add_5(5)
print(result)

print(help(add_5))
print(add_5.__name__)
"""
"""
import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

def encode_user(object):
    if isinstance(object, User): # whether an object is an instance of a class
        return {"name": object.name, "age": object.age, object.__class__.__name__: True}

    else:
        raise TypeError("Object of type User is not JSON serializable")



from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, User):  # whether an object is an instance of a class
            return {"name": object.name, "age": object.age, object.__class__.__name__: True}

        return JSONEncoder.default(self, object)

user       = User("Max" ,27)
user_dict  = encode_user(user)
user_json1 = json.dumps(user_dict)
print(user_json1)

user_json2 = json.dumps(user, cls = UserEncoder)
print(user_json2)

user_json3 = UserEncoder().encode(user)
print(user_json3)

def decode_user(dict):
    if User.__name__ in dict:
        return User(name = dict['name'], age = dict['age'])
    return dict

user_chg_back1 = json.loads(user_json3)
print(user_chg_back1)

user_chg_back2 = json.loads(user_json3, object_hook = decode_user)
print(user_chg_back2.name)
print(user_chg_back2)
print(type(user_chg_back2))
"""

"""
import json
# Serialization/ encoding: python -> json
person      = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
person_json = json.dumps(person, indent = 4, sort_keys = True)

with open('person.json', 'w') as file:
    json.dump(person, file, indent = 4)

# Deserialization/ decoding: json -> python
person_chg = json.loads(person_json) # with s
print(person_chg)

with open('person.json', 'r') as file:
    person_chg = json.load(file) # without s
    print(person_chg)
"""
"""
import logging

logger = logging.getLogger(__name__)

stream_h = logging.StreamHandler()
file_h   = logging.FileHandler('file.log')

stream_h.setLevel(logging.WARNING)
file_h.setLevel((logging.ERROR))

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler((file_h))

logger.warning('This is a warning')
logger.error('This is an error')

logger.propagate
logger.info('hello from helper')

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = '%m/%d/%Y %H:%M:%S')

logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')
"""