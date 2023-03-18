# from rest_framework.test import APITestCase
from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from mixer.backend.django import mixer

from .models import Notes, Tags

# Create your tests here.
# https://testdriven.io/blog/django-custom-user-model/


# class UsersManagersTests(TestCase):
#
#     def test_create_user(self):
#         User = get_user_model()
#         user = User.objects.create_user(username="user1", email="normal@user.com", password="foo")
#         self.assertEqual(user.email, "normal@user.com")
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(TypeError):
#             User.objects.create_user()
#         with self.assertRaises(TypeError):
#             User.objects.create_user(email="")
#         with self.assertRaises(ValueError):
#             User.objects.create_user(email="", password="foo")
#
#     def test_create_superuser(self):
#         User = get_user_model()
#         admin_user = User.objects.create_superuser(username="admin", email="super@user.com", password="foo")
#         self.assertEqual(admin_user.email, "super@user.com")
#         self.assertTrue(admin_user.is_active)
#         self.assertTrue(admin_user.is_staff)
#         self.assertTrue(admin_user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(admin_user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(ValueError):
#             User.objects.create_superuser(
#                 email="super@user.com", password="foo", is_superuser=False)


class DRFTestCase(APITestCase):
    def setUp(self):
        #         User = get_user_model()
        #         user = User(username="user1", email='user1@email.com', password='user1')
        #         user.save()

        # создадим пользователя 'user21' с двумя заметками и тэгом к этим заметкам
        self.user21 = get_user_model().objects.create_user(
            username="user21", email="user21@email.com", password="user21"
        )
        # self.tag_user21 = Tag.create("user21 tag1")
        self.tag_user21 = Tags.objects.create(author_id=self.user21, name="user21 tag1")
        notes21 = mixer.cycle(2).blend(
            "myapp.Notes",
            author_id=self.user21,
            content=("user21 note"),
            title="title 21",
            tags=self.tag_user21
            #            tags__name=("user21 tag{1}")
            #            tags__name=mixer.sequence("user21 tag{1}")
        )
        # создадим пользователя 'user20' с одной заметкой
        self.user20 = get_user_model().objects.create_user(
            username="user20", email="user20@email.com", password="user20"
        )
        notes20 = mixer.cycle(1).blend(
            "myapp.Notes",
            author_id=self.user20,
            content=mixer.sequence("user20 note"),
            title="title 20",
        )

    def test_anonymous_cannot_see_page(
        self,
    ):  # проверяме отсутствие доступа GET к странице "/api/notes" неавторизованного пользователя
        response = self.client.get(reverse("notesapp:notes-list"))
        self.assertEqual(401, response.status_code)  # Unauthorized

    def test_authenticated_user_can_see_page_home(
        self,
    ):  # проверяме наличия доступа GET к странице "/api/notes" авторизованного пользователя
        # self.client.login(username='fred', password='secret')  #test client will have all the cookies and session data
        self.client.force_login(
            user=self.user20
        )  # test requires a user be logged in and the details of how a user logged in aren’t important
        #        print("resolved name:", resolve("/api/notes").url_name)
        url = reverse("notesapp:notes-list")
        response = self.client.get(
            url,
            content_type="application/json",
        )
        resp_json = response.json()
        self.assertEqual(response.status_code, 200)  # запрос выполнен успешно
        self.assertEqual(
            1, resp_json["count"]
        )  # в запросе предоставлена только единственная запись пользователя user20
        self.client.logout()


# https://python-scripts.com/create-blog-django#blog-views
class NotesTests(TestCase):
    # @classmethod
    # def setUpTestData(self):   #is run    once
    #     from django.core.wsgi import get_wsgi_application
    #     application = get_wsgi_application()                # устранение ошибки django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.
    def setUp(self):
        # # Before performing any tests, record the existing
        # # user IDs:
        # # 1. So we know which users we created during the test
        # # 2. So we can remove just those fake users.
        # print('setUp()')
        # # Get the list of all users before the tests.
        # # Must evaluate the QuerySet or it will be lazily-evaluated later, which is wrong.
        # self.users_before = list(get_user_model().objects.values_list('id', flat=True).order_by('id'))
        # print(self.users_before)

        # создадим пользователя 'user20' с одной заметкой
        self.user20 = get_user_model().objects.create_user(
            username="user20", email="user20@email.com", password="user20"
        )

    def test_fake_test(self):
        self.assertEqual(False, True)  # проверка работоспособности

    def test_authenticated_user_can_see_page_home(
        self,
    ):  # проверяме наличие доступа к странице "/" авторизованного пользователя
        # self.client.login(username='fred', password='secret')  #test client will have all the cookies and session data
        self.client.force_login(
            user=self.user20
        )  # test requires a user be logged in and the details of how a user logged in aren’t important
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Nice body content')
        #        self.assertTemplateUsed(response, '_index.html')
        #     self.assertEqual(no_response.status_code, 404)
        self.client.logout()

    def test_anonymous_cannot_see_page_home(
        self,
    ):  # проверяме отсутствие доступа к странице "/" неавторизованного пользователя
        # url = reverse('home')
        # print("Resolve : ", resolve(url))
        response = self.client.get(reverse("home"))
        self.assertRedirects(response, "/accounts/login/?next=/")

    def test_anonymous_cannot_see_page_detail(
        self,
    ):  # проверяме отсутствие доступа к странице "category/<int:group_id>" неавторизованного пользователя
        response = self.client.get(
            reverse("detail", args=[1])
        )  # значение args в этом тесте роли не играет
        print(response)
        self.assertRedirects(response, "/accounts/login/?next=/category/1")

    # @classmethod
    # def tearDown(self):
    #     print('tearDown()')
    #     users_after = get_user_model().objects.values('id', 'username', 'password', 'user_notes', 'user_tags')
    #     notes = Notes.objects.values('id', 'title', 'content',  'author_id_id',  'group_id_id')
    #     tags = Tags.objects.values('id', 'name', 'author_id_id')
    #     # Get the list of all users after the tests.
    #     #users_after = list(get_user_model().objects.values_list('id', flat=True).order_by('id'))
    #     #print(users_after)
    #     # print(notes)
    #     # print(tags)
    #     # # Calculate the set difference.
    #     # users_to_remove = sorted(list(set(users_after) - set(self.users_before)))
    #     # print(users_to_remove)
    #     # # Delete that difference from the database.
    #     # get_user_model().objects.filter(id__in=users_to_remove).delete()
