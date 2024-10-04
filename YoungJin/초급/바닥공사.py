import sys

trial = sys.stdin.readline().strip()
trial = int(trial)
li = []
for _ in range(trial):
    alpha = sys.stdin.readline().strip()
    if alpha not in li:
        li.append(alpha)

li.sort(key=lambda x: (len(x), x))

for charr in li:
    print(charr)