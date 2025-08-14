# Базовый класс User и производные классы для различных типов пользователей
#
import bcrypt
#
class User:
    """
    Базовый класс, представляющий пользователя.
    Содержит общие атрибуты и методы для всех пользователей.
    Хранит список всех пользователей в статическом атрибуте.
    """
    users = [] # список для хранения всех пользователей
    def __init__(self, username, email, password):
#
        self.username = username
        self.email = email
#
        if any(user.username == username for user in User.users):
            raise ValueError(f"users_Пользователь с именем {username} уже существует.")
        self.username = username
        self.email = email
        self.password = self.hash_password(password)  # Хешируем пароль при создании пользователя
        User.users.append(self)          
        print(f"users_Пользователь {self.username} успешно создан.")
#
    @staticmethod
    def hash_password(password):
        #генерируем соль и хешируем пароль с помощью bcrypt
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed
#
    @staticmethod
    def verify_password(stored_password, provided_password):
        """
        Метод для проверки пароля пользователя.
        :param stored_password: Хешированный пароль, сохраненный в базе данных.
        :param provided_password: Пароль, введенный пользователем при входе.
        :return: True, если пароли совпадают, иначе False.
        """
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)
#
    def get_details(self):
        """
        Метод для получения деталей пользователя.
        Должен быть переопределен в производных классах.
        """
        raise NotImplementedError("Метод get_details должен быть переопределен в производных классах.")
#
class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address
#
    def get_details(self):
        """
        Метод для получения деталей клиента.
        :return: Строка с деталями клиента.
        вывод хеш_пароля для демонстрации (после отладки нужно убрать)
        """
        return f"Клиент: {self.username}, Email: {self.email}, Адрес: {self.address}, хеш_Пароля: {self.password}"
#
class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level
#
    def get_details(self):
        return f"Сотрудник: {self.username}, Email: {self.email}, Admin-Level: {self.admin_level}, хеш_Пароля: {self.password}"
#
    @staticmethod
    def get_all_users():
        """
        Статический метод для получения списка всех пользователей.
        """
        return [user.get_details() for user in User.users]
#
    @staticmethod
    def delete_user(username):
        for user in User.users:
            if user.users==username:
                User.users.remove(user)
            return None
        
        