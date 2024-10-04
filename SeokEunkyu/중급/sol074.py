def possible_passwords(N, times): 
    MOD = 1000000007 
     
    # 버튼 위치 매핑 (전역 변수로 정의) 
    positions = { 
        1: (0, 0), 2: (0, 1), 3: (0, 2), 
        4: (1, 0), 5: (1, 1), 6: (1, 2), 
        7: (2, 0), 8: (2, 1), 9: (2, 2) 
    } 
     
    # 시간에 따른 가능한 버튼 수 계산 
    dp = [[0] * 10 for _ in range(N)] 
     
    # 첫 번째 버튼: 1-9 모두 가능 
    for i in range(1, 10): 
        dp[0][i] = 1 
     
    # 시간에 따른 버튼 가능성 계산 
    for i in range(1, N): 
        time = times[i - 1] 
        for j in range(1, 10):  # 현재 버튼 
            if dp[i-1][j] > 0:  # 이전 버튼에서 올 수 있는 경우 
                for k in range(1, 10):  # 다음 버튼 
                    if can_press(j, k, time, positions): 
                        dp[i][k] = (dp[i][k] + dp[i-1][j]) % MOD 
     
    # 최종 가능한 경우의 수 계산 
    total_count = sum(dp[N-1]) % MOD 
    return total_count 
 
def can_press(button1, button2, time, positions): 
    pos1 = positions[button1] 
    pos2 = positions[button2] 
    distance = max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1])) 
     
    if button1 == button2: 
        return time == 1 
    elif distance == 1: 
        return time == 2 
    else: 
        return time == 3 
 
# 입력 처리 
N = int(input()) 
times = list(map(int, input().split())) 
 
# 함수 호출 및 출력 
print(possible_passwords(N, times)) 
