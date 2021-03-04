
from urllib import request
import json
from math import sqrt

class User:
    
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.username = data["username"]
        self.email = data["email"]
        self.address = data["address"]
        self.phone = data["phone"]
        self.website = data["website"]
        self.company = data["company"]
        self.todos_done = 0

    def get_city(self):
        try:
            return self.address["city"]
        except:
            return None

    def get_dict_format(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "address": self.address,
            "phone": self.phone,
            "website": self.website,
            "company": self.company
        }

    def get_dict_format_with_todos(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "address": self.address,
            "phone": self.phone,
            "website": self.website,
            "company": self.company,
            "todos_done": self.todos_done
        }
    

class Users:

    def __init__(self) -> None:
        self.users = []
    
    def get_users(self):
        try:
            with request.urlopen('https://jsonplaceholder.typicode.com/users') as response:
                data = json.loads(response.read().decode())
                for user in data:
                    self.users.append(User(user))
        except:
            print("Response error")

    def print_list_of_cities(self):
        cities = []
        for user in self.users:
            if user.get_city() not in cities:
                cities.append(user.get_city())
        print(cities)

    def get_dist(self, user1, user2):
        return sqrt((float(user2.address["geo"]["lng"]) - float(user1.address["geo"]["lng"])) ** 2 - (float(user2.address["geo"]["lng"]) - float(user1.address["geo"]["lng"])) ** 2)

    def so_close(self):
        min_dist = 100000000000000
        users_with_min_dist = []
        for user1 in self.users:
            for user2 in self.users:
                if not user1 is user2 and self.get_dist(user1, user2) < min_dist:
                    min_dist = self.get_dist(user1, user2)
                    users_with_min_dist = [user1, user2]
        for user in users_with_min_dist:
            print(user.address)

    def dump(self, filename = 'users.json'):
        data = []
        for user in self.users:
            data.append(user.get_dict_format())
        with open(filename, 'w') as dump_file:
            json.dump(data, dump_file)

    def add_todos(self):
        try:
            with request.urlopen('https://jsonplaceholder.typicode.com/todos') as response:
                data = json.loads(response.read().decode())
                for todo in data:
                    for user in self.users:
                        if user.id == todo['userId']:
                            user.todos_done += 1
        except:
            print('Response error')
    
    def dump_with_todos(self, filename = 'users_with_todos.json'):
        data = []
        for user in self.users:
            data.append(user.get_dict_format_with_todos())
        with open(filename, 'w') as dump_file:
            json.dump(data, dump_file)
