from collections import deque 
 
def can_place_cards_in_order(n, cards): 
    # 카드 더미를 덱으로 초기화 
    card_deck = deque(cards) 
    current_card = 1 
 
    while card_deck: 
        # 맨 위 또는 맨 아래 카드를 확인하여 현재 카드가 순서대로 놓일 수 있는지 확인 
        if card_deck[0] == current_card: 
            card_deck.popleft() 
            current_card += 1 
        elif card_deck[-1] == current_card: 
            card_deck.pop() 
            current_card += 1 
        else: 
            # 맨 위나 맨 아래 카드가 현재 내려놓아야 할 카드가 아닌 경우 
            return \"NO\" 
 
    return \"YES\" 
 
# 입력 처리 
n = int(input().strip()) 
cards = list(map(int, input().split())) 
 
# 결과 출력 
print(can_place_cards_in_order(n, cards)) 
