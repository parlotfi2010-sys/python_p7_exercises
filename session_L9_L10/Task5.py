#==================================
#==============Task 5==============
#==================================


class BankAccount :

    def __init__(self, owner, account_number, balance=0) :
        if not isinstance(balance, (int, float)) or isinstance(balance, bool) :
            raise TypeError('Balance must be a number.')

        if balance < 0 :
            raise ValueError('Balance cannot be negative.')

        self.owner = owner
        self.account_number = str(account_number)
        self.balance = balance
        self.transactions = []

        self.transactions.append(f'Account created with balance: {balance:,.2f}')

    def __str__(self) :
        return (f'Owner: {self.owner}\n'
                f'Account Number: {self.account_number}\n'
                f'Balance: {self.balance:,.2f}')

    def deposit(self, amount) :
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) :
            raise TypeError('Deposit amount must be a number.')

        if amount <= 0 :
            raise ValueError('Deposit amount must be positive.')

        self.balance = self.balance + amount
        self.transactions.append(f'Deposit: +{amount:,.2f}')

    def withdraw(self, amount) :
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) :
            raise TypeError('Withdrawal amount must be a number.')

        if amount <= 0 :
            raise ValueError('Withdrawal amount must be positive.')

        if amount > self.balance :
            raise ValueError('Insufficient balance.')

        self.balance = self.balance - amount
        self.transactions.append(f'Withdrawal : -{amount:,.2f}')

    def transfer(self, target_account, amount) :
        if not isinstance(target_account, BankAccount) :
            raise TypeError('Target must be a BankAccount object.')

        if target_account is self :
            raise ValueError('Cannot transfer money to the same account.')

        if not isinstance(amount, (int, float)) or isinstance(amount, bool) :
            raise TypeError('Transfer amount must be a number.')

        if amount <= 0 :
            raise ValueError('Transfer amount must be positive.')

        if amount > self.balance :
            raise ValueError('Insufficient balance for transfer.')

        self.balance = self.balance - amount
        target_account.balance = target_account.balance + amount

        self.transactions.append(f'Transfer to {target_account.account_number} : - {amount:,.2f}')

        target_account.transactions.append(f'Transfer from {self.account_number} : + {amount:,.2f}')

    def get_balance(self) :
        return self.balance

    def transaction_history(self) :
        print(f'\nTransaction History - {self.owner}')
        print(f'Account Number: {self.account_number}')

        for transaction in self.transactions :
            print(transaction)


class Bank :

    def __init__(self, name) :
        self.name = name
        self.accounts = []

    def create_account(self, owner, account_number, balance=0) :
        account_number = str(account_number)

        existing_account = self.find_account(account_number)

        if existing_account is not None:
            raise ValueError('Account number already exists.')

        account = BankAccount(owner, account_number, balance)
        self.accounts.append(account)

        return account

    def find_account(self, account_number) :
        account_number = str(account_number)

        for account in self.accounts:
            if account.account_number == account_number:
                return account

        return None

    def total_balance(self) :
        total = 0

        for account in self.accounts:
            total = total + account.get_balance()

        return total

    def display_accounts(self) :
        print(f'\nBank : {self.name}')

        for account in self.accounts :
            print()
            print(account)


def main():
    #Create a bank
    bank = Bank('Simple Bank')

    #Create accounts
    ali = bank.create_account('Ali', '1001', 5000000)
    sara = bank.create_account('Sara', '1002', 2000000)

    #Deposit money
    ali.deposit(1000000)

    #Withdraw money
    ali.withdraw(500000)

    #Transfer money
    ali.transfer(sara, 2000000)

    #Display account information
    print(ali)
    print()
    print(sara)

    # Display current balances
    print(f'\nAli balance : {ali.get_balance():,.2f}')
    print(f'Sara balance : {sara.get_balance():,.2f}')

    # Display transaction histories
    ali.transaction_history()
    sara.transaction_history()

    # Search for an account
    found_account = bank.find_account('1002')

    if found_account is not None :
        print('\nAccount found : ')
        print(found_account)
    else:
        print('Account not found.')

    # Display all accounts and total bank balance
    bank.display_accounts()
    print(f'\nTotal Bank Balance : {bank.total_balance():,.2f}')


if __name__ == '__main__' :
    try:
        main()
    except (ValueError, TypeError) as error :
        print(f'Error : {error}')
