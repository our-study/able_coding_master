import sys

X, Y = map(int, input().strip().split())

current_avg = Y * 100 // X

required_at_bats = -1

left, right = 0, 1000000000

while left <= right:
    mid = (left + right) // 2
    new_avg = (Y + mid) * 100 // (X + mid)
    
    if new_avg > current_avg:
        required_at_bats = mid
        right = mid - 1  
    else:
        left = mid + 1  

print(required_at_bats)
