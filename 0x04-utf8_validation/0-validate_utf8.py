#!/usr/bin/python3

'''
Write a method that determines if a given data set represents a valid UTF-8
encoding.

- Prototype: def validUTF8(data)
- Return: True if data is a valid UTF-8 encoding, else return False
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle
the 8 least significant bits of each integer
'''


def validUTF8(data):
    '''
    Validates if evey integer in data array is valid UTF-8 character
    '''
    if not data:
        return False
    for elm in data:
        if not isinstance(elm, int):
            return False
        if elm < 0 or elm > 255:
            return False
    return True
