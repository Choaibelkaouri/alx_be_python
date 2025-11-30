class BankAccount:
    """A simple bank account class that supports basic banking operations."""

    def __init__(self, initial_balance=0.0):
        """
        Initialize the bank account.

        :param initial_balance: optional starting balance, defaults to 0.0
        """
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.

        :param amount: amount to deposit (must be non-negative)
        """
        if amount is None:
            return
        if amount < 0:
            # Ignore negative deposits (or you could raise an exception)
            return
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient funds exist.

        :param amount: amount to withdraw
        :return: True if withdrawal succeeded, False otherwise
        """
        if amount is None:
            return False
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Display the current balance in a user-friendly format.

        The balance is formatted with two decimal places to match tests:
        e.g. 'Current Balance: $250.00'
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
