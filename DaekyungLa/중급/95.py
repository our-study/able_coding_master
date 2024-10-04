import sys
from itertools import permutations

data = sys.stdin.read().strip().split('\n')

def is_valid_puzzle(words):
    for i in range(3):
        for j in range(3):
            if words[i][j] != words[j+3][i]:
                return False
    return True

for perm in sorted(permutations(data, 6)):
    if is_valid_puzzle(perm):
        for i in range(3):
            print(perm[i])
        break
