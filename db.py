from msilib import datasizemask
from pprint import pprint
from unittest import mock
from tinydb import TinyDB,Query

class DB:
    def __init__(self, filename:str) -> None:
        self.db = TinyDB(filename)
        self.query = Query()
        self.table = None
        self.mobel = None

    def company(self, company:str) -> list:
        self.db.default_table_name = company
        self.table = company
        mobil_company = self.db.search(self.query.company.search(company))
        return mobil_company

    def company_name(self, company:str) -> list:
        self.db.default_table_name = company
        self.table = company
        mobil_company = self.db.search(self.query.company.search(company))
        mobil_name = []
        for i in mobil_company:
            if i['name'] not in mobil_name:
                mobil_name.append(i['name'])

        return mobil_name

    def company_mobil(self, mobil:str) -> dict:
        self.db.default_table_name = self.table
        self.mobel = mobil
        data = self.db.search(self.query.name.search(mobil))
        return data

    def company_mobil_imeg(self, mobil_name:str) -> list:
        self.db.default_table_name = self.table
        data = self.db.search((self.query.name == mobil_name))
        return data



# x = DB('db.json')
# pprint(x.companys('Apple'))
# x.company_mobil('Apple iPhone XR')
# pprint(x.company_mobil_price(1644.2))