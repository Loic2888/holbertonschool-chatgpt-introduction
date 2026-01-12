#!/usr/bin/python3
class Checkbook:
	def __init__(self):
		"""
		Function description:
			Initialize a new Checkbook with a starting balance of 0.0.

		Parameters:
			None

		Returns:
			None
		"""
		self.balance = 0.0

	def deposit(self, amount):
		"""
		Function description:
			Add the given amount to the current balance and display the result.

		Parameters:
			amount (float): The amount of money to deposit. Must be non-negative.

		Returns:
			None
		"""
		self.balance += amount
		print("Deposited ${:.2f}".format(amount))
		print("Current Balance: ${:.2f}".format(self.balance))

	def withdraw(self, amount):
		"""
		Function description:
			Subtract the given amount from the current balance if sufficient funds exist.

		Parameters:
			amount (float): The amount of money to withdraw. Must be non-negative.

		Returns:
			None
		"""
		if amount > self.balance:
			print("Insufficient funds to complete the withdrawal.")
		else:
			self.balance -= amount
			print("Withdrew ${:.2f}".format(amount))
			print("Current Balance: ${:.2f}".format(self.balance))

	def get_balance(self):
		"""
		Function description:
			Display the current balance.

		Parameters:
			None

		Returns:
			None
		"""
		print("Current Balance: ${:.2f}".format(self.balance))


def main():
	"""
	Function description:
		Run an interactive checkbook application that lets the user deposit,
		withdraw, check the balance, or exit. All numeric inputs are validated
		to prevent crashes on invalid values.

	Parameters:
		None

	Returns:
		None
	"""
	cb = Checkbook()
	while True:
		action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

		if action == 'exit':
			break

		elif action == 'deposit':
			try:
				amount = float(input("Enter the amount to deposit: $"))
				if amount < 0:
					print("Amount must be non-negative.")
					continue
				cb.deposit(amount)
			except ValueError:
				print("Invalid amount. Please enter a numeric value.")

		elif action == 'withdraw':
			try:
				amount = float(input("Enter the amount to withdraw: $"))
				if amount < 0:
					print("Amount must be non-negative.")
					continue
				cb.withdraw(amount)
			except ValueError:
				print("Invalid amount. Please enter a numeric value.")

		elif action == 'balance':
			cb.get_balance()

		else:
			print("Invalid command. Please try again.")


if __name__ == "__main__":
	main()
