import hashlib
#import base64
#import binascii
#import json
import time
import sys
from datetime import datetime
from datetime import date



# set up logger
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('----------')
now = datetime.now()
t=2
print('Running System')
countdown(int(t))
current_time = now.strftime("%d/%m/%Y %H:%M:%S")
print("\n System started running at = \n", current_time)
f = open("System_entry.txt", "a")
f.write(current_time)
f.close()


sys.tracebacklimit = 0

def signup():
    print ("please request assistance from administrator")
    countdown(int(t))


"""
def signup():
    email = input("Enter email address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
             f.write(email + "\n")
             f.write(hash1)
        f.close()
        print("You have registered successfully!")
    else:
        print("Password is not same as above! \n")
"""
def login():
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
         print("Logged in Successfully!")
         f = open("Login_entry.txt", "a")
         f.write(current_time)
         f.close()
         user_logined()

    else:
         print("Login failed! \n")


def user_logined():
    print("************** \n")
    import Crypto_Assignment.py
    execfile("Crypto_Assignment.py")




while 1:
    try:
        print("********** Login System **********")
        print("1.Signup")
        print("2.Login")
        print("3.Exit")
        ch =int(input("Enter your choice: "))
        if ch == 1:
            signup()
        elif ch == 2:
            login()
        elif ch == 3:
            break
    except ValueError:
        pass
    else:
        print("Returning back to login module!")


