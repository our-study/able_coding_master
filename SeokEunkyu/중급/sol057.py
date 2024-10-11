import sys

def calculate_additional_at_bats(X, Y):
    # 현재 타율 계산
    current_average = Y * 10 // X  # 현재 타율의 할, 푼 부분만 사용
    additional_at_bats = 0
    
    # 최대 1,000,000,000번의 타석에 대해 반복
    while additional_at_bats <= 1000000000:
        new_at_bats = X + additional_at_bats
        new_hits = Y + additional_at_bats
        
        # 새로운 타율 계산
        new_average = new_hits * 10 // new_at_bats
        
        # 타율이 오르면 결과를 반환
        if new_average > current_average:
            return additional_at_bats
        
        additional_at_bats += 1

    # 타율이 오르지 않으면 -1 반환
    return -1

# 입력 받기
input_data = sys.stdin.readline().strip()
X, Y = map(int, input_data.split())

# 결과 출력
result = calculate_additional_at_bats(X, Y)
print(result)
