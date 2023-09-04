from unittest import TestCase
from dave_package.Bank_App import BankAccount


class TestBankAccount(TestCase):

    def __init__(self, method_name: str = ...):
        super().__init__(method_name)
        self.pin = 1234
        self.accounts = {}

    def setUp(self):
        self.bank = BankAccount()

    def test_register(self):
        self.bank.register(123456)
        self.assertEqual(self.bank.pin, 1234)
        self.assertEqual(self.bank.accounts, {123456: 0})

    def test_get_pin(self):
        self.assertEqual(self.bank.pin, 1234)
        print(self.bank.pin)

    def test_incorrect_pin(self):
        with self.assertRaises(ValueError):
            self.bank.incorrect_pin(123456, 1234)

    def test_deposit(self):
        self.bank.accounts[123456] = 0
        with self.assertRaises(ValueError):
            self.bank.deposit(789012, 100)
        initial_balance = self.bank.accounts[123456]
        deposit_amount = 1000
        expected_balance = initial_balance + deposit_amount
        updated_balance = self.bank.deposit(123456, deposit_amount)
        self.assertEqual(updated_balance, expected_balance)

    def test_check_balance(self):
        self.bank.accounts[123456] = 1000
        balance = self.bank.check_balance(123456)
        self.assertEqual(balance, 1000)
        self.assertEqual(self.bank.accounts, {123456: 1000})

    def test_transfer_with_pin(self):
        self.bank.accounts[123456] = 1000
        self.bank.accounts[789012] = 1000
        self.bank.transfer_with_pin(123456, 789012, 1000, self.bank.accounts[123456])
        self.assertEqual(self.bank.accounts[123456], 0)
        self.assertEqual(self.bank.accounts[789012], 2000)

    def test_withdraw(self):
        self.bank.accounts[123456] = 1000
        self.bank.withdraw(123456, 500)
        expected_balance = 500
        actual_balance = self.bank.accounts[123456]
        self.assertEqual(expected_balance, actual_balance)

    def test_find_account(self):
        self.bank.accounts = [123456]
        self.assertEqual(self.bank.accounts, [123456])

    def test_lock_account(self):
        account_number = 123456
        self.bank.accounts[account_number] = 1000
        self.bank.lock_account(account_number)
        self.assertEqual(self.bank.accounts.get(account_number, 0), 0)
