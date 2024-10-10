class BankAccount:
    def __init__(self, initial_balance=0):
        """Initializes the account with an optional starting balance."""
        self.account_balance = initial_balance  # Set the initial balance (default 0)

    def deposit(self, amount):
        """Deposits the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws the specified amount from the account balance, if sufficient funds are available."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """Displays the current account balance in a user-friendly format."""
        print(f"Current balance: ${self.account_balance:.2f}")
