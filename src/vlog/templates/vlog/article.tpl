{% extends "core/base.tpl" %}
{% import "core/macros.tpl" as macro %}

{% block breadcrumbs %}
{{ macro.breadcrumbs(crumbs, _(article.title)) }}
{% endblock %}

{% block title %}{{ article.title }}{% endblock %}

{% block content %}
    <h1>{{ article.title }}</h1>
    <br>
    <h2>{{ article.content|safe }}</h2>
{% endblock %}