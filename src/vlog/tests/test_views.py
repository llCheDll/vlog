from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase, Client
from vlog import models
from vlog import forms


class SimpleTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='user')
        self.user.set_password('qwerty123')
        self.user.save()

        self.client = Client()
        self.client.login(username='user', password='qwerty123')

    def test_IndexView(self):
        response = self.client.get(reverse('vlog:index'))
        self.assertEqual(response.status_code, 200)

    def test_CategoriesView(self):
        response = self.client.get(reverse('vlog:categories'))
        self.assertEqual(response.status_code, 200)

    def test_CategoryView(self):
        category = forms.CategoryForm({'title': 'спорт', 'author': self.user.pk}).save()

        response = self.client.get(reverse('vlog:category', kwargs={'category_title': category.slug}))
        self.assertEqual(response.status_code, 200)

    def test_ArticlesView(self):
        category = forms.CategoryForm({'title': 'спорт', 'author': self.user.pk}).save()

        response = self.client.get(reverse('vlog:articles', kwargs={'category_title': category.slug}))
        self.assertEqual(response.status_code, 200)

    def test_ArticleView(self):
        category = forms.CategoryForm({'title': 'спорт', 'author': self.user.pk}).save()

        response = self.client.get(reverse('vlog:article', kwargs={
                                                                    'category_title': 'sport',
                                                                    'article_title': 'sport-eto-zlo'
                                                                    }))
        self.assertEqual(response.status_code, 200)
