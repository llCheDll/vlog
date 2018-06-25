{% extends "core/base.tpl" %}
{% import "core/macros.tpl" as macro %}

{% block breadcrumbs %}
{{ macro.breadcrumbs(crumbs, _('Categories'))}}
{% endblock %}

{% block title %}{{_('Categories') }}{% endblock %}

{% block content %}
    <h1>{{ _('Categories') }}</h1>
    <br>
    {% for category in categories %}
        <h2><a href="{{ url('vlog:category', category.slug ) }}">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}

    <nav aria-label="Category navigation">
      <ul class="pagination">
          {% for page in categories.paginator.page_range %}
            <li class="page-item"><a class="page-link" href="?page={{ page }}">{{ page }}</a></li>
          {% endfor %}
      </ul>
    </nav>

{% endblock %}