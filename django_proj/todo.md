### Настроить в settings.py ###
- ALLOWED_HOSTS = []
Если вас заботит именно вопрос безопасности запросов к вашему приложению - рекомендую рассмотреть две вещи
  - настройка разрешенных хостов для запросоа на сайт обслуживаемый django через ALLOWED_HOSTS - https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts
  - инструмент django-cors-headers ограничивающий источники запросов в ваше приложение (может пригодиться если django у вас выступает только как бэкэнд а фронт в другом приложении) - https://pypi.org/project/django-cors-headers/
- безопасность пароля к БД настроить
This can be done easily with the Python package Python Decouple. 
https://ordinarycoders.com/blog/article/django-beginners-guide

### Настроить в Django ###
Добавить декоратор аутентифицированный пользователь только во view

### Настроить в DRF ###

### testing ###
- тестировать свой код, не тестировать чужой
- сделать позитивные тесты, проверяющие реализованный функционал
- охватить хотя бы 40% функций написанных
- можно негативные тексты на проверку отсутствия функционала, который должен отсутствовать
- делать тестирование сложных фукций, простые можно не тестировать
https://ilyachch.gitbook.io/django-rest-framework-russian-documentation/overview/navigaciya-po-api/testing
How to write tests in Django: Best practices for testing in Django
https://ordinarycoders.com/blog/article/django-testing
#### протестировать: ####
- NotesSerializer.validate_tags()


### [create users programmatically](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#creating_users_and_groups) ###
rom django.contrib.auth.models import User

# Create user and save to the database
user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
user.first_name = 'Tyrone'
user.last_name = 'Citizen'
user.save()

### Adding Log In To The Browsable API ###
https://docs.djangoproject.com/en/4.1/howto/logging/
[DRF.Adding login to the Browsable API](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#adding-login-to-the-browsable-api)