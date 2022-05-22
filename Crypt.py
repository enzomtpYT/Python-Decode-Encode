import os, base64
from cryptography.fernet import Fernet

#ask user for password
password = input("Enter password: ")
if len(password) >= 32:
    print("Password must be 32 characters or less")
    exit()
elif len(password) < 32:
    passwordmod = password + "=" * (32 - len(password))
    print(passwordmod)
key = base64.urlsafe_b64encode(passwordmod.encode("utf-8"))
files = []

#list all files in the current directory
for file in os.listdir():
    if file == "Crypt.py" or file == "key.key":
        continue
    if os.path.isfile(file):
        files.append(file)

def encode(key, files):
    print(key)
    for file in files:
        with open(file, "rb") as f:
            data = f.read()
        data_encrypted = Fernet(key).encrypt(data)
        with open(file, "wb") as f:
            f.write(data_encrypted)

def decode(key, files):
    for file in files:
        with open(file, "rb") as f:
            data = f.read()
        data_decrypted = Fernet(key).decrypt(data)
        with open(file, "wb") as f:
            f.write(data_decrypted)

#ask for encode or decode
choice = str(input("Do you want to encode or decode? "))
if choice == "encode":
    encode(key, files)
elif choice == "decode":
    decode(key, files)