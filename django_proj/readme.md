### Запуск программы и загрузка данных
1. ``git clone https://github.com/viktorr1975/notebook.git`` *result*
2. ``cd `` *result*
3. ``git checkout``
4. ``python3 -m venv`` *venv*
5. ``source venv/bin/activate``
6. ``cd django_proj/``
4. ``pip install -r requirements.txt``
5. Создать базу данных в Postgresql
6. В файле settings.py проекта django установить настройки базы данных, наподобие:
````
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_db",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "",
        "TEST": {
            "NAME": "mytestdatabase",
        },
    }
}
````
7. ``python manage.py migrate``
8. ``python manage.py loaddata dump.json``
9. ``python manage.py runserver``
10. Зайти на сайт http://127.0.0.1:8000 с учётной записью администратора или пользователя. Учётные записи логин/пароль:  
- admin/admin
- user1/user1
- user2/user2
### Особенности 
- в url отсутствуют trailing slashes
##### Django
1. Страницы пользователя:
- работа с категориями:
``` html
/
```
- работа к заметками в категории:
``` html
category/<int:group_id>
```
- работа с тэгами заметки:
``` html
note/<int:note_id>
```
- работа с тэгами пользователя:
``` html
tags
```
2. Безопасность
- Доступ к View только аутентифицированным пользователям
- Из БД данные выбираются для View с фильтрацией по пользователю, который указан в сессии
3. Логирование  
 Настроено логиирование модуля django.server. Отображаются запросы с уровня INFO, WARNING, ERROR, CRITICAL в консоль. В логе отображаетс время, результаты запроса и параметры запроса.

#### Django REST Framework ####
1. Безопасность
- Включаю аутентификацию, чтобы к API был доступ только после ввода логина/пароль
- Использую rest_framework.authentication.SessionAuthentication, т.к. это встроенное в Django решение
- Custom permissions использую для ограничения доступа пользователя к записям в БД при редактировании и Detaied View. Т.к. при запросах ListView разграничение доступа к объектам не отрабатывает, использую во ViewSet фильтр по пользователю в queryset.
2. API  
Описание в файле openapi.yaml

#### Тестирование ####
1. Команда запуска тестов:
``` sh
python manage.py test --settings "django_proj.settings" myapp.tests
```
2. Из 6 тестов 5 должно выполнятьса успешно, один - ошибочный, для проверки работоспособности тестирования.
Тестируется в DRF:
- отсутствие доступа GET к странице "/api/notes" неавторизованного пользователя
- наличия доступа GET к странице "/api/notes" авторизованного пользователя и выдача в запросе заметок только данного пользователя
Тестируется в Django:
- наличие доступа к странице "/" авторизованного пользователя
- отсутствие доступа к странице "/" неавторизованного пользователя и перенаправление на страницу авторизации
- отсутствие доступа к странице "category/<int:group_id>" неавторизованного пользователя и перенаправление на страницу авторизации  


