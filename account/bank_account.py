from decimal import Decimal

from account.client import Client
from account.account_status import AccountStatus


class BankAccount:
    def __init__(
        self,
        account_id: int,
        balance: Decimal,
        owner: Client,
        status: AccountStatus
    ):
        if account_id <= 0:
            raise ValueError(
                "account_id must be a value greater than zero."
            )

        self.__account_id = account_id
        self.__balance = balance
        self.__owner = owner
        self.__status = status

    @property
    def account_id(self) -> int:
        return self.__account_id

    @property
    def balance(self) -> Decimal:
        return self.__balance

    @property
    def owner(self) -> Client:
        return self.__owner

    @property
    def status(self) -> AccountStatus:
        return self.__status

    @status.setter
    def status(self, value: AccountStatus) -> None:
        self.__status = value

    def update_balance(self, amount: Decimal) -> None:
        self.__balance += amount

    def deposit(self, amount: Decimal) -> None:
        if amount < 0:
            raise ValueError(
                "amount must be a value greater than or equal to zero."
            )

        self.update_balance(amount)

    def withdraw(self, amount: Decimal) -> None:
        if amount < 0:
            raise ValueError(
                "amount must be a value greater than or equal to zero."
            )

        if amount > self.__balance:
            raise ValueError(
                "amount cannot exceed the account balance."
            )

        self.update_balance(-amount)

    def __str__(self) -> str:
        return (
            f"Account Number: {self.__account_id} "
            f"Balance: ${self.__balance:,.2f}"
        )