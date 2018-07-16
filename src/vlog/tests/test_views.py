from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase, Client
from vlog import views


class ViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='user')
        self.user.set_password('qwerty123')
        self.user.save()

        self.client = Client()
        self.client.login(username='user', password='qwerty123')

        views.Category.objects.create(slug='sport', author=self.user)
        views.Article.objects.create(
            slug='test',
            category=views.Category.objects.get(slug='sport'),
            author=self.user
        )
        views.Tag.objects.create(slug='ololo')

    def test_IndexView(self):
        response = self.client.get(reverse('vlog:index'))
        self.assertEqual(response.status_code, 200)
        
        context = response.context_data
        
        self.assertTrue('articles' in context)
        self.assertTrue('categories' in context)
        self.assertTrue('tags' in context)

    def test_CategoriesView(self):
        response = self.client.get(reverse('vlog:categories'))
        self.assertEqual(response.status_code, 200)
        
        context = response.context_data
        
        self.assertTrue('categories' in context)
        self.assertTrue('crumbs' in context)

    def test_CategoryView(self):
        category = views.Category.objects.get(slug='sport')

        response = self.client.get(reverse('vlog:category', kwargs={'category_title': category.slug}))
        self.assertEqual(response.status_code, 200)
        
        context = response.context_data
        
        self.assertTrue('articles' in context)
        self.assertTrue('category' in context)
        self.assertTrue('crumbs' in context)
        self.assertEqual(category.slug, 'sport')

    def test_ArticlesView(self):
        category = views.Category.objects.get(slug='sport')

        response = self.client.get(reverse('vlog:articles', kwargs={'category_title': category.slug}))
        self.assertEqual(response.status_code, 200)
        
        context = response.context_data
        
        self.assertTrue('articles' in context)
        self.assertTrue('category' in context)
        self.assertTrue('crumbs' in context)
        self.assertEqual(category.slug, 'sport')
        

    def test_ArticleView(self):
        category = views.Category.objects.get(slug='sport')
        article = views.Article.objects.get(slug='test')

        response = self.client.get(reverse('vlog:article', kwargs={
            'category_title': category.slug,
            'article_title': article.slug
        }))
        self.assertEqual(response.status_code, 200)
        
        context = response.context_data
        
        self.assertTrue('article' in context)
        self.assertTrue('crumbs' in context)
        self.assertEqual(article.slug, 'test')
        self.assertEqual(category.slug, 'sport')
        

    def test_TagsView(self):
        response = self.client.get(reverse('vlog:tags'))
        self.assertEqual(response.status_code, 200)
        
        context = response.context_data
        
        self.assertTrue('articles' in context)
        self.assertTrue('tags' in context)
        self.assertTrue('crumbs' in context)

    def test_TagView(self):
        tag = views.Tag.objects.get(slug='ololo')

        response = self.client.get(reverse('vlog:tag', kwargs={'tag_title': tag.slug}))
        self.assertEqual(response.status_code, 200)
        
        context = response.context_data
        
        self.assertTrue('articles' in context)
        self.assertTrue('tag' in context)
        self.assertTrue('crumbs' in context)
        self.assertEqual(tag.slug, 'ololo')
