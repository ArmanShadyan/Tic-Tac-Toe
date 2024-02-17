import random

def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Tie'
    return False

def minimax(board, depth, maximizing_player):
    result = check_win(board)
    if result == 'X':
        return {'score': -1, 'position': None}
    elif result == 'O':
        return {'score': 1, 'position': None}
    elif result == 'Tie':
        return {'score': 0, 'position': None}

    if maximizing_player:
        best_score = {'score': -float('inf'), 'position': None}
        symbol = 'O'
    else:
        best_score = {'score': float('inf'), 'position': None}
        symbol = 'X'

    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = symbol
            score = minimax(board, depth + 1, not maximizing_player)
            board[i] = ' '
            score['position'] = i
            if maximizing_player:
                if score['score'] > best_score['score']:
                    best_score = score
            else:
                if score['score'] < best_score['score']:
                    best_score = score
    return best_score

def tic_tac_toe():
    board = [' '] * 9
    print_board(board)
    while True:
        move = int(input('Your move (0-8): '))
        board[move] = 'X'
        print_board(board)
        result = check_win(board)
        if result:
            print(f'{result} wins!' if result != 'Tie' else 'It\'s a tie!')
            break
        print('Computer\'s move:')
        move = minimax(board, 0, True)['position']
        board[move] = 'O'
        print_board(board)
        result = check_win(board)
        if result:
            print(f'{result} wins!' if result != 'Tie' else 'It\'s a tie!')
            break


tic_tac_toe()
