import random

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate, APITestCase
from .views import AuthorModelViewSet
from .models import Author, Bio
from django.contrib.auth.models import User
from mixer.backend.django import mixer


class TestAuthorApi(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='denis', password='qwerty')
        self.author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_1(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors')
        force_authenticate(request, self.user)
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class TestAuthorApiClient(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='denis', password='qwerty')
        self.author = mixer.blend(Author, birthday_year=mixer.sequence(lambda c: random.random() * 100))
        self.bio = mixer.blend(Bio, author__birthday_year=2000)

    def test_get_list(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_1(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_list_bio(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/bios/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        # print(response.data)

    def test_get_list_2(self):
        self.client.login(username='denis', password='qwerty')
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.client.logout()
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_author(self):
        self.client.login(username='denis', password='qwerty')
        response = self.client.post('/api/authors/', data={
            'first_name': 'Александр',
            'last_name': 'Грин',
            'birthday_year': 1860
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        author = Author.objects.get(pk=response.data.get('id'))
        self.assertEqual(author.last_name, 'Грин')

