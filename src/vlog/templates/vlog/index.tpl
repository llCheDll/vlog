{% extends 'core/base.tpl' %}

{% block breadcrumbs %}
    <li class="breadcrumb-item active">{{ _('Home') }} </li>
{% endblock %}

{% block title %}Index{% endblock %}

{% block content %}
    <h1>{{ _('Popular categories') }}</h1>
    <br>
    {% for category in categories %}
        <h2><a href="{{ url('vlog:category', category.slug) }}">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}
    <h1>{{ _('Most commented articles') }}</h1>
    <br>
    {% for article in articles %}
        <h2><a href="{{ url('vlog:article', article.category__slug, article.slug) }}">{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
    <h1>{{ _('Most populated tags') }}</h1>
    <br>
    {% for tag in tags %}
        <h2><a href="{{ url('vlog:tags') }}">{{ tag.tag__title }}</a></h2>
        <hr>
    {% endfor %}

{% endblock %}