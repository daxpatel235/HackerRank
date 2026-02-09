import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # 1. Read N (the size of the array)
    n = int(input().strip())
# split() cuts the string by spaces
# map(int, ...) converts those string pieces into integers
# list(...) gathers them into a formal list
    arr = list(map(int, input().rstrip().split()))
    # arr[::-1] creates a reversed copy
# * (the asterisk) unpacks the list, printing elements separated by spaces
    print(*(arr[::-1]))
