import string
def encode(cipher, shift):
    """
    Returns tuple with lowercase alphabet
    Encodes the input text with shift by number.
    """
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    encoded_str = ''
    
    for char in cipher:
        if char.isalpha():  
            char_lower = char.lower()
            index = alphabet.index(char_lower)
            shifted_index = (index + shift) % 26
            shifted_char = alphabet[shifted_index]
            encoded_str += shifted_char
        else:
            encoded_str += char
    
    return (alphabet, encoded_str)
alphabet, encoded_text = encode("", 0)  # Empty input, shift doesn't matter
print(alphabet)  # Output: ['a', 'b', 'c', ..., 'z']
print(encoded_text)  # Output: ''

def decode(cipher, shift):
    """
    Decodes and returns the decoded text.
    """
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    decoded_str = ''
    
    for char in cipher:
        if char.isalpha(): 
            is_upper = char.isupper()
            char_lower = char.lower()
            index = alphabet.index(char_lower)
            shifted_index = (index - shift) % 26
            shifted_char = alphabet[shifted_index]
            if is_upper:
                shifted_char = shifted_char.upper()
            decoded_str += shifted_char
        else:
            decoded_str += char
    
    return decoded_str


alphabet, encoded_text = encode("A", 3)
print(encoded_text)  

alphabet, encoded_text = encode("XyZ", 3)
print(encoded_text)  

alphabet, encoded_text = encode("X!y.Z&", 3)
print(encoded_text)  

alphabet, encoded_text = encode("Calmly we walk on this April day", 10)
print(encoded_text)  

import datetime

class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        self.name = name
        self.ID = ID
        self.creation_date = creation_date if creation_date else datetime.date.today()
        self.balance = balance

        if self.creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future.")

    def deposit(self, amount):
        if amount < 0:
            return  
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def view_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if (datetime.date.today() - self.creation_date).days < 180:
            return  
        if self.balance - amount < 0:
            return  
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if self.balance - amount < 0:
            # This applies a $30 overdraft fee
            self.balance -= (amount + 30)
            print(f"Withdrew ${amount}. Overdraft fee of $30. New balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")