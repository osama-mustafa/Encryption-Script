#! /usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = os.listdir()
targets = []


# Get encryption key
key = 'key.key'
with (open(key, 'rb')) as the_key:
    encryption_key = the_key.read()


# Get all files from the current directory
for file in files:

    file_extension = os.path.splitext(file)

    # Execlude Python scripts & key from decryption
    if file.lower().endswith(('.py', '.key')):
        continue

    # Execlude directories from decryption
    if os.path.isdir(os.path.abspath(file)):
        continue
    
    targets.append(file)

    with open(file, 'rb') as the_file:
        file_content = the_file.read()

    decrypted_content = Fernet(encryption_key).decrypt(file_content)
    with open(file, 'wb') as the_file:
        the_file.write(decrypted_content)

print('Congratulations ... Your Files Has Been Decrypted Successfully')






    


    
