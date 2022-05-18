# CRUD app on Flask
В данной работе были использованны библиотеки Flask,SQLAlchemy.\
Для запуска приложения необходимо установить библиотеки из списка, который находится в файле
requirements.txt. 
---
1)Создать виртуальное окружение в папке приложения 
(в терминале должен быть открыт репозиторий приложения) с помощью команды:
`virtualenv venv`\
2)Запустить виртуальное окружение командой:
`source venv/bin/activate`\
3)Установить все нужные библеотеки:
`pip install -r requirements.txt`.
----
Чтобы указать подключение к БД MeSQL, необходимо изменить значения в файлу app.py.
`app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Пользователь:Пароль@localhost/БД'`
Где необходимо написать имя пользователя вместо `Пользователь`,
пароль пользователя вместо `Пароль`,
адрес вашего сервера БД вместо `localhost` и название БД вместо `БД`.
----
 ## Запуск приложения можно осуществить, находясь в репозитории приложения и введя в консоль команду:
`python3 app.py`
## Чтобы открыть страницу приложения в браузере надо ввести:
`http://127.0.0.1:5000/`.
