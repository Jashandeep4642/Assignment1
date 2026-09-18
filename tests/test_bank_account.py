import unittest
from decimal import Decimal

from account.bank_account import BankAccount
from account.account_status import AccountStatus
from account.client import Client


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.owner = Client(
            1010,
            "Pete Zahut",
            "pzahut@vernon-mullain.ca"
        )
        self.account = BankAccount(
            20019,
            Decimal("1000.00"),
            self.owner,
            AccountStatus.ACTIVE
        )

    # __init__ Method

    def test_init_account_id_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            BankAccount(
                -1,
                Decimal("1000.00"),
                self.owner,
                AccountStatus.ACTIVE
            )

        self.assertEqual(
            "account_id must be a value greater than zero.",
            str(context.exception)
        )

    def test_init_account_id_zero(self):
        with self.assertRaises(ValueError) as context:
            BankAccount(
                0,
                Decimal("1000.00"),
                self.owner,
                AccountStatus.ACTIVE
            )

        self.assertEqual(
            "account_id must be a value greater than zero.",
            str(context.exception)
        )

    def test_init_new_instance(self):
        account = BankAccount(
            20019,
            Decimal("1000.00"),
            self.owner,
            AccountStatus.ACTIVE
        )

        self.assertEqual(20019, account._BankAccount__account_id)
        self.assertEqual(
            Decimal("1000.00"),
            account._BankAccount__balance
        )
        self.assertEqual(
            self.owner,
            account._BankAccount__owner
        )
        self.assertEqual(
            AccountStatus.ACTIVE,
            account._BankAccount__status
        )

    # Account Id Property

    def test_account_id_returns_current_state(self):
        self.assertEqual(20019, self.account.account_id)

    # Balance Property

    def test_balance_returns_current_state(self):
        self.assertEqual(
            Decimal("1000.00"),
            self.account.balance
        )

    # Owner Property

    def test_owner_returns_current_state(self):
        self.assertEqual(self.owner, self.account.owner)

    # Status Property

    def test_status_returns_current_state(self):
        self.assertEqual(
            AccountStatus.ACTIVE,
            self.account.status
        )

    # Update Balance Method

    def test_update_balance_increase_with_positive_amount(self):
        self.account.update_balance(Decimal("100.00"))

        self.assertEqual(
            Decimal("1100.00"),
            self.account._BankAccount__balance
        )

    def test_update_balance_decrease_with_negative_amount(self):
        self.account.update_balance(Decimal("-100.00"))

        self.assertEqual(
            Decimal("900.00"),
            self.account._BankAccount__balance
        )

    # Deposit Method

    def test_deposit_amount_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(Decimal("-100.00"))

        self.assertEqual(
            "amount must be a value greater than or equal to zero.",
            str(context.exception)
        )

    def test_deposit_increase_balance_by_amount(self):
        self.account.deposit(Decimal("100.00"))

        self.assertEqual(
            Decimal("1100.00"),
            self.account._BankAccount__balance
        )

    # Withdraw Method

    def test_withdraw_amount_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(Decimal("-100.00"))

        self.assertEqual(
            "amount must be a value greater than or equal to zero.",
            str(context.exception)
        )

    def test_withdraw_amount_zero(self):
        self.account.withdraw(Decimal("0.00"))

        self.assertEqual(
            Decimal("1000.00"),
            self.account._BankAccount__balance
        )

    def test_withdraw_amount_greater_than_balance(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(Decimal("1100.00"))

        self.assertEqual(
            "amount cannot exceed the account balance.",
            str(context.exception)
        )

    def test_withdraw_decrease_balance_by_amount(self):
        self.account.withdraw(Decimal("100.00"))

        self.assertEqual(
            Decimal("900.00"),
            self.account._BankAccount__balance
        )

    # __str__ Method

    def test_str_returns_string_representation(self):
        account = BankAccount(
            20019,
            Decimal("6764.67"),
            self.owner,
            AccountStatus.ACTIVE
        )

        self.assertEqual(
            "Account Number: 20019 Balance: $6,764.67",
            str(account)
        )