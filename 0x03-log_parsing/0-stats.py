#!/usr/bin/python3
'''
Write a script that reads stdin line by line and computes metrics:

- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status
code> <file size> (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
 - Total file size: File size: <total size>
 - where <total size> is the sum of all previous <file size> (see input format
 above)
 - Number of lines by status code:
  - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
  - if a status code doesn't appear or is not an integer, don't print anything
  for this status code
  - format: <status code>: <number>
  - status codes should be printed in ascending order
'''


import re
import sys


lines_counter = 1
total_size = 0
status_counter = {'200': 0, '301': 0, '400': 0,
                  '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
input_format = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}.+')
for line in sys.stdin:
    if input_format.match(line.strip()) is None:
        print('didnt match the regex')
        break
    line_array = line.split(' ')
    # print(line_array)
    total_size += int(line_array[-1])
    # print(total_size)
    for key in status_counter.keys():
        if key == line_array[-2] and isinstance(status_counter[key], int):
            status_counter[key] += 1
    # print(lines_counter)
    if lines_counter % 10 == 0:
        print(f'File size: {total_size}')
        for key, value in status_counter.items():
            if value:
                print(f'{key}: {value}')
        for key in status_counter.keys():
            status_counter[key] = 0
    lines_counter += 1
