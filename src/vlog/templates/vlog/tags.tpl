{% extends "core/base.tpl" %}

{% block title %} Tags {% endblock %}

{% block breadcrumbs %}
    <li class="breadcrumb-item"><a href="/">Главная </a></li>
    <li class="breadcrumb-item active">Теги </li>
{% endblock %}

{% block content %}
    <h1>Топ-3</h1>
    <br>
    {% for article in articles %}
        <h3><a href="../categories/{{ article.category__slug }}/articles/{{ article.slug }}/">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}
    <h1>Теги</h1>
    <br>
    {% for tag in tags %}
        <h3><a href="{{ tag.tag__slug }}">{{ tag.tag__title }}</a></h3>
        <hr>
    {% endfor %}


{% endblock %}