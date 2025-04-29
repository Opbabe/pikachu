def detect_threat(board, player):
    opponent = 'Player 2' if player == 'Player 1' else 'Player 1'
    for row in range(6):
        for col in range(7):
            if board[row][col] == opponent.token:
                # Check if the opponent has a winning move on the next turn
                if check_line(row, col, 1, 0, opponent) or \
                        check_line(row, col, 0, 1, opponent) or \
                        check_line(row, col, 1, 1, opponent) or \
                        check_line(row, col, 1, -1, opponent):
                    return True
    return False
