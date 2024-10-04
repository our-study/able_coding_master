import sys 
import itertools 
 
def read_graph(): 
    \"\"\" 
    그래프의 정점 수와 간선 수를 읽고, 인접 행렬을 생성합니다. 
    \"\"\" 
    line = sys.stdin.readline() 
    if not line: 
        return None, None, None 
    N, M = map(int, line.strip().split()) 
    adj_matrix = [[0 for _ in range(N)] for _ in range(N)] 
    for _ in range(M): 
        u, v = map(int, sys.stdin.readline().strip().split()) 
        adj_matrix[u-1][v-1] = 1 
        adj_matrix[v-1][u-1] = 1  # 무향 그래프이므로 대칭으로 표시 
    return N, M, adj_matrix 
 
def are_isomorphic(N1, M1, G1, N2, M2, G2): 
    \"\"\" 
    두 그래프가 동형인지 판단합니다. 
    \"\"\" 
    # 기본 조건 확인 
    if N1 != N2 or M1 != M2: 
        return False 
     
    # 정점 번호의 모든 순열을 생성하여 비교 
    vertices = list(range(N1)) 
    for perm in itertools.permutations(vertices): 
        is_iso = True 
        for i in range(N1): 
            for j in range(N1): 
                if G1[i][j] != G2[perm[i]][perm[j]]: 
                    is_iso = False 
                    break 
            if not is_iso: 
                break 
        if is_iso: 
            return True 
    return False 
 
def main(): 
    # 첫 번째 그래프 읽기 
    N1, M1, G1 = read_graph() 
    if N1 is None: 
        print(\"NO\") 
        return 
     
    # 두 번째 그래프 읽기 
    N2, M2, G2 = read_graph() 
    if N2 is None: 
        print(\"NO\") 
        return 
     
    # 동형 여부 판단 
    if are_isomorphic(N1, M1, G1, N2, M2, G2): 
        print(\"YES\") 
    else: 
        print(\"NO\") 
 
if __name__ == \"__main__\": 
    main() 
