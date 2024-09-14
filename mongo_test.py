from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    db = client['compositions']
    collection = db['robot']
    print(collection.estimated_document_count())
    for collection in collection.find():
        print(collection)


if __name__ == '__main__':
    main()
