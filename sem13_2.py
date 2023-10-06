class Loger:
    db = {}

    def __init__(self, path):
        self.__class__.db = load_json(path)
        self.level = None

    def authorize(self, the_id, name):
        user = User(name, the_id)
        print(user)
        print(self.__class__.db)
        for obj in self.__class__.db.values():
            if user == obj:
                self.level = self.__class__.db[str(the_id)]['level']
                return self.level
        else:
            raise Exception('Пользователь с такими данными не найден')


if __name__ == '__main__':
    PATH = 'my_json.json'
    loger = Loger(PATH)
    print(f"Уровень доступа: {loger.authorize(1, 'Алекс')}")