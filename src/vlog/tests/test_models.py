from django.contrib.auth import get_user_model
from django.test import TestCase

from vlog.models import *


class ModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='user')
        self.user.set_password('qwerty123')
        self.user.save()

        self.article = Article.objects.create(title='Тест', slug='test', author=self.user)

    def test_publication_representation(self):
        public = Publication(title="Тестовая публикация")
        self.assertEqual(str(public), public.title)

    def test_comments_representation(self):
        comment = Comment(author=self.user, article=self.article, text='Тест текст')
        self.assertEqual(str(comment), f'{self.user.username} [{self.article.title}]')
