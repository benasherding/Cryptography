# -*- coding: utf-8 -*-
"""

@edited : Ding hong
"""
# Using fernet to encrypt and decrypt text, and put them in text file
# decrypting them if required
import base64
import hashlib
import os
import time
import sys
from datetime import datetime
from cryptography.fernet import Fernet

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('----------')
now = datetime.now()

sys.tracebacklimit = 0


#Generate the key
#key = Fernet.generate_key()
def encrypt():
    key = base64.urlsafe_b64encode(os.urandom(32))# Keep this secret!
    #print(key)
    f = Fernet(key)
   #print(f)
    idit = input("Enter message to encrypt: ")
    #Message= "abcdefgh"
    print(idit)
    token = f.encrypt(idit.encode())
    print(token)
    hash1 = hashlib.md5(token).hexdigest()
    #print("this is hash cipher text" + hash1)
   # print("this is ciphertext"+ token )
    hash2 = hashlib.md5(hash1.encode()).hexdigest()
    print(hash2)
    some_bytes = token
    binary_file = open("my_bfile.txt", "wb") #ciphertext
    binary_file.write(some_bytes)
    binary_file.close()

    some_bytess = key
    binary_file = open("my_b1file.txt", "wb")
    binary_file.write(some_bytess)
    binary_file.close()

    idit = input("create an unused filename for secret item ")

    try:
    #change textfile to new name
        old_name = r"C:\Users\user\Desktop\New folder (2)\my_bfile.txt"
        new_name = r"C:\Users\user\Desktop\New folder (2)\_" + idit +"_"+ hash1 + ".txt"
        os.rename(old_name, new_name)

    except ValueError:
        print("your filename isn't unique, try again!")
        pass



    print("your file is saved in/as " + new_name )
    idita1 = input("type in first unique key/id to retrieve your plain text ")
    hash3 = hashlib.md5(idita1.encode()).hexdigest()
    hashed = hash3 + hash1
    hasheroo = hashlib.md5(hashed.encode()).hexdigest()
    print(hasheroo)

    #file_existed = os.path.exists("__" + "_" + hash3 + ".txt")
    #print(file_existed)

    #print("please type in a new unique key" )

    file_exists = os.path.exists("__" + "_" + hasheroo + ".txt")
    #print(file_exists)
    print("Pending storing...")
    t = 2
    print('Updating audit details...')
    countdown(int(t))
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n Secret key commited at= \n", current_time, "\n file existed", file_exists)
    f = open("System_entry.txt", "a")
    f.write(current_time + str(file_exists))
    f.close()



    old_name = r"C:\Users\user\Desktop\New folder (2)\my_b1file.txt"
    new_name = r"C:\Users\user\Desktop\New folder (2)\__" +"_"+ hasheroo + ".txt"
    os.rename(old_name, new_name)



    file_exists = os.path.exists("__" +"_"+ hasheroo + ".txt")
    #print(file_exists)

    print("Pending storing...")
    t = 3
    print('Updating audit details...')
    countdown(int(t))
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n Secret key commited at= \n", current_time,"\n file stored", + file_exists)
    f = open("System_entry.txt", "a")
    f.write(current_time + str(file_exists))
    f.close()






    #print ("your message is crypted")
    #print ("your message is being decoded")
    #print(f.decrypt(token))
   # b = (f.decrypt(token))
   # c = b.decode('ASCII')
   # print(c)






#test
#receive starts here
#'...'

#print ("your message is crypted")
#print ("your message is being decoded")
#print(f.decrypt(token))
#b = (f.decrypt(token))
#c = b.decode('ASCII') #byte decrypted text to string
#print(c)

def decrypto():
    key = base64.urlsafe_b64encode(os.urandom(32))
    f = Fernet(key)
    #print(f)
    print("showing files...")
    arr = os.listdir("C:\\Users\\user\\Desktop\\New folder (2)")
    for entry in arr:
        print(entry)

    try:

    # All files and directories ending with .txt and that don't begin with a dot:

        iditde = input("Enter name of  file to decrypt it's content: ")



        #change textfile to new name
        #old_name = r"C:\Users\user\Desktop\New folder (2)\my_bfile.txt"
        #read1 = r"C:\Users\user\Desktop\New folder (2)\\"+ iditde
        file = open(iditde, "rb")

    except (FileNotFoundError, UnboundLocalError):
        pass
    else:
        print("Back to page")
    try:

        hidden = file.read()
    except (FileNotFoundError, UnboundLocalError):
      pass
    try:
        token = hidden
    except (FileNotFoundError, UnboundLocalError):
      pass
    #base64_token = hidden.decode('ascii')
    #print(base64_token)

    #file.close()

    try:

        iditas = input("password to open secret item")


        hash33 = hashlib.md5(iditas.encode()).hexdigest()#hash the password
        hashedtoken = hashlib.md5(hidden).hexdigest() #hash the cipher text
        verify = hash33 + hashedtoken #hashed password + #hashed cipher text
        verified = hashlib.md5(verify.encode()).hexdigest()  #hashed  password + #hashed cipher text







        #read2 = r"C:\Users\user\Desktop\New folder (2)\
        file1 = open("__" +"_"+ verified + ".txt","rb")  #the file name of the key  is the hashed password and hashed cipher text
    except (FileNotFoundError, UnboundLocalError): #if the hashed of the combined hashed password and hashed ciphertext not found? then cant find the encryption/decryption key
        pass

    else:
        print("Back to page")
    try:
        keyz = file1.read()
        base64_key = keyz.decode('ascii')
        print(base64_key)
        f = base64_key
        print(f)
        #token = base64_token
        #print(token)
        f = Fernet(keyz)
    except (FileNotFoundError, UnboundLocalError):
      pass
    try:
        try:
            print(f.decrypt(token))
            b = (f.decrypt(token))
            decoded_key = b.decode('ASCII')
            print(" your decrypted code is : " + decoded_key)
        except (cryptography.fernet.InvalidToken, TypeError):
            pass
    except (FileNotFoundError, UnboundLocalError, NameError):
      pass







    #file1.close()
    #print(read2)
   # this_decryptionkey = read2
    # "__" +"_"+ hash33 + ".txt"

   # this_ciphertext = read1





   # file = open(this_decryptionkey, "rb")
   # eat = file.read(1)
   # fresh_decryptionkey = eat

   #  f = fresh_decryptionkey



    #print(f.decrypt(token))



    #c = newbie # .decode('ASCII')

    #print(c)







def main():
    while 1:
        try:
            print("********** Login System **********")
            print("1.retrieve file index")
            print("2.store new file")
            print("3.Exit application")
            ah = int(input("Enter your choice: "))
            if ah == 1:
                decrypto()
            elif ah == 2:
                encrypt()
            elif ah == 3:
                quit()
        except ValueError:
            pass
        else:
            print("Back to page")

main()
#old_name = r"C:\Users\user\Desktop\New folder (2)\my_b1file.txt"
#new_name = r"C:\Users\user\Desktop\New folder (2)\my_bfile" + idit + hash3 + ".txt"
#os.rename(old_name, new_name)










#'A really secret message. Not for prying eyes.'

#some_bytes = token

# Open file in binary write mode
#binary_file = open("my_bfile.txt", "wb")

# Write bytes to file
#binary_file.write(some_bytes)

# Close file
#binary_file.close()



