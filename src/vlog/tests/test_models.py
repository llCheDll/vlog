from django.contrib.auth import get_user_model
from django.test import TestCase

from vlog.models import *


class ModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='user')
        self.user.set_password('qwerty123')
        self.user.save()

        self.category = Category.objects.create(
            title='Спорт',
            slug='sport',
            author=self.user
        )
        
        self.article = Article.objects.create(
            title='Тест',
            slug='test',
            author=self.user,
            category=self.category
        )
        
        self.comment = Comment.objects.create(
            author=self.user,
            article=self.article,
            text='Полезный комент'
        )
        
        self.tag = Tag.objects.create(title='Тееег', slug='teeg')
        
        self.article.tags.add(self.tag)
        self.article.comments.add(self.comment)

    def test_publication_representation(self):
        public = Publication(title="Тестовая публикация")
        self.assertEqual(str(public), public.title)
        self.assertEqual(public.title, "Тестовая публикация")
        
    def test_comments_representation(self):
        self.assertEqual(str(self.comment), f'{self.user.username} [{self.article.title}]')
        
    def test_category(self):
        self.assertIsInstance(self.category, Category)
        self.assertEqual(self.category.title, 'Спорт')
        self.assertEqual(self.category.slug, 'sport')
        self.assertEqual(self.category.author.username, 'user')
        
    def test_article(self):
        self.assertIsInstance(self.article, Article)
        self.assertEqual(self.article.title, 'Тест')
        self.assertEqual(self.article.slug, 'test')
        self.assertEqual(self.article.author.username, 'user')
        self.assertEqual(self.article.category.title, 'Спорт')
        
    def test_comment(self):
        self.assertEqual(str(self.comment), 'user [Тест]')
        self.assertIsInstance(self.comment, Comment)
        self.assertEqual(self.comment.article.title, 'Тест')
        self.assertEqual(self.comment.author, self.user)
        self.assertEqual(self.comment.text, 'Полезный комент')
        
    def test_tag(self):
        self.assertIsInstance(self.tag, Tag)
        self.assertEqual(self.tag.articles.get().title, 'Тест')
