import math 
 
def find_best_entry_point(N, x_p, y_p): 
    min_time = float('inf') 
    best_x = 0 
     
    # 모든 가능한 입수 위치 x_e에 대해 시간을 계산합니다. 
    for x_e in range(-100, 101): 
        # 육지에서 입수 지점까지의 시간 
        land_time = math.sqrt((x_e - 0) ** 2 + (N - 0) ** 2) / 10 
        # 입수 지점에서 물에 빠진 사람까지의 시간 
        water_time = math.sqrt((x_p - x_e) ** 2 + (y_p - 0) ** 2) / 5 
        # 총 시간 계산 
        total_time = land_time + water_time 
         
        # 최소 시간을 가지는 입수 지점을 갱신 
        if total_time < min_time: 
            min_time = total_time 
            best_x = x_e 
     
    return best_x 
 
# 입력 예시 
N = int(input()) 
x_p, y_p = map(int, input().split()) 
 
# 최적의 입수 위치를 출력 
print(find_best_entry_point(N, x_p, y_p)) 
