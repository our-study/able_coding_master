# 중급

# Num[21~30]

### 21. 좋은 배열

```python
import sys 

a = int(sys.stdin.readline()) 

# 1.ist로 풀기
b = list(map(int,sys.stdin.readline().split()))
num_odd=[b[0]] 
num_even=[b[1]]

# 옳은 배열 판별(1:bad, 0:good)
cnt=0
for i in range(2,len(b)): #a*2
    # 홀수 (index 0,2,4,,,)
    if i%2==0:
        if num_odd[0] == b[i]: 
            print("NO")
            cnt+=1
            break
        else:
            num_odd[0]=b[i]
    # 짝수 (index 1,3,5,,,)
    else:
        if num_even[0] == b[i]: 
            print("NO")
            cnt+=1
            break
        else:
            num_even[0]=b[i]
            
if cnt==0:
    print("YES")

```

# Num[31~20]

### 35. 싱크홀

```python
import sys 

n, k = map(int,sys.stdin.readline().split())
hole_spot = sorted(list(map(int,sys.stdin.readline().split())))

cnt = 0
start =  0
end = 0

for i in hole_spot:
  if start==0:
    start+=1
  else:
    end = i
    if end-start == k:
      start, end = 0,0
      cnt+=1
    elif end-start>k:
      start=i
      end=0
      cnt+=1
      # print(i, start, end, cnt)
      
# 마지막 구멍 남아 있을 경우
if start !=0:
  cnt+=1
print(cnt)
```

### 36. 블로그

```python
import sys 

n, k = map(int,sys.stdin.readline().split())
visit_history = list(map(int,sys.stdin.readline().split()))

sum_list = []

# k개만큼 누적합 구하기 
for i in range(n):
  sum_visit = 0
  for j in visit_history[i:i+k]:
    sum_visit +=j
  sum_list.append(sum_visit)
#   print(f'i:{j} ,sum_visit:{sum_visit} sum_visit:{sum_visit}')
print(sum_list.index(max(sum_list))+1)
```

### 37. 알람 맞추기

```python
import sys 

time = list(map(int,sys.stdin.readline().strip().split(":")))
n = int(sys.stdin.readline().strip())

# 등차수열의 합/ if n=5 -> 1~4의합
hours = 0
minutes = (n*(n-1))//2

# Calculate N time
if minutes >=60:
  hours = minutes//60
  minutes = minutes % 60

time[0]+= hours
time[1]+= minutes

#  시간 단위 minute to hour&minute
if time[1]>=60:
  time[1]=time[1]%60
  time[0]+=1
if time[0]>=24:
  time[0]=time[0]%24

# 출력형태 조절
if time[1]==0:
  time[1]="00"
if len(str(time[0]))==1:
  time[0]="0"+f'{time[0]}'
  
print(f'{time[0]}:{time[1]}')
```

# Num[61~70]

### 65. 자연수의 신

```python
import sys 

n, k = map(int,sys.stdin.readline().split())

half = (n+1)//2

# odd (1~6)
if k <= half:
    print(2*k-1)
    
# even (7~11 or 12)
else:
    print((k-half)*2)
```