{% extends "core/base.tpl" %}

{% block breadcrumbs %}
    <li class="breadcrumb-item"><a href="/">Главная </a></li>
    <li class="breadcrumb-item"><a href="/categories/">Категории </a></li>
    <li class="breadcrumb-item"><a href="../../{{ category.slug }}">{{ category.title }}</a></li>
    <li class="breadcrumb-item active">Статьи </li>
{% endblock %}

{% block title %}{{ category.title }}{% endblock %}

{% block content %}
    <h1>Статьи</h1>
    <br>
    {% for article in articles %}
        <h3><a href="{{ article.slug }}/">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}
{% endblock %}