{% extends 'core/base.tpl' %}

{% block breadcrumbs %}
    <li class="breadcrumb-item active">Главная </li>
{% endblock %}

{% block title %}Index{% endblock %}

{% block content %}
    <h1>Популярные категории</h1>
    <br>
    {% for category in categories %}
        <h2><a href="categories/{{ category.slug }}/">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}
    <h1>Топ комментируемых</h1>
    <br>
    {% for article in articles %}
        <h2><a href="categories/{{ article.category__slug }}/articles/{{ article.slug }}/">{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
    <h1>Популярные теги</h1>
    <br>
    {% for tag in tags %}
        <h2><a href="tags/{{ tag.tag__slug }}">{{ tag.tag__title }}</a></h2>
        <hr>
    {% endfor %}

{% endblock %}