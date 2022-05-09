#!/usr/bin/python3
"""
The script gets a password string from command prompt and prints sha512 hash with salt of 16 characters.
This could be useful if you want to edit your password in /etc/shadows without passwd execution.
"""

import crypt
import string
import random
import getpass

HASH = crypt.crypt(getpass.getpass(), '$6${}$'.format(''.join(random.sample(string.ascii_letters + string.digits, 16))))
print(HASH)
