from erikash.dddsandbox.domain.DomainEvents import DomainEvents
from erikash.dddsandbox.domain.BalanceChangedEvent import BalanceChangedEvent

__author__ = 'erik.ashepa'


class Account:
    def __init__(self):
        self.balance = 0
        self.id = 0

    def deposit(self, amount):
        self.balance += amount
        DomainEvents.publish(BalanceChangedEvent(self.id, amount))


account = Account()
account.deposit(1000)

