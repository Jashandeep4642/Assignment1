from email_validator import validate_email, EmailNotValidError


class Client:
    def __init__(
        self,
        client_id: int,
        name: str,
        email_address: str
    ):
        if client_id <= 0:
            raise ValueError(
                "client_id must be a value greater than zero."
            )

        name = name.strip()

        if name == "":
            raise ValueError(
                "name cannot be an empty string."
            )

        email_address = email_address.strip()
        email_info = validate_email(
            email_address,
            check_deliverability=False
        )

        self.__client_id = client_id
        self.__name = name
        self.__email_address = email_info.normalized

    @property
    def client_id(self) -> int:
        return self.__client_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email_address(self) -> str:
        return self.__email_address

    @email_address.setter
    def email_address(self, value: str) -> None:
        value = value.strip()

        email_info = validate_email(
            value,
            check_deliverability=False
        )

        self.__email_address = email_info.normalized

    def __str__(self) -> str:
        return (
            f"{self.__name} [{self.__client_id}] - "
            f"{self.__email_address}"
        )