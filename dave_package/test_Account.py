import unittest
from dave_package.Account import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    def test_set_pin(self):
        self.account.set_pin()
        self.assertTrue(self.account.pin.isdigit() and len(self.account.pin) == 4)

    def test_get_name(self):
        self.account.get_name()
        self.assertTrue(not self.account.name.isdigit())

    def test_deposit(self):
        initial_balance = self.account.check_balance()
        self.account.deposit(100.0)
        self.assertEqual(self.account.check_balance(), initial_balance + 100.0)

    def test_withdraw(self):
        self.account.deposit(100.0)
        initial_balance = self.account.check_balance()
        self.account.withdraw(50.0)
        self.assertEqual(self.account.check_balance(), initial_balance - 50.0)

    def test_check_pin(self):
        self.account.set_pin()
        self.assertTrue(self.account.check_pin(self.account.pin))

    def test_check_balance(self):
        self.account.deposit(100.0)
        self.assertEqual(self.account.check_balance(), 100.0)


if __name__ == "__main__":
    unittest.main()
