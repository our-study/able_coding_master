import sys

N = int(sys.stdin.readline().strip())
x, y = map(int, sys.stdin.readline().strip().split())

min_time = float('inf')
best_x = None

for candidate_x in range(-100, 101):
    entry_time = ((candidate_x - 0) ** 2 + (N - 0) ** 2) ** 0.5 / 10
    swim_time = ((candidate_x - x) ** 2 + (0 - y) ** 2) ** 0.5 / 5
    total_time = entry_time + swim_time

    if total_time < min_time:
        min_time = total_time
        best_x = candidate_x

print(best_x)
