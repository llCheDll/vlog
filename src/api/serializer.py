from vlog.models import *
from rest_framework import serializers


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'created', 'updated')


class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'slug', 'description', 'content', 'author_id', 'category_id')


class TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', 'slug', 'articles_id')
