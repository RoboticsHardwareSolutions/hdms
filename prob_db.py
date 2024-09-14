from pymongo import MongoClient
from tabulate import tabulate
import pymongo
import re


class ProdDB:
    def __init__(self, host, port):
        self.client = MongoClient(host, port)
        self.db = self.client["products"]
        self.collection = self.db["info"]
        self.name_list = []
        self.type_list = []

    def __del__(self):
        self.client.close()

    def names(self) -> list:
        for item in self.collection.find():
            self.name_list.append(item["Name"])
        return self.name_list

    def types(self) -> list:
        for item in self.collection.find():
            self.type_list.append(item["Type"])
        return self.type_list

    def products(self):
        return self.collection

    def add(self, name: str, descr: str, comment: str) -> str:
        pattern = re.compile(r"[A-Z]{2}\-\d{3}\.\d{3}\.\d{3}")
        if pattern.fullmatch(name) is None:
            return "Error product name"
        else:
            try:
                self.names().index(name)
                return "Name already exists"
            except ValueError:
                try:
                    self.types().index(int(name[3:6]))
                    return "Type already exists"
                except ValueError:
                    self._add_product(name, descr, comment)
                    return "Added!"

    def _add_product(self, name, descr, comment) -> str:
        product = {"Name": name, "Type": int(name[3:6]), "Description": descr, "Comment": comment}
        self.collection.insert_one(product)

    def delete(self, name: str) -> bool:
        return self.collection.delete_one({"Name": name}).deleted_count == 1

    def show(self):
        print(tabulate(self.collection.find(), headers='keys'))

    def show_sort_by_type(self):
        print(tabulate(self.collection.find().sort('Type', pymongo.ASCENDING), headers='keys'))


if __name__ == '__main__':
    prod = ProdDB('localhost', 27017)
    print(prod.names())
    print(prod.types())
    print(prod.add("CM-567.001.001", "TEST PRODUCT", "Test comment for product"))
    print(prod.delete("CM-567.001.001"))

    print(prod.add("CM-999.000.000", "Robot Proto Emulator", "Virtual device for software debugging"))
    print(prod.add("CM-998.000.000", "Charger Proto Emulator", "Virtual device for software debugging"))
    print(prod.add("CM-997.000.000", "Remote Controller Emulator", "Virtual device for software debugging"))
    print(prod.add("CM-131.001.001", "HMI Sorter Controller", "HMI оператора сортировочной станции"))

    for item in prod.products().find():
        print(item)

    prod.show()
    prod.show_sort_by_type()
