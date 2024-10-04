import sys 
 
def read_board(): 
    board = [] 
    for _ in range(10): 
        line = sys.stdin.readline().strip() 
        board.append(list(line)) 
    return board 
 
def remove_line(board, direction, index): 
    new_board = [row.copy() for row in board] 
    if direction == 'H': 
        for col in range(10): 
            new_board[index][col] = '.' 
    else:  # direction == 'V' 
        for row in range(10): 
            new_board[row][index] = '.' 
    return new_board 
 
def get_empty_cells(board): 
    empty = [] 
    for r in range(10): 
        for c in range(10): 
            if board[r][c] == '.': 
                empty.append((r, c)) 
    return empty 
 
def place_white(board, r, c): 
    new_board = [row.copy() for row in board] 
    new_board[r][c] = 'W' 
    return new_board 
 
def has_five_or_more_w(board): 
    directions = [ (0,1), (1,0), (1,1), (-1,1) ]  # Right, Down, Down-Right, Up-Right 
    for r in range(10): 
        for c in range(10): 
            if board[r][c] == 'W': 
                for dr, dc in directions: 
                    count = 1 
                    nr, nc = r + dr, c + dc 
                    while 0 <= nr < 10 and 0 <= nc < 10 and board[nr][nc] == 'W': 
                        count += 1 
                        nr += dr 
                        nc += dc 
                    if count >= 5: 
                        return True 
    return False 
 
def main(): 
    board = read_board() 
    count = 0 
    # Iterate over all possible lines 
    for direction in ['H', 'V']: 
        for index in range(10): 
            modified_board = remove_line(board, direction, index) 
            empty_cells = get_empty_cells(modified_board) 
            for r, c in empty_cells: 
                new_board = place_white(modified_board, r, c) 
                if has_five_or_more_w(new_board): 
                    count += 1 
    print(count) 
 
if __name__ == \"__main__\": 
    main() 
