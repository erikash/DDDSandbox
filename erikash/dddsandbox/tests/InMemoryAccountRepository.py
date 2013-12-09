from erikash.dddsandbox.domain.AccountRepository import AccountRepository

__author__ = 'erik'


class InMemoryAccountRepository(AccountRepository):
    def __init__(self):
        self._list = set()

    def add(self, account):
        self._list.add(account)

    def get_by_id(self, account_id):
        return next(x for x in self._list if x.id == account_id)