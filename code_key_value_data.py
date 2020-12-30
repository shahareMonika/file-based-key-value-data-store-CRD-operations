import threading
from threading import *
import time

# 'dict' is the dictionary in which we store data
dict = {}

# for create operation
# use syntax "create(key_name,value,timeout_value)"
# timeout is optional you can continue by passing two arguments without timeout

def create(key, value, timeout=0):
    if key in dict:
        print("error: this key already exists")  # show the error message
    else:
        if (key.isalpha()):
            if len(dict) < (1024 * 1024 * 1024) and value <= (16 * 1024 * 1024):  # constraints for file size less than 1GB and Json_object value less than 16KB
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time() + timeout]
                if len(key) <= 32:  # constraints for input key_name capped at 32characters
                    dict[key] = l
            else:
                print("error: Memory limit exceeded! ")  # show the error message
        else:
            print(
                "error: Invalind key_name! key_name must contain only alphabets and no special characters or numbers")  # show error message


# for read operation
# use syntax "read(key_name)"
def read(key):
    if key not in dict:
        print("error:Please enter a valid key! given key does not exist in database. ")  #show the error message
    else:
        b = dict[key]
        if b[1] != 0:
            if time.time() < b[1]:  # comparing the present time with expiry time
                str_i = str(key) + ":" + str(
                    b[0])  # to return the value in the format of Json_Object i.e.,"key_name:value"
                return str_i
            else:
                print("error: time-to-live of", key, "has expired")  # show the error message
        else:
            str_i = str(key) + ":" + str(b[0])
            return str_i


# for delete operation
# use syntax "delete(key_name)"

def delete(key):
    if key not in dict:
        print("error:Please enter a valid key! given key does not exist in database. ")  # error message
    else:
        b = dict[key]
        if b[1] != 0:
            if time.time() < b[1]:  # comparing the current time with expiry time
                del dict[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of", key, "has expired")  # error message
        else:
            del dict[key]
            print("key is successfully deleted")


# I did additional operation of modify in order to change the value of key before its expiry time if provided
# for modify operation
# use syntax "modify(key_name,new_value)"

def modify(key, value):
    b = dict[key]
    if b[1] != 0:
        if time.time() < b[1]:
            if key not in dict:
                print("error: given key does not exist in database. Please enter a valid key")  # show the error message
            else:
                list = []
                list.append(value)
                list.append(b[1])
                dict[key] = list
        else:
            print("error: time-to-live of", key, "has expired")  # show the error message
    else:
        if key not in dict:
            print("error:Please enter a valid key! given key does not exist in database. ")  # show the error message
        else:
            list = []
            list.append(value)
            list.append(b[1])
            dict[key] = list