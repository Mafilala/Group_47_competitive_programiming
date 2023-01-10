class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(self.balance)
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > self.n:
            return False
        if account2 < 1 or account2 > self.n:
            return False
        
        balance1 = self.balance[account1 - 1]
        balance2 = self.balance[account2 - 1]
        if balance1 < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money 
        return True
    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        if money < 0:
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
