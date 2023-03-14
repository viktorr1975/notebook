### Настроить в settings.py ###
- ALLOWED_HOSTS = []
Если вас заботит именно вопрос безопасности запросов к вашему приложению - рекомендую рассмотреть две вещи
  - настройка разрешенных хостов для запросоа на сайт обслуживаемый django через ALLOWED_HOSTS - https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts
  - инструмент django-cors-headers ограничивающий источники запросов в ваше приложение (может пригодиться если django у вас выступает только как бэкэнд а фронт в другом приложении) - https://pypi.org/project/django-cors-headers/
- безопасность пароля к БД настроить
This can be done easily with the Python package Python Decouple. 
https://ordinarycoders.com/blog/article/django-beginners-guide

### Настроить в Django ###
не сделано:
- удаление категорий
- удаление заметок
- редактирование категорий
- редактирование заметок
- работа с тэгами
- должна быть группа для заметок без группы
[Easy Tags Input Component For Bootstrap 5/4 – Tags.js](https://www.cssscript.com/tags-input-bootstrap-5/)
+ https://codepen.io/dannibla/pen/QGLyBW
+ https://bootstrap-tagsinput.github.io/bootstrap-tagsinput/examples/
[bootstrap 5 tags input with jquery, bootstrap 5 tags input with Tagify(tag.js)](https://larainfo.com/blogs/bootstrap-5-tags-input-examples)
[lekoala /bootstrap5-tags ](https://github.com/lekoala/bootstrap5-tags)
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
- NotesSerializer.validate_tags(), для этотого:
  - проверить отсутствие доступа POST http://0.0.0.0:8000/api/notes для анонима
  - проверить наличие доступа POST http://0.0.0.0:8000/api/notes для авторизованного пользователя
  - невозможность сохранить запись с чужой группой POST http://0.0.0.0:8000/api/notes
  - невозможность сохранить запись с чужим тэгом POST http://0.0.0.0:8000/api/notes

py .\manage.py dumpdata <app_name>.<ModelName>  # выгрузка дамп данных из ДБ

py .\manage.py loaddata <path_to_fixture_file>  # загрузка в базу данных
там джсон создается сам и при переопределение в сетингах ДБ на другую, данные подгружаюся
но надо все модели мигрировать сначала, прежде чем их дампом даных загружать
[Fixture loading](https://docs.djangoproject.com/en/4.1/topics/testing/tools/#fixture-loading)