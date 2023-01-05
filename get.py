import re
from tinydb import TinyDB
db = TinyDB("templates.json")


def get_data_type(data):
    if re.match(r'\d{2}\.\d{2}\.\d{4}', data) or re.match(r'\d{4}\-\d{2}\-\d{2}', data):
        return "date"
    if re.match(r'\+7 \d{3} \d{3} \d{2} \d{2}', data):
        return "phone"
    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', data):
        return "email"
    return "text"


def find_data_by_query(query):  # f_name1=value1&f_name2=value2
    keys = []
    types = []
    fields = query.split("&")
    try:
        for i in fields:
            key, item = i.split('=')
            keys.append(key)
            types.append(get_data_type(item))
    except:
        return "ValueError"

    for template in db.all():
        for key, type in zip(keys, types):
            if key in template:
                if template[key] == type:
                    continue
            break
        else:
            return template['name']
    return {keys[i]: types[i] for i in range(len(keys))}
