import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())    # read the number
binary = bin(n)[2:]   # convert to binary and remove '0b'
count = 0           #Count consecutive 1s
max_count = 0       #Count consecutive 1s

for bit in binary:    #Loops through each character in the binary string
    if bit == '1':    # if this true, We are inside a streak of 1s
        count += 1    #Increase current streak length
        max_count = max(max_count, count)    # comapre previous longest streak(max_count) and current streak(count)
    else:
        count = 0     #The streak is broken , Reset current count back to 0

print(max_count)
