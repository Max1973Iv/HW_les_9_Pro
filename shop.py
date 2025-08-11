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
## Регистрация нового пользователя через сервис аутентификации
auth_service_inst = AuthenticationService()
# Регистрация нового пользователя
#
auth_service = auth_service_inst.register(user_class="Customer", username="Жужик", email="jhf@by", password="0986667qwerty", address="Минск, ул. Советская, 3")
#auth_service = auth_service_inst.register(user_class="Customer",username="Жора",email="hgf5@8jh.by", password="0987qwerty", address="Минск, ул. Советская, 3")
#print(f"Регистрация нового пользователя:{auth_service_inst.username} {auth_service}")
if auth_service[0]==True:
    print(f"shop_Пользователь {auth_service[1].username} успешно зарегистрирован.")
    print(f"shop_Детали нового пользователя: {auth_service[1].get_details()}")
else:
    print("shop_Регистрация не удалась.")
#print(f"Регистрация нового пользователя: {auth_service[0]}")
#print(f"Детали нового пользователя: {auth_service[1].get_details()}")
# Выводим список всех пользователей после регистрации нового пользователя
print("Список всех пользователей после регистрации нового пользователя:")
print(Admin.get_all_users()) # Выводим список всех пользователей
#print("Список всех пользователей2:")
#print(Admin.get_all_users()) # Выводим список всех пользователей
# время и дата создания
#print(f"Дата и время создания: {AuthenticationService.creation_time()}")