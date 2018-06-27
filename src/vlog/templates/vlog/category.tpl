{% extends "core/base.tpl" %}
{% import "core/macros.tpl" as macro %}

{% block breadcrumbs %}
{{ macro.breadcrumbs(crumbs, category.title )}}
{% endblock %}

{% block title %}{{ category.title }}{% endblock %}

{% block content %}
    <h1>{{ category.title }}</h1>
    <h2>{{ _('Popular articles') }}</h2>
    <br>
    {% for article in articles[:2] %}
        <h3><a href="{{ url('vlog:article', category.slug, article.slug) }}">{{ article.title }}</a></h3>
            <h5>{{ article.description }}</h5>
        <hr>
    {% endfor %}
    <h1><a href="{{ url('vlog:articles', category.slug) }}">{{ _('Articles') }}</a></h1>
    <br>
    {% for article in articles %}
        <h3><a href="{{ url('vlog:article', category.slug, article.slug) }}">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}
{% endblock %}