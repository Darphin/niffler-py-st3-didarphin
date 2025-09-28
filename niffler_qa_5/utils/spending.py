import json
import random
from dataclasses import dataclass
from datetime import datetime , date
from faker import Faker


@dataclass
class Spending:
    amount: float
    description: str
    category: str
    spendDate: date
    currency: str

    def __init__(self, amount=0, description="", category="", currency="RUB"):
        self.amount = amount
        self.description = description
        self.category = category
        self.spendDate =  date.today()
        self.currency = currency

    def random_init(self):
        fake = Faker("en_US")
        self.amount = random.randint(1, 1000)
        self.description = fake.text(100)
        self.category = fake.text(5)
        return self

    def to_json(self):
        spend_dict = {
            "amount": self.amount,
            "description": self.description,
            "category": self.category,
            "spendDate":  "2024-08-08T18:39:27.955Z",
            "currency": self.currency
        }
        return json.dumps(spend_dict, default=str)


