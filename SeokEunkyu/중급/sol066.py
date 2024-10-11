from itertools import permutations

# 입력 처리
N = int(input())  # 교실의 행의 개수
K = int(input())  # 학생들의 관계의 개수

# 관계 저장을 위한 딕셔너리
relations = {}

# K개의 관계 입력 받기
for _ in range(K):
    a, b, c = map(int, input().split())
    relations[(b, c)] = a
    relations[(c, b)] = a  # 관계는 대칭적임

# 학생 번호 리스트 (1번부터 2N번까지)
students = list(range(1, 2 * N + 1))

# 최댓값 저장 변수
max_score = float('-inf')

# 가능한 모든 학생 배치 (순열 생성)
for perm in permutations(students):
    score = 0
    # 각 행의 두 학생에 대해 점수 계산
    for i in range(N):
        s1, s2 = perm[2 * i], perm[2 * i + 1]
        if (s1, s2) in relations:
            if relations[(s1, s2)] == 1:  # 관계가 좋은 경우
                score += 1
            elif relations[(s1, s2)] == 2:  # 관계가 나쁜 경우
                score -= 1
    # 최댓값 갱신
    max_score = max(max_score, score)

# 결과 출력
print(max_score)
