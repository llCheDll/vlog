from core.views import BaseView
from django.db.models import Count
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse
from django.utils.translation import gettext as _

from vlog.models import *


class IndexView(BaseView):
    template_name = 'vlog/index.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.annotate(populate=Count('articles')).order_by('-populate')[:3]

        articles = Article.objects.all()[:10]

        import ipdb
        ipdb.set_trace()

        tags = Tag.articles.through.objects.select_related('tag')\
                           .values('tag__title',
                                   'tag__slug')\
                           .annotate(counter=Count('article_id'))\
                           .order_by('-counter')[:10]

        context.update({
            'articles': articles,
            'categories': categories,
            'tags': tags
                        })

        return self.render_to_response(context)


class CategoriesView(BaseView):
    template_name = 'vlog/categories.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        categories_list = Category.objects.annotate(num=Count('articles__category_id')).order_by('-num')

        paginator = Paginator(categories_list, 2)

        page = self.request.GET.get('page')

        categories = paginator.get_page(page)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')}
        ]

        context.update({
            'categories': categories,
            'crumbs': crumbs,
        })

        return self.render_to_response(context)


class CategoryView(BaseView):
    template_name = 'vlog/category.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.get(slug=kwargs.get('category_title'))

        articles = Article.objects\
            .filter(category_id=category.id)

        articles_filter = articles[:2]

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')}
        ]

        context.update({
            'articles': articles,
            'articles_filter': articles_filter,
            'category': category,
            'crumbs': crumbs,
        })

        return self.render_to_response(context)


class ArticlesView(BaseView):
    template_name = 'vlog/articles.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.get(slug=kwargs.get('category_title'))
        articles = Article.objects\
            .filter(category_id=category.id)\
            .values('title',
                    'slug',
                    'description',
                    'category__slug',
                    'comments__article_id') \
            .annotate(counter=Count('comments__article_id')) \
            .order_by('-counter')\

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')},
            {'url': reverse('vlog:category', category.slug)}
        ]

        context.update({
            'category': category,
            'articles': articles,
            'crumbs': crumbs,
        })

        return self.render_to_response(context)


class ArticleView(BaseView):
    template_name = 'vlog/article.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        article = Article.objects\
            .filter(slug=kwargs.get('article_title'))\
            .values('title',
                    'content',
                    'category__title',
                    'category__slug')\
            .first()

        context.update({
            'article': article,
        })

        return self.render_to_response(context)


class TagsView(BaseView):
    template_name = 'vlog/tags.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tags = Tag.articles.through.objects\
            .select_related('tag')\
            .values('tag__title',
                    'tag__slug')\
            .annotate(counter=Count('article_id'))\
            .order_by('-counter')

        articles = Article.objects.all()\
            .values('title',
                    'slug',
                    'category__slug',
                    'comments__article_id') \
            .annotate(counter=Count('comments__article_id')) \
            .order_by('-counter')[:3] \

        context.update({
            'tags': tags,
            'articles': articles
        })

        return self.render_to_response(context)


class TagView(BaseView):
    template_name = 'vlog/tag.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = Tag.objects.filter(slug=kwargs.get('tag_title')).values('id',)

        context.update({
            'tag': tag,
        })

        return self.render_to_response(context)