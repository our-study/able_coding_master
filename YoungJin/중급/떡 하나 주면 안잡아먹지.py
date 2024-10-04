import sys

a = int(sys.stdin.readline())
dic = dict()

for v in range(1, a + 1):
    v = str(v)
    v = list(v)
    for vv in v:
        if dic.get(vv) == None:
            dic[vv] = 1
        else:
            dic[vv] = dic[vv] + 1

keys = list(dic.keys())
keys.sort()
for key in keys:
    print(dic[key], end=" ")



