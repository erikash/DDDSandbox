import unittest
from erikash.dddsandbox.domain import Account, DomainEvents

__author__ = 'erik.ashepa'


class BalanceChangedEventHandler:

    def __init__(self):
        self.balance_changed_event_name = ''

    def handle(self, balance_changed_event):
        self.balance_changed_event_name = balance_changed_event.__class__.__name__


class DomainEventsTest(unittest.TestCase):
    def test_publish_domain_event_to_registered_handler(self):
        handler = BalanceChangedEventHandler()
        DomainEvents.register(handler)
        account = Account()
        account.deposit(1000)
        self.assertTrue(handler.balance_changed_event_name == "BalanceChangedEvent", "Handler didn't handle the event")

if __name__ == '__main__':
    unittest.main()