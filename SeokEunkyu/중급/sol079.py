import sys 
import itertools 
 
def is_palindrome(s): 
    return s == s[::-1] 
 
def can_form_palindrome(N, strings): 
    # 모든 순열을 생성하여 팰린드롬 여부 확인 
    for perm in itertools.permutations(strings): 
        concatenated = ''.join(perm) 
        if is_palindrome(concatenated): 
            return \"YES\" 
    return \"NO\" 
 
if __name__ == \"__main__\": 
    import sys 
    input = sys.stdin.read 
    data = input().splitlines() 
     
    N = int(data[0]) 
    strings = [line.strip() for line in data[1:N+1]] 
     
    result = can_form_palindrome(N, strings) 
    print(result) 
