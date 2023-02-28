### Настроить в settings.py ###
- ALLOWED_HOSTS = []
- безопасность пароля к БД настроить

### Настроить в DRF ###


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