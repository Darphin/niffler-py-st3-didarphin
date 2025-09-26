from datetime import datetime, timedelta
from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from niffler_qa_5.constants import TEST_CATEGORY

import random
from faker import Faker


class Category(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str
    username: str


class Spend(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    username: str
    amount: float
    description: str
    category: str
    spendDate: str = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+00:00'
    currency: str


class SpendAdd(BaseModel):
    amount: float|None=0.0
    description: str=""
    category: dict={"name": TEST_CATEGORY}
    spendDate: str=(datetime.today() - timedelta(hours=24)).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    currency: str="RUB"

    def random_init(self, currency=None, description = None, category=None):
        fake = Faker("en_US")
        self.amount = random.randint(1, 1000)
        self.description = description if description else fake.text(100)
        self.category = category if category else {"name": TEST_CATEGORY}
        self.spendDate =(datetime.today() - timedelta(hours=24)).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        self.currency = currency if currency else self.currency
        return self
