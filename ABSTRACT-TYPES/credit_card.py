

from typing import Any


class Card:
    """Credit Card Data Structure."""
    def __init__(self, name: str, card_id: int, limit: float) -> None:
        self.name = name
        self.card_id = card_id
        self.limit = limit
        self.balance = 0.
    
    def charge(self, amount: float) -> bool:
        if amount + self.balance > self.limit:
            print("Charge Denyed.")
            return False
        self.balance += amount
        print("Charge Processed.")
        return True
    
    def deposit(self, amount: float) -> bool:
        if self.balance - amount < 0:
            print("Deposit Denyed.")
            return False
        self.balance -= amount
        print("Deposit Processed.")
        return True
    
    def __str__(self):
        return f"\nName: {self.name}\nCard: {self.card_id}\nLimit: {self.limit}\nBalance: {self.balance}\n"


if __name__ == "__main__":
    credit_card = Card("Máximo", 42, 500)
    print(credit_card)

    credit_card.charge(200)
    print(credit_card)

    credit_card.deposit(150)
    print(credit_card)

    credit_card.charge(11234)
    print(credit_card)