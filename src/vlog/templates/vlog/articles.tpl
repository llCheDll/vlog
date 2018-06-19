{% extends "core/base.tpl" %}

{% block breadcrumbs %}
    <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }} </a></li>
    <li class="breadcrumb-item"><a href="{{ url('vlog:categories') }}">{{ _('Categories') }} </a></li>
    <li class="breadcrumb-item"><a href="{{ url('vlog:category', category.slug) }}">{{ category.title }}</a></li>
    <li class="breadcrumb-item active">{{ _('Articles') }} </li>
{% endblock %}

{% block title %}{{ category.title }}{% endblock %}

{% block content %}
    <h1>{{ _('Articles') }}</h1>
    <br>
    {% for article in articles %}
        <h3><a href="{{ url('vlog:article', category.slug, article.slug) }}">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}
{% endblock %}