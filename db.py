from tinydb import TinyDB,Query

class DB:
    def __init__(self, filename:str) -> None:
        self.filename = filename

    def companies(self) -> list:
        query = Query()
        db = TinyDB(self.filename)
        db.default_table_name = 'Mobile'

        companies = []
        for i in  db.search(query.company.search('')):
            if i["company"] not in companies:
                companies.append(i["company"])
        return companies

    def company_mobile(self, company:str) -> list:
        query = Query()
        db = TinyDB(self.filename)
        db.default_table_name = 'Mobile'

        data_mobile = db.search(query.company == company)
        return data_mobile


    def company_mobile_name(self, company:str) -> list:
        query = Query()
        db = TinyDB(self.filename)
        db.default_table_name = 'Mobile'

        data_mobile = db.search(query.company == company)
        mobil_name = []
        for i in data_mobile:
            if i['name'] not in mobil_name:
                mobil_name.append(i['name'])
        return mobil_name


    def pone_name(self) ->list:
        query = Query()
        db = TinyDB(self.filename)
        db.default_table_name = 'Mobile'

        pone_name = db.search(query.name.search(''))
        pone_name_list = []
        for i in pone_name:
            if i['name'] not in pone_name_list:
                pone_name_list.append(i['name'])
        return pone_name_list

    def mobile_imeg(self, mobile_name:str) -> str:
        query = Query()
        db = TinyDB(self.filename)
        db.default_table_name = 'Mobile'

        image = db.search(query.name == mobile_name)
        img_url = image[0]['img_url']
        return img_url

    def mobol_info(self, mobile_name:str) -> dict:
        query = Query()
        db = TinyDB(self.filename)
        db.default_table_name = 'Mobile'

        data_mobil = db.search(query.name == mobile_name)[0]
        return data_mobil