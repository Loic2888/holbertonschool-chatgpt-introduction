#!/usr/bin/python3
import random
import os

def clear_screen():
	"""Clear the terminal screen."""
	os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
	def __init__(self, width=10, height=10, mines=10):
		"""Initialize the Minesweeper board."""
		self.width = width
		self.height = height
		self.mines = set(random.sample(range(width * height), mines))
		self.revealed = [[False for _ in range(width)] for _ in range(height)]

	def print_board(self, reveal=False):
		"""Display the current state of the board."""
		clear_screen()
		print('  ' + ' '.join(str(i) for i in range(self.width)))
		for y in range(self.height):
			print(y, end=' ')
			for x in range(self.width):
				if reveal or self.revealed[y][x]:
					if (y * self.width + x) in self.mines:
						print('*', end=' ')
					else:
						count = self.count_mines_nearby(x, y)
						print(count if count > 0 else ' ', end=' ')
				else:
					print('.', end=' ')
			print()

	def count_mines_nearby(self, x, y):
		"""Count how many mines are adjacent to cell (x, y)."""
		count = 0
		for dx in [-1, 0, 1]:
			for dy in [-1, 0, 1]:
				nx, ny = x + dx, y + dy
				if 0 <= nx < self.width and 0 <= ny < self.height:
					if (ny * self.width + nx) in self.mines:
						count += 1
		return count

	def reveal(self, x, y):
		"""Reveal cell (x, y); return False if it is a mine, True otherwise."""
		idx = y * self.width + x
		if idx in self.mines:
			return False
		if self.revealed[y][x]:
			return True
		self.revealed[y][x] = True
		if self.count_mines_nearby(x, y) == 0:
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					nx, ny = x + dx, y + dy
					if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
						self.reveal(nx, ny)
		return True

	def is_won(self):
		"""Return True if all non-mine cells have been revealed."""
		safe_total = self.width * self.height - len(self.mines)
		revealed_safe = sum(
			1
			for y in range(self.height)
			for x in range(self.width)
			if self.revealed[y][x] and (y * self.width + x) not in self.mines
		)
		return revealed_safe == safe_total

	def play(self):
		"""Main game loop: play until win or mine hit."""
		while True:
			self.print_board()
			if self.is_won():
				print("Congratulations! You've won the game.")
				break
			try:
				x = int(input("Enter x coordinate: "))
				y = int(input("Enter y coordinate: "))
				if x < 0 or x >= self.width or y < 0 or y >= self.height:
					print("Out of bounds. Try again.")
					continue
				if not self.reveal(x, y):
					self.print_board(reveal=True)
					print("Game Over! You hit a mine.")
					break
			except ValueError:
				print("Invalid input. Enter integers only.")


if __name__ == "__main__":
	game = Minesweeper()
	game.play()
