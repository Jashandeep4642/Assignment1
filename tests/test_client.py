import unittest

from email_validator import EmailNotValidError

from account.client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(
            1010,
            "Pete Zahut",
            "pzahut@yarrow-mullein.ca"
        )

    # __init__ Method

    def test_init_client_id_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            Client(
                -1,
                "Pete Zahut",
                "pzahut@yarrow-mullein.ca"
            )

        self.assertEqual(
            "client_id must be a value greater than zero.",
            str(context.exception)
        )

    def test_init_client_id_zero(self):
        with self.assertRaises(ValueError) as context:
            Client(
                0,
                "Pete Zahut",
                "pzahut@yarrow-mullein.ca"
            )

        self.assertEqual(
            "client_id must be a value greater than zero.",
            str(context.exception)
        )

    def test_init_name_empty_string(self):
        with self.assertRaises(ValueError) as context:
            Client(
                1010,
                "",
                "pzahut@yarrow-mullein.ca"
            )

        self.assertEqual(
            "name cannot be an empty string.",
            str(context.exception)
        )

    def test_init_email_invalid(self):
        with self.assertRaises(EmailNotValidError):
            Client(
                1010,
                "Pete Zahut",
                "invalid-email"
            )

    def test_init_new_instance(self):
        client = Client(
            1010,
            "Pete Zahut",
            "pzahut@yarrow-mullein.ca"
        )

        self.assertEqual(
            1010,
            client._Client__client_id
        )
        self.assertEqual(
            "Pete Zahut",
            client._Client__name
        )
        self.assertEqual(
            "pzahut@yarrow-mullein.ca",
            client._Client__email_address
        )

    # Client Id Property

    def test_client_id_returns_current_state(self):
        self.assertEqual(
            1010,
            self.client.client_id
        )

    # Name Property

    def test_name_returns_current_state(self):
        self.assertEqual(
            "Pete Zahut",
            self.client.name
        )

    # Email Address Property

    def test_email_address_returns_current_state(self):
        self.assertEqual(
            "pzahut@yarrow-mullein.ca",
            self.client.email_address
        )

    def test_email_address_set_invalid_email(self):
        with self.assertRaises(EmailNotValidError):
            self.client.email_address = "invalid-email"

    def test_email_address_set_valid_email(self):
        self.client.email_address = "newemail@example.com"

        self.assertEqual(
            "newemail@example.com",
            self.client._Client__email_address
        )

    # __str__ Method

    def test_str_returns_string_representation(self):
        self.assertEqual(
            "Pete Zahut [1010] - pzahut@yarrow-mullein.ca",
            str(self.client)
        )