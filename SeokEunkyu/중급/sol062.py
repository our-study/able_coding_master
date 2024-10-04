from collections import deque 
 
def min_rotations(N, M, targets): 
    # 초기 덱 설정: 1부터 N까지 
    candy_deque = deque(range(1, N + 1)) 
    total_rotations = 0 
 
    for target in targets: 
        # 현재 타겟의 인덱스 찾기 
        idx = candy_deque.index(target) 
        # 덱의 길이 
        length = len(candy_deque) 
        # 왼쪽으로 회전하는 경우 
        left_rotations = idx 
        # 오른쪽으로 회전하는 경우 
        right_rotations = length - idx 
        # 최소 회전 횟수 선택 
        if left_rotations <= right_rotations: 
            total_rotations += left_rotations 
            candy_deque.rotate(-left_rotations)  # 왼쪽 회전 
        else: 
            total_rotations += right_rotations 
            candy_deque.rotate(right_rotations)   # 오른쪽 회전 
        # 타겟 사탕 제거 
        candy_deque.popleft() 
     
    return total_rotations 
 
# 입력 받기 
if __name__ == \"__main__\": 
    import sys 
    input = sys.stdin.read 
    data = input().split() 
     
    N = int(data[0]) 
    M = int(data[1]) 
    targets = list(map(int, data[2:2+M])) 
     
    result = min_rotations(N, M, targets) 
    print(result) 
