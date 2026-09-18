import unittest

from account.account_status import AccountStatus


class TestAccountStatus(unittest.TestCase):

    def test_account_status_values_initialized(self):
        self.assertEqual(0, AccountStatus.INACTIVE.value)
        self.assertEqual(1, AccountStatus.ACTIVE.value)
        self.assertEqual(2, AccountStatus.SUSPENDED.value)
        self.assertEqual(3, AccountStatus.CLOSED.value)