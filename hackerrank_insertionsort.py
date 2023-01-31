#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    key = arr[-1]
    for i in range(n - 2, -2, -1):
        if key < arr[i] and i >= 0:
            arr[i + 1] = arr[i]
            ans = [str(ele) for ele in arr]
            print(' '.join(ans))
        else:
            arr[i + 1] = key
            ans = [str(ele) for ele in arr]
            print(' '.join(ans))
            break


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
