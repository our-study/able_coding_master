import sys
from itertools import product

n, k = map(int, sys.stdin.readline().split())
chars = sorted(sys.stdin.readline().strip())  

for combination in product(chars, repeat=k):
    print(''.join(combination))
