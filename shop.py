#
from classesP.users import Customer, Admin
from classesP.autent import AuthenticationService
import sys
sys.stdout.reconfigure(encoding='utf-8')  # Настройка кодировки вывода для корректного отображения русских символов
print(f'globals: {globals()["AuthenticationService"]}')
print(f'globals: {globals()['Admin']}')
print(f'globals: {globals()["Customer"]}')
# имеющиеся пользователи
# Создаем несколько пользователей для демонстрации работы сервиса аутентификации
# (в реальном приложении пользователи обычно загружаются из базы данных)
customer = Customer(username="Максим", email="mmm@blgroup.by", password = "qwerty12345", address="Минск, ул. Ленина, 1")
admin = Admin(username="админ_1", email="root@v.ru",password = "12345qwerty", admin_level=5)
customer2 = Customer(username="Вася", email="aaa@jhf.bu", password = "12345qwerty$", address="Минск, ул. Октябрьская, 2")
#
#print(f'globals: {globals()["AuthenticationService","User","Customer","Admin"]}')
#print(f'globals: {globals()['Admin']}')
# Выводим список всех пользователей
print("Список всех пользователей:")
print(Admin.get_all_users()) # Выводим список всех пользователей
#
# Регистрация нового пользователя через сервис аутентификации
auth_service_inst = AuthenticationService() # Создаем экземпляр сервиса аутентификации -сессия
# Регистрация нового пользователя
#auth_service = auth_service_inst.register(user_class="Customer", username="Василий", email="jhf@by", password="0986667qwerty", address="Минск, ул. Советская, 3")
auth_service = auth_service_inst.register(user_class="Admin",username="Жора_fadmin",email="hgf5@8j22h.by", password="098777qwerty", admin_level=4)
#
#print(auth_service)
#
# Выводим список всех пользователей после регистрации нового пользователя
print("Список всех пользователей после регистрации нового пользователя:")
print(Admin.get_all_users()) # Выводим список всех пользователей
#
# вывести список открытых сессий
AuthenticationService.show_sessions()
#    print("Нет открытых сессий.")
#else:
#    print(f'открытые сессии: {AuthenticationService.show_sessions()}')