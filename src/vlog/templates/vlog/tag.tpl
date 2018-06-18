{% extends "core/base.tpl" %}

{% block title %}{{ tag.title }}{% endblock %}

{% block breadcrumbs %}
    <li class="breadcrumb-item"><a href="/">Главная </a></li>
    <li class="breadcrumb-item"><a href="/tags/"> Теги </a></li>
    <li class="breadcrumb-item active">{{ tag.title }} </li>
{% endblock %}

{% block content %}
    <h1>{{ tag.title }}</h1>

    {% for article in articles %}
        <h3><a href="../../categories/{{ article.category_title }}/articles/{{ article.slug }}/">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}

{% endblock %}