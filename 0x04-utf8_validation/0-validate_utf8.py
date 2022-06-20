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
    numb_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for number in data:
        mask = 1 << 7
        if numb_bytes == 0:
            while mask & number:
                numb_bytes += 1
                mask1 = mask1 >> 1
            if numb_bytes == 0:
                continue
            if numb_bytes == 1 or numb_bytes > 4:
                return False
        else:
            if not (number & mask1 and not (number & mask2)):
                return False
        numb_bytes -= 1
    return numb_bytes == 0
