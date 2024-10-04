from itertools import permutations 
 
def solve_word_puzzle(words): 
    # 주어진 6개의 단어를 사전순으로 정렬한 후 가능한 모든 순열을 생성 
    words.sort() 
    for perm in permutations(words): 
        # 가로 방향 단어 3개 
        row1, row2, row3 = perm[:3] 
 
        # 세로 방향 단어 생성 
        col1 = row1[0] + row2[0] + row3[0] 
        col2 = row1[1] + row2[1] + row3[1] 
        col3 = row1[2] + row2[2] + row3[2] 
 
        # 세로 단어가 나머지 3개의 단어에 있는지 확인하고 중복 방지 
        remaining_words = set(perm[3:]) 
        if {col1, col2, col3} == remaining_words: 
            # 조건 만족 시 사전순으로 가장 빠른 해답을 출력 후 종료 
            print(row1) 
            print(row2) 
            print(row3) 
            return 
 
# 입력 처리 
words = [input().strip() for _ in range(6)] 
 
# 결과 출력 
solve_word_puzzle(words) 
