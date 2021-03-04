
"""
1) Что такое JSON?

JSON - java script object notation. Текстовый формат для хранения и обмена информацией.

2)Что такое сериализация/десериализация?

Сериализация - процесс преобразования объектов в строку. Дессериализация - обратный процесс (строка -> объект)

"""

from json import dump, dumps, load, loads
import json
import users

json_example = {
	"userId": 1,
	"id": 1,
	"title": "delectus aut autem",
	"completed": False
}
print("json_example", json_example)

json_example_string = dumps(json_example)
print("dumps", json_example_string)
print("loads", loads(json_example_string))

with open ("dump.json", "w") as dump_file:
    dump(json_example, dump_file)

with open("load.json", "r") as load_file:
    loaded = load(load_file)

print("from_file", loaded)

data_types = {
    "dict": {"a": 1, "b": 2},
    "list": [1, 2],
    "tuple": (1, 2),
    "str": "string",
    "int": 1,
    "float": 1.212,
    "true": True,
    "false": False,
    "None": None
}

str_data_types = dumps(data_types)
print("dumps data_types", str_data_types)
print("loads data types", loads(str_data_types))

print("types with indent", dumps(data_types, indent=4))
print("types with indent n sort", dumps(data_types, indent=4, sort_keys=True))
print("types with indent n separator", dumps(data_types, indent=4, separators=(":", "||")))


json_users = users.Users()
json_users.get_users()
json_users.print_list_of_cities()
json_users.so_close()
json_users.dump()
json_users.add_todos()
json_users.dump_with_todos()
