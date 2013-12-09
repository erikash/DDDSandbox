__author__ = 'erik'


class AccountBalanceService(object):
    def __init__(self, account_repository):
        self._account_repository = account_repository

    def deposit(self, account_id, amount):
        account = self._account_repository.get_by_id(account_id)
        account.deposit(amount)