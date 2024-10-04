import sys


def find_optimal_recycling_station(N, apartments):
    # 입력 순서를 기억하기 위해 index를 추가
    apartments_with_index = [(i + 1, D, A) for i, (D, A) in enumerate(apartments)]

    # 아파트 위치를 기준으로 정렬
    apartments_with_index.sort(key=lambda x: x[1])

    # 각 아파트의 사람 수의 누적 합 계산
    total_people = sum(a[2] for a in apartments_with_index)
    half_people = total_people // 2

    # 사람 수의 누적 합으로 중앙값 위치 찾기
    cumulative_people = 0
    for i in range(N):
        cumulative_people += apartments_with_index[i][2]
        if cumulative_people > half_people:
            # i번째 아파트에 분리수거장을 세우는 것이 최적
            # 원래 입력 순서로 출력 (apartment_with_index[i][0]는 입력에서의 원래 인덱스)
            return apartments_with_index[i][0]


# 입력 처리
N = int(sys.stdin.readline().strip())  # 아파트 단지의 수
apartments = []

for _ in range(N):
    D, A = map(int, sys.stdin.readline().strip().split(" "))  # 아파트 단지의 위치 D와 주민 수 A
    apartments.append((D, A))

# 최적의 분리수거장 위치 찾기
optimal_location = find_optimal_recycling_station(N, apartments)
print(optimal_location)
