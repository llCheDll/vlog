{% extends "core/base.tpl" %}
{% import "core/macros.tpl" as macro %}

{% block title %}{{ tag.title }}{% endblock %}

{% block breadcrumbs %}
{{ macro.breadcrumbs(crumbs, active = tag.title) }}
{% endblock %}

{% block content %}
    <h1>{{ tag.title }}</h1>

    {% for article in articles %}
        <h3><a href="{{ url('vlog:article', article.category.slug, article.slug) }}">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}

{% endblock %}