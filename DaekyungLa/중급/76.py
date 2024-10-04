import sys
from itertools import permutations

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())

relationships = {
    'good': set(),
    'bad': set()
}

def calculate_score(arrangement, relationships):
    score = 0
    for i in range(len(arrangement) // 2):
        a, b = arrangement[2 * i], arrangement[2 * i + 1]
        if (a, b) in relationships['good']:
            score += 1
        elif (a, b) in relationships['bad']:
            score -= 1
    return score
    
for _ in range(K):
    a, b, c = map(int, input().strip().split())
    if a == 1:
        relationships['good'].add((b, c))
        relationships['good'].add((c, b))  
    elif a == 2:
        relationships['bad'].add((b, c))
        relationships['bad'].add((c, b)) 

students = list(range(1, 2 * N + 1))
max_score = float('-inf')

for arrangement in permutations(students):
    current_score = calculate_score(arrangement, relationships)
    max_score = max(max_score, current_score)

print(max_score)
