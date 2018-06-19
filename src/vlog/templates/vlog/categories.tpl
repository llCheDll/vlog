{% extends "core/base.tpl" %}

{% block breadcrumbs %}
    <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
    <li class="breadcrumb-item active">{{ _('Categories') }}</li>
{% endblock %}

{% block title %}_('Categories'){% endblock %}

{% block content %}
    <h1>{{ _('Categories') }}</h1>
    <br>
    {% for category in categories %}
        <h2><a href="{{ url('vlog:category', category.slug ) }}">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}

    <div class="pagination">
        <span class="step-links">
            {% if categories.has_previous %}
                <a href="?page=1">&laquo; first</a>
                <a href="?page={{ categories.previous_page_number }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ categories.number }} of {{ categories.paginator.num_pages }}.
            </span>

            {% if categories.has_next %}
                <a href="?page={{ categories.next_page_number }}">next</a>
                <a href="?page={{ categories.paginator.num_pages }}">last &raquo;</a>
            {% endif %}
        </span>
    </div>

{% endblock %}