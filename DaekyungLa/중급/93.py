import sys
from collections import deque


N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().strip().split()))
target = 1
deck = deque(cards)

while deck:
    top_card = deck[0]
    bottom_card = deck[-1]
    
    if top_card == target:
        deck.popleft()  
    elif bottom_card == target:
        deck.pop()  
    else:
        print("NO")
        break
    target += 1

else:
    print("YES")
