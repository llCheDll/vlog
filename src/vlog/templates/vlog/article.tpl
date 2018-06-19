{% extends "core/base.tpl" %}

{% block breadcrumbs %}
    <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }} </a></li>
    <li class="breadcrumb-item"><a href="{{ url('vlog:categories') }}">{{ _('Categories') }} </a></li>
    <li class="breadcrumb-item"><a href="../../../{{ article.category__slug }}">{{ article.category__title }}</a></li>
    <li class="breadcrumb-item"><a href="../../articles">{{ _('Articles') }} </a></li>
    <li class="breadcrumb-item active">{{ article.title }} </li>
{% endblock %}

{% block title %}{{ article.title }}{% endblock %}

{% block content %}
    <h1>{{ article.title }}</h1>
    <br>
    <h2>{{ article.content|safe }}</h2>
{% endblock %}