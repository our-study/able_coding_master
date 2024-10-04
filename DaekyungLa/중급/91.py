import sys

n = int(sys.stdin.readline().strip())

def is_pretty_number(n):
    str_n = str(n)
    length = len(str_n)
    
    for i in range(1, length):
        sub_number = int(str_n[:i])
        if sub_number != 0 and n % sub_number == 0:
            print("YES")
            return

    for i in range(1, length):
        sub_number = int(str_n[-i:])
        if sub_number != 0 and n % sub_number == 0:
            print("YES")
            return
    print("NO")

is_pretty_number(n)
