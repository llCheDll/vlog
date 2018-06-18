{% extends "core/base.tpl" %}

{% block breadcrumbs %}
    <li class="breadcrumb-item"><a href="/">Главная </a></li>
    <li class="breadcrumb-item active">Категории </li>
{% endblock %}

{% block title %}Категории{% endblock %}

{% block content %}
    <h1>Категории</h1>
    <br>
    {% for category in categories %}
        <h2><a href="{{ category.slug }}">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}