from itertools import product 
 
def generate_passwords(n, k, characters): 
    # 모든 가능한 조합을 생성 
    all_combinations = product(characters, repeat=k) 
     
    # 조합을 사전순으로 출력 
    for combination in all_combinations: 
        print(''.join(combination)) 
 
# 입력 처리 
n, k = map(int, input().strip().split()) 
characters = input().strip() 
 
# 결과 출력 
generate_passwords(n, k, sorted(characters)) 
