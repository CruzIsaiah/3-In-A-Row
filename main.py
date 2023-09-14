# Step 1: Create a function to print the board.
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Step 2: Create a function to check if the game is over (win or tie).
def game_over(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True

    for col in range(3):
        check = [board[row][col] for row in range(3)]
        if check.count(check[0]) == 3 and check[0] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return True

    return False

# Step 3: Create the minimax algorithm.
def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'tie': 0}

    if game_over(board):
        result = scores['X'] if is_maximizing else scores['O']
        return result

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # AI's move
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'  # Player's move
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# Step 4: Create a function to make the AI move using minimax.
def ai_move(board):
    best_move = None
    best_eval = -float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # AI's move
                eval = minimax(board, 0, False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    return best_move

# Step 5: Create the main game loop.
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True  # True for X (Player), False for O (AI)

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over(board):
        if player_turn:
            while True:
                try:
                    move = int(input("Enter your move (1-9): "))
                    if 1 <= move <= 9:
                        row, col = get_coordinates(move)
                        if board[row][col] != ' ':
                            print("Invalid move. Try again.")
                            continue
                        board[row][col] = 'X'  # Player's move
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 9.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("AI is thinking...")
            row, col = ai_move(board)
            board[row][col] = 'O'  # AI's move

        print_board(board)
        player_turn = not player_turn

    if minimax(board, 0, True) == 1:
        print("You win!")  # Corrected message
    elif minimax(board, 0, True) == -1:
        print("AI wins!")
    else:
        print("It's a tie!")

def get_coordinates(move):
    move -= 1  # Adjust for 0-based index
    row = move // 3
    col = move % 3
    return row, col

if __name__ == "__main__":
    main()
