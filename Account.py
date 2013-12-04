from DomainEvents import DomainEvents

__author__ = 'erik.ashepa'


class BalanceChangedEvent:
    def __init__(self):
        pass


class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, balance):
        self.balance += balance
        DomainEvents.publish(BalanceChangedEvent())


account = Account()
account.deposit(1000)

