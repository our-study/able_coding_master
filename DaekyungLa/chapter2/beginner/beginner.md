# 초급

# Num[1~10]

### 1. 채터링

```python

```

### 2. **기차와 파리**

```python
import sys 

# Input
distance, v_train, v_fly = map(int,sys.stdin.readline().split())

# Total time 
time_flying = distance/(v_train*2)

# Distance = Time * velocity
answer = time_flying * v_fly

print(int(answer))
```

### 3. 팬그램

```python
import sys 
from collections import Counter

str0 = sys.stdin.readline().strip()

# 대,소문자 통일
str2 = str0.lower()

# 글자 수 확인
cnt = len(Counter(str2).keys())

if cnt == 26:
    print("YES")
else:
    print("NO")
```

### 8.톱니바퀴

```python
import sys 

a,b,c= map(int,sys.stdin.readline().split())

rotation = 0

# saw_count x rotation = C
rotation +=(c*10)//a

# remain_rotation
if (c*10)%a !=0:
    rotation+=1
print(rotation)
```

### 9. 전화번호 입

```python
import sys 

a,b,c= map(int,sys.stdin.readline().split())

rotation = 0

# saw_count x rotation = C
rotation +=(c*10)//a

# remain_rotation
if (c*10)%a !=0:
    rotation+=1
print(rotation)
```

# Num[11~20]

### 1. 채터링

```python

```