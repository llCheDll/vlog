{% extends "core/base.tpl" %}

{% block breadcrumbs %}
    <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
    <li class="breadcrumb-item active">{{ _('Categories') }}</li>
{% endblock %}

{% block title %}{{_('Categories') }}{% endblock %}

{% block content %}
    <h1>{{ _('Categories') }}</h1>
    <br>
    {% for category in categories %}
        <h2><a href="{{ url('vlog:category', category.slug ) }}">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}

    <nav aria-label="Page navigation example">
      <ul class="pagination">
          {% for page in categories.paginator.page_range %}
            <li class="page-item"><a class="page-link" href="?page={{ page }}">{{ page }}</a></li>
          {% endfor %}
      </ul>
    </nav>

{% endblock %}