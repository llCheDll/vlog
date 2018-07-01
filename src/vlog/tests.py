from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase, Client
from vlog import models
from vlog import forms


class TransliterationTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user', password='qwerty123'
        )

    def test_transliteration(self):
        cat_form = forms.CategoryForm(
            {'title': 'спорт', 'author': self.user.pk}
        )

        cat = None

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'sport')

        cat_form = forms.CategoryForm(
            {'title': 'тест'}, instance=cat
        )

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'test')

        cat_form = forms.CategoryForm(
            {'title': 'Breaking News! Новости.'}, instance=cat
        )

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'breaking-news-novosti')


class SimpleTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='user')
        self.user.set_password('qwerty123')
        self.user.save()

        self.client = Client()
        self.client.login(username='user', password='qwerty123')

    def test_index(self):
        response = self.client.get(reverse('vlog:categories'))
        self.assertEqual(response.status_code, 200)

        import ipdb
        ipdb.set_trace()

