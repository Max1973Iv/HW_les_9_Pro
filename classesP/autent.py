'''Класс - сервис управления регистрацией и аутентификацией пользователей
   Сервис аутентификации, который позволяет регистрировать пользователей и управлять сессиями.
   Содержит методы для создания сессий, регистрации пользователей и отображения ?? сессий.
   Сессии хранятся в статическом списке, что позволяет отслеживать ?? сессии.
   При регистрации пользователя проверяется корректность введенных данных и создается экземпляр соответствующего класса пользователя.
   Сервис поддерживает два класса пользователей: Customer и Admin.'''
from datetime import datetime
class AuthenticationService:
    # список созданных сессий
    sessions = []
    #
    def __init__(self,username=None,start_time=None,fin_time=None,status_session='active_ses'):
        self.username = username # имя пользователя
        self.start_time = start_time # время начала сессии
        self.fin_time = fin_time # время окончания сессии
        self.start_time = self.x_time()+"_st" # устанавливаем время начала сессии
        self.status_session = status_session # статус сессии
        # Добавляем текущую сессию в список открытых сессий
        AuthenticationService.sessions.append(self)
        print(f"aut_Сессия создана и начата в: {self.start_time}")
        """
        Инициализация сервиса аутентификации. экземпляр класса - сессия.
        Сессия содержит информацию о пользователе, времени начала сессии и статусе сессии.
        status_session может быть 'error_ses' (сессия завершенная после ошибки регистрации или аутентификации)'active_ses' (активная) или 'completed_ses' (завершенная).
        По числу error-сессий идущих подряд можно отслеживать поведение пользователя, который несколько раз
        делал попытки регистрации с неверными данными.
        """
    def __del__(self):
        print(f"aut_сессия пользователя: {self.username} завершена в {self.fin_time} статус {self.status_session}")
        """ Метод для удаления сессии
        Вызывается при удалении экземпляра класса AuthenticationService.
        выводится время окончания сессии и статус сессии.
        """
#        
    @classmethod
    def show_sessions(cls):
        """
        Метод для отображения всех сессий в статическом списке sessions.
        Если список пуст, выводит сообщение об отсутствии открытых сессий.
        """
        if not cls.sessions:
            print("aut_sh_Нет открытых сессий.")
        else:
            print("aut_sh_Созданные сессии:")
            for session in cls.sessions:
                print(f"aut_sh_Сессия {session.status_session} пользователя '{session.username}' начата в {session.start_time} завершена в {session.fin_time}")# if session.fin_time else 'еще не завершена'}")
#    
#
    def x_time(self):
        """ Возвращает дату и время события сессии
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#        
# регистрация нового пользователя:
    def register(self,user_class:str, username: str, email: str, password: str,**kwargs):
        '''
        Метод для регистрации нового пользователя.
        :param user_class: Класс пользователя (Customer или Admin)
        :param username: Имя пользователя.
        :param email: Email пользователя.
        :param password: Пароль пользователя.
        :param kwargs: Дополнительные аргументы для создания пользователя (например, адрес для Customer).
        :return: Кортеж (успех, пользователь), где успех - булево значение, указывающее на успешность регистрации,
        а пользователь - созданный экземпляр класса User  или None в случае ошибки.
        после регистрации устанавливается время окончания сессии и статус сессии.
        сессия может быть завершена с ошибкой или успешно завершена.
        '''
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
                #self.fin_time = self.x_time()  # устанавливаем время окончания сессии
                self.status_session = 'error_ses'  # устанавливаем статус сессии как 'error_ses'
                return False, None
            #
        except ValueError as ee:
            print(f"Ошибка регистрации: {ee}")
            #self.fin_time = self.x_time()  # устанавливаем время окончания сессии
            self.status_session = 'error_ses'  # устанавливаем статус сессии как 'error_ses'
            return False, None
#
        print(f"aut_значение user_class {user_class}")
        if user_class == "Customer":
            from classesP.users import Customer
            try:
                user_new = Customer(username=username, email=email, password=password, **kwargs)
                #self.fin_time = self.x_time()  # устанавливаем время окончания сессии
                self.status_session = 'completed_ses'  # устанавливаем статус сессии как 'completed_ses'
                return True, user_new
            except ValueError as ae:
                print(f"aut_Ошибка создания пользователя: {ae}")
                #self.fin_time = self.x_time()  # устанавливаем время окончания сессии
                self.status_session = 'error_ses'  # устанавливаем статус сессии как 'error_ses'
                return False, None
        if user_class == "Admin":
            from classesP.users import Admin
            try:
                user_new = Admin(username=username, email=email, password=password, **kwargs)
                #elf.fin_time = self.x_time()  # устанавливаем время окончания сессии
                self.status_session = 'completed_ses'  # устанавливаем статус сессии как 'completed_ses'
                # Возвращаем успешный результат регистрации и созданного пользователя
                return True, user_new
            except ValueError as be:
                print(f"aut_Ошибка создания пользователя: {be}")
                #self.fin_time = self.x_time()  # устанавливаем время окончания сессии
                self.status_session = 'error_ses'  # устанавливаем статус сессии как 'error_ses'
                return False, None
# проверяем статус сессии и закрываем сессию
# если статус сессии 'error_ses', то сессия завершена с ошибкой
# в ином случае сессия завершена успешно - меняем статус на 'completed_ses'
    def close_session(self):
        """ Метод для закрытия сессии
        проверяем статус сессии и закрываем сессию
        если статус сессии 'error_ses', то сессия завершена с ошибкой
        в ином случае сессия завершена успешно - меняем статус на 'completed_ses'
        """
        if self.status_session=='error_ses':
            print(f"aut_Ошибка регистрации,сессия завершена с ошибкой:")
            self.fin_time = self.x_time()+"_fin"
        else:
            self.status_session = 'completed_ses'
            print(f"aut_Сессия завершена успешно.")
            self.fin_time = self.x_time()+"_fin"
        del self # удаляем экземпляр класса
        #print(f"aut_Сессия удалена.")