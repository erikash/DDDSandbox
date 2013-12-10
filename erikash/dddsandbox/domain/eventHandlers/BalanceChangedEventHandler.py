__author__ = 'erik.ashepa'


class BalanceChangedEventHandler(object):
    def __init__(self, journalRepository):
        self.journalRepository = journalRepository

    def handle(self, balanceChangedEvent):
        self.journalRepository.add(
            "Amount of " + balanceChangedEvent.amount + "was deposited to account " + balanceChangedEvent.accountId)