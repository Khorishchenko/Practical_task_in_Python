# def main():
#     print("Hello, world!")

# if __name__ == '__main__':
#     main()




import math
import os
import random
import re
import sys

# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 1:
        print('Weird')
    elif n % 2 == 0 and 2 <= n <= 5:
        print('Not Weird')
    elif n % 2 == 0 and 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')
