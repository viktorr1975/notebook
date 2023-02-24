### Настроить в settings.py ###
- ALLOWED_HOSTS = []
- безопасность пароля к БД настроить
### set up a custom user model ###
models.py:
create a custom user model
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    
settings.py
AUTH_USER_MODEL = 'feedapp.User'

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### [create users programmatically](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#creating_users_and_groups) ###
rom django.contrib.auth.models import User

# Create user and save to the database
user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
user.first_name = 'Tyrone'
user.last_name = 'Citizen'
user.save()