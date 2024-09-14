from json2table import convert
import json

value = ['''
       {
           "_id": {
               "$Col1": "XXXXXXX2443"
           },
           "col2": false,
           "col3": "359335050111111",
           "startedAt": {
               "$date": 1633309625000
           },
           "endedAt": {
               "$date": 1633310213000
           },
           "col4": "YYYYYYYYYYYYYYYYYY",
           "created_at": {
               "$date": 1633310846935
           },
           "updated_at": {
               "$date": 1633310846935
           },
           "__v": 0
       }''']


def print_html(name):
    html = convert(json.loads(name[0]))
    print(html)



if __name__ == '__main__':
    print_html(value)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
