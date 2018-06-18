{% extends "core/base.tpl" %}

{% block breadcrumbs %}
    <li class="breadcrumb-item"><a href="/">Главная </a></li>
    <li class="breadcrumb-item"><a href="/categories/">Категории </a></li>
    <li class="breadcrumb-item active">{{ category.title }} </li>
{% endblock %}

{% block title %}{{ category.title }}{% endblock %}

{% block content %}
    <h1>{{ category.title }}</h1>
    <h2>Популярные статьи</h2>
    <br>
    {% for article in articles_filter %}
        <h3><a href="articles/{{ article.slug }}/">{{ article.title }}</a></h3>
            <h5>{{ article.description }}</h5>
        <hr>
    {% endfor %}
    <h1><a href="articles/">Статьи</a></h1>
    <br>
    {% for article in articles %}
        <h3><a href="articles/{{ article.slug }}/">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}
{% endblock %}