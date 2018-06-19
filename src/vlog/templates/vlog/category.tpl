{% extends "core/base.tpl" %}

{% block breadcrumbs %}
    <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
    <li class="breadcrumb-item"><a href="{{ url('vlog:categories') }}">{{ _('Categories') }} </a></li>
    <li class="breadcrumb-item active">{{ category.title }} </li>
{% endblock %}

{% block title %}{{ category.title }}{% endblock %}

{% block content %}
    <h1>{{ category.title }}</h1>
    <h2>{{ _('Popular articles') }}</h2>
    <br>
    {% for article in articles_filter %}
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