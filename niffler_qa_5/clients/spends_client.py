import json
from dataclasses import asdict
from urllib.parse import urljoin

import requests

from niffler_qa_5.models.spend import Category, SpendAdd, Spend


class SpendsHttpClient:
    session: requests.Session
    base_url: str

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.session = requests.session()
        self.session.headers.update({
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

    def get_categories(self):
        response = self.session.get(urljoin(self.base_url, "/api/categories/all"))
        response.raise_for_status()
        return response.json()

    def add_category(self, name: str) -> Category:
        response = self.session.post(urljoin(self.base_url, "/api/categories/add"), json={
            "name": name
        })
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response
        return Category.model_validate(response.json())

    def update_category(self, id: str, name: str) -> Category:
        response = self.session.patch(urljoin(self.base_url, "/api/categories/update"), json={
            "id": id,
            "name": name
        })
        response.raise_for_status()
        return Category.model_validate(response.json())

    def add_spends(self, spend: SpendAdd):
        url = urljoin(self.base_url, "/api/spends/add")
        x=spend.model_dump()
        response = self.session.post(url, json=spend.model_dump())
        response.raise_for_status()
        return response.json()

    def remove_spends(self, ids: list[int]):
        url = urljoin(self.base_url, "/api/spends/remove")
        response = self.session.delete(url, params={"ids": ids})
        response.raise_for_status()

    def get_statistics(self, username, from_value, to_value, filter_currency="RUB", user_currency="RUB" ):
        url = urljoin(self.base_url,
                      f"/api/stat/total?username={username}&userCurrency={user_currency}&from={from_value}"
                      f"&to={to_value}&f ilterCurrency={filter_currency}")
        response = self.session.get(url)
        response.raise_for_status()
        r = response.json()
        return r

