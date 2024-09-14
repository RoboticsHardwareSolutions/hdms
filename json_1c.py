import json
import tabulate
from pymongo import MongoClient

task_types = ["Изготовление деталей - производство",
              "Печатные платы - Изготовление платы",
              "Печатные платы - Комплектующие для платы",
              "Печатные платы - Монтаж",
              "Печатные платы - Изготовление платы с закупкой и монтажом",
              "Печатные платы - Внешние разъемы",
              "Закупка  - По спецификации",
              "Закупка - Без спецификации",
              "Изготовление - по ТЗ у подрядчика"]

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client['partlists']
    collection = db['agv_m']
    count = 0
    obj = {"Тип задачи": task_types[1],
           "Гиперссылка файлы": "",
           "Номер тикета": "",
           "Позиции": [

           ]
           }
    for collection in collection.find():
        count += 1
        print()
        item = {"N": count,
                "Артикул изготовителя": collection["Article number"],
                "Артикулы аналогов": "",
                "Описание": collection["Textual description"],
                "Изготовитель": collection["Manufacturer"],
                "Контрагент Предполагаемый": "",
                "Количество": float(collection["Quantity"] if collection["Quantity"] == None else '1') * int(
                    collection["Designation quantity"]),
                "Ед.изм": collection["Unity"] if collection["Unity"] == None else 'шт',
                "Поз. по спецификации": str(count),
                "URL": collection["Supplier"],
                "Комментарий": ""
                }
        obj["Позиции"].append(item)

    print(json.dumps(obj, ensure_ascii=False))
    # list = obj["Позиции"] // TODO add print JSON result in tabulate form
    # print(list.index(1))
    # # print(tabulate(list, headers='keys'))
