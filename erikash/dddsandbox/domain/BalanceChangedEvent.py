__author__ = 'erik.ashepa'


class BalanceChangedEvent:
    def __init__(self, accountId, amount):
        self.amount = amount
        self.accountId = accountId
