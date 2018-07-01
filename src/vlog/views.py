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

        categories = Category.objects.annotate(
                populate=Count('articles')
            ).order_by('-populate')[:3]

        articles = Article.objects.annotate(
                count=Count('comments')
            ).order_by('count')[:10]

        tags = Tag.objects.annotate(
                count=Count(Tag.articles.field.attname)
            ).order_by('-count')[:10]

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

        categories_list = Category.objects.annotate(
                num=Count('articles__category_id')
                ).order_by('-num')

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

        articles = Article.objects.filter(category_id=category.id)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')}
        ]

        context.update({
            'articles': articles,
            'category': category,
            'crumbs': crumbs,
        })

        return self.render_to_response(context)


class ArticlesView(BaseView):
    template_name = 'vlog/articles.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.get(slug=kwargs.get('category_title'))

        articles = Article.objects.filter(
                category_id=category.id
            )

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')},
            {'url': reverse(
                    'vlog:category', kwargs={'category_title': category.slug}
                    ), 'title': _(category.title)}
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

        article = Article.objects.get(
                slug=kwargs.get('article_title')
            )

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')},
            {'url': reverse(
                    'vlog:category', kwargs={'category_title': article.category.slug}
                    ), 'title': _(article.category.title)},
            {'url': reverse(
                    'vlog:articles', kwargs={'category_title': article.category.slug}
                    ), 'title': _('Articles')},
        ]

        context.update({
            'article': article,
            'crumbs': crumbs,
        })

        return self.render_to_response(context)


class TagsView(BaseView):
    template_name = 'vlog/tags.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tags = Tag.objects.annotate(
                count=Count(Tag.articles.field.attname)
            ).order_by('-count')

        articles = Article.objects.annotate(
                count=Count('comments')
            ).order_by('count')[:3]

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
        ]

        context.update({
            'articles': articles,
            'crumbs': crumbs,
            'tags': tags
        })

        return self.render_to_response(context)


class TagView(BaseView):
    template_name = 'vlog/tag.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = Tag.objects.filter(slug=kwargs.get('tag_title')).first()

        articles = Article.objects.filter(tags=tag)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:tags'), 'title': _('Tags')},
        ]

        context.update({
            'articles': articles,
            'crumbs': crumbs,
            'tag': tag,
        })

        return self.render_to_response(context)