{% extends "core/base.tpl" %}
{% import "core/macros.tpl" as macro%}

{% block title %} Tags {% endblock %}

{% block breadcrumbs %}
{{ macro.breadcrumbs(crumbs, active = _('Tags')) }}
{% endblock %}

{% block content %}
    <h1>Топ-3</h1>
    <br>
    {% for article in articles %}
        <h3><a href="{{ url('vlog:article', article.category.slug, article.slug) }}">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}
    <h1>Теги</h1>
    <br>
    {% for tag in tags %}
        <h3><a href="{{ tag.slug }}">{{ tag.title }}</a></h3>
        <hr>
    {% endfor %}


{% endblock %}