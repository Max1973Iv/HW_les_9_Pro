# Класс - сервис управления регистрацией и аутентификацией пользователей
from datetime import datetime
class AuthenticationService:
    def __init__(self):#,user_class:str, username: str, email: str, password: str,*args):
        print(f'сессия начата:время начала сессии: {self.x_time()}')
    #
    #
        #
        """
        Инициализация сервиса аутентификации. экземпляр класса - сессия.
        :param user_class: Класс пользователя (Customer или Admin)
        :param username: Имя пользователя.
        :param email: Email пользователя.
        :param password: Пароль пользователя.
        :param args: Дополнительные аргументы для создания пользователя.
        """
#        if user_class not in ['Customer', 'Admin']:
#            raise ValueError("Неверный класс пользователя. Доступны только 'Customer' и 'Admin'.")
        #if not username or not email or not password:
        #    raise ValueError("Имя пользователя, email и пароль не могут быть пустыми.")
#
#        self.user_class = user_class
#        self.username = username
#        self.email = email
#        self.password = password
#        self.args = args
    def x_time(self):
        """ Возвращает дату и время события.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#        
# регистрация нового пользователя:
#    @staticmethod
    def register(self,user_class:str, username: str, email: str, password: str,**kwargs):
        self.user_class = user_class
        self.username = username
        self.email = email
        self.password = password
        self.args = kwargs
        try:
            if user_class not in ['Customer', 'Admin']:
                raise ValueError("Неверный класс пользователя. Доступны только 'Customer' и 'Admin'.")
            #
            try:
                if not username or not email or not password:
                    raise ValueError("Имя пользователя, email и пароль не могут быть пустыми.")
            except ValueError as e:
                print(f"Ошибка регистрации: {e}")
                return False, None
            #
        except ValueError as e:
            print(f"Ошибка регистрации: {e}")
            return False, None
#
        print(f"aut_значение user_class {user_class}")
        if user_class == "Customer":
            from classesP.users import Customer
            try:
                user_new = Customer(username=username, email=email, password=password, **kwargs)
                return True, user_new
            except ValueError as e:
                print(f"aut_Ошибка создания пользователя: {e}")
                return False, None
        if user_class == "Admin":
            from classesP.users import Admin
            try:
                user_new = Admin(username=username, email=email, password=password, **kwargs)
#
#                if  user_new == None:
#                    raise ValueError("aut_Ошибка создания пользователя.")
#                raise ValueError("aut_Ошибка создания пользователя.")
                return True, user_new
            except ValueError as e:
                print(f"aut_Ошибка создания пользователя: {e}")
                return False, None
#        print(f'globals: {globals()['Admin']}')
        #from classes.users import Customer, Admin
#        user_cl = globals()[user_class]  # Получаем ссылку на класс пользователя по имени
        #
        # Создаем нового пользователя
        #print(f"Регистрация нового пользователя: {user_cl} с именем {username}, email {email}, пароль {password}")
        #print("значение user_class",user_cl)
#        user_new = user_cl(username=username, email=email, password=password, **kwargs)#создаем экземпляр класса пользователя
        #print(f"Пользователь {user_new.username} успешно зарегистрирован.")
        #return True, user_new
        #