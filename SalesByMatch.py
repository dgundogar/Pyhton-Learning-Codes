import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    x = 0
    counter = []
    total = 0
    for i in range(0,n):
        counter.append(1)
    
    for i in range(n-1):
        if ar[i] != -1:
            for j in range(i+1,n):
                if ar[i] == ar[j]:
                    counter[x] += 1
                    ar[j] = -1
            x+=1                
    for i in range(n):
        total += counter[i] // 2
    return total
                       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()