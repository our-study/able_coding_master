import math

# 최대공약수를 구하는 함수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 모든 약수를 구하는 함수
def find_divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

# 입력 받기
n = int(input())
numbers = [int(input()) for _ in range(n)]

# 1. 수들을 정렬
numbers.sort()

# 2. 수들 간의 차이의 최대공약수 구하기
g = numbers[1] - numbers[0]
for i in range(2, n):
    g = gcd(g, numbers[i] - numbers[i - 1])

# 3. 최대공약수의 약수 찾기
result = find_divisors(g)

# 4. 결과 출력
print(" ".join(map(str, result)))
