def max_non_crossing_segments(N): 
    return 2 * N - 3 
 
# 입력 받기 
if __name__ == \"__main__\": 
    import sys 
    N_input = int(sys.stdin.readline()) 
    result = max_non_crossing_segments(N_input) 
    print(result) 
