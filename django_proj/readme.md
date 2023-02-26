### Описание архитектуры ###
#### Django REST Framework ####
1. Безопасность
- Включаю аутентификацию, чтобы к API был доступ только после ввода логина/пароль
- использую rest_framework.authentication.SessionAuthentication, т.к. это встроенное в Django решение
- custom permissions использую для ограничения доступа пользователя к записям в БД при редактировании и Detaied View. Т.к. при запросах ListView разграничение доступа к объектам не отрабатывает, использую во ViewSet фильтр по пользователю в queryset.
2. API

| API | Описание |
| ------ | ------ |
| `GET /api/tasks` | `получть список всех задач` |
| `GET /api/tasks/{id}` | `получть одну конкретную задачу` |
| `POST /api/tasks` | `создать задачу` |
| `GET /api/tasks` | `получть список всех задач` |
| `PUT (или PATCH) /api/tasks/{id}` | `отредактировать существующую задачу` |
| `DELETE /api/tasks/{id}` | `удалить одну задачу` |
Дополнительно в запросах можно использовать(!!!!!! не сделано !!!!!!!!!!):
-   фильтрацию для поиска задачи по заголовку (`запрос GET может быть дополнен query-параметром ?title=...`)
-   фильтрацию для поиска активных\неактривных задач (`запрос GET может быть дополнен query-параметром ?is_active=...`)
-   пагинацию при GET-запросе (`запрос GET может быть дополнен query-параметром ?limit=...&offset=...`)
-   упорядочение результата GET - запроса (`запрос GET может быть дополнен query-параметром ?ordering=...`)