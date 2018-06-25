{% extends "core/base.tpl" %}
{% import "core/macros.tpl" as macro %}

{% block breadcrumbs %}
{{ macro.breadcrumbs(crumbs, _('Articles')) }}
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