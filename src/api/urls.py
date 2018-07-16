from django.conf.urls import re_path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoriesViewSet)
router.register(r'articles', views.ArticlesViewSet)
router.register(r'tags', views.ArticlesViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]