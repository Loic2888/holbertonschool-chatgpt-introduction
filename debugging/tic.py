#!/usr/bin/python3

def print_board(board):
	"""
	Function description:
		Print the current state of the Tic Tac Toe board.

	Parameters:
		board (list[list[str]]): 3x3 grid containing "X", "O", or " ".

	Returns:
		None
	"""
	for row in board:
		print(" | ".join(row))
		print("-" * 5)


def check_winner(board):
	"""
	Function description:
		Check if there is a winner on the board.

	Parameters:
		board (list[list[str]]): 3x3 grid containing "X", "O", or " ".

	Returns:
		str: "X" or "O" if a player has won, or None if there is no winner yet.
	"""
	# Check rows
	for row in board:
		if row[0] != " " and row.count(row[0]) == len(row):
			return row[0]

	# Check columns
	for col in range(len(board[0])):
		if (
			board[0][col] != " "
			and board[0][col] == board[1][col] == board[2][col]
		):
			return board[0][col]

	# Check diagonals
	if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
		return board[0][0]

	if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
		return board[0][2]

	return None


def is_board_full(board):
	"""
	Function description:
		Determine if the board is full (no empty spaces left).

	Parameters:
		board (list[list[str]]): 3x3 grid containing "X", "O", or " ".

	Returns:
		bool: True if the board is full, False otherwise.
	"""
	for row in board:
		if " " in row:
			return False
	return True


def tic_tac_toe():
	"""
	Function description:
		Run an interactive Tic Tac Toe game for two players ("X" and "O"),
		handling invalid inputs and detecting wins and draws.

	Parameters:
		None

	Returns:
		None
	"""
	board = [[" "]*3 for _ in range(3)]
	player = "X"

	while True:
		print_board(board)

		# Vérifier s'il y a un gagnant
		winner = check_winner(board)
		if winner is not None:
			print(f"Player {winner} wins!")
			break

		# Vérifier match nul
		if is_board_full(board):
			print("It's a draw!")
			break

		# Saisie sécurisée
		try:
			row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
			col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
		except ValueError:
			print("Invalid input. Please enter numeric values (0, 1, or 2).")
			continue

		# Vérifier les bornes
		if row < 0 or row > 2 or col < 0 or col > 2:
			print("Row and column must be 0, 1, or 2. Try again.")
			continue

		# Case déjà occupée
		if board[row][col] != " ":
			print("That spot is already taken! Try again.")
			continue

		# Jouer le coup
		board[row][col] = player

		# Changer de joueur
		player = "O" if player == "X" else "X"


if __name__ == "__main__":
	tic_tac_toe()
