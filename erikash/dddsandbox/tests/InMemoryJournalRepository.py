__author__ = 'erik.ashepa'


class InMemoryJournalRepository(object):
    def __init__(self):
        self._list = set()

    def add(self, journalEntry):
        self._list.add(journalEntry)