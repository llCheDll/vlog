from django.urls import re_path

from vlog import views

urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),

    re_path(
        r'^categories/$',
        views.CategoriesView.as_view(),
        name='categories'
    ),

    re_path(
        r'^categories/(?P<category_title>[\w-]+)/$',
        views.CategoryView.as_view(),
        name='category'
    ),

    re_path(
        r'^categories/(?P<category_title>[\w-]+)/articles/$',
        views.ArticlesView.as_view(),
        name='articles'
    ),

    re_path(
        r'^categories/(?P<category_title>[\w-]+)/articles/(?P<article_title>[\w-]+)/$',
        views.ArticleView.as_view(),
        name='article',
    ),

    re_path(
        r'^tags/$',
        views.TagsView.as_view(),
        name='tags'
    ),

    re_path(
        r'^tags/(?P<tag_title>[\w-]+)$',
        views.TagView.as_view(),
        name='tag'
    )
]