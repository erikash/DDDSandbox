__author__ = 'erik'


class AccountBalanceService(object):
    def __init__(self, accountRepository):
        self._accountRepository = accountRepository

    def deposit(self, account_id, amount):
        account = self._accountRepository.get_by_id(account_id)
        account.deposit(amount)