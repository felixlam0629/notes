import numpy as np
import pandas as pd
from pprint import pprint
import requests
import time
import threading

signal_list = [0, 0, 0, -1, -2, 3]

# Get the second last element using negative indexing
second_last_element = signal_list[-2]
print(second_last_element)
exit()

number = 0.324072
rounded_number = round(number, 2)  # Round to 4 significant figures

print(rounded_number)
exit()

locker_activated = False

def activate_locker():
    global locker_activated

    while True:
        print("a")
        break

    print("b")

    if locker_activated == False:
        print("Locker deactivated")

        locker_activated = True

        print("Locker activated")

        timer = threading.Timer(5, deactivate_locker)
        timer.start()
        print("a")

        """
        start_time = time.time()
        now_time   = time.time()

        while (now_time - start_time < 10) == True:
            now_time = time.time()
            print("Locker waiting to deactivate")

        deactivate_locker()
        """

def deactivate_locker():
    global locker_activated

    if locker_activated == True:
        print("Locker ready to deactivate")

        locker_activated = False

        print("Locker deactivated")

# Test the locker functionality
activate_locker()