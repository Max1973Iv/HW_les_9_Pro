# Класс - сервис управления регистрацией и аутентификацией пользователей
from datetime import datetime
class AuthenticationService:
    # список созданных сессий
    sessions = []
    #
    def __init__(self):
        #
        AuthenticationService.sessions.append(self) # Добавляем сессию в список открытых сессий
        print(f"aut_Сессия {self.x_time()} начата.")
        """
        Инициализация сервиса аутентификации. экземпляр класса - сессия.
        """
#
#    def __del__(self):
#        print(f'сессия завершена:время окончания сессии: {self.x_time()}')
#
    def x_time(self):
        """ Возвращает дату и время события.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#        
# регистрация нового пользователя:
    def register(self,user_class:str, username: str, email: str, password: str,**kwargs):
        self.user_class = user_class # класс пользователя
        self.username = username # имя пользователя
        self.email = email # email пользователя
        self.password = password # пароль пользователя
        # Дополнительные аргументы для создания пользователя
        self.kwargs = kwargs
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
        except ValueError as ee:
            print(f"Ошибка регистрации: {ee}")
            return False, None
#
        print(f"aut_значение user_class {user_class}")
        if user_class == "Customer":
            from classesP.users import Customer
            try:
                user_new = Customer(username=username, email=email, password=password, **kwargs)
                return True, user_new
            except ValueError as ae:
                print(f"aut_Ошибка создания пользователя: {ae}")
                return False, None
        if user_class == "Admin":
            from classesP.users import Admin
            try:
                user_new = Admin(username=username, email=email, password=password, **kwargs)
                return True, user_new
            except ValueError as be:
                print(f"aut_Ошибка создания пользователя: {be}")
                return False, None
#
        #