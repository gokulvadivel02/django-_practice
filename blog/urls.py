from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name='index'),
    path("post/<str:slug>", views.post, name='post'),
    path("change_new_url", views.new_url_view, name='new_page_url'),
    path("old_url", views.old_url, name='old_url'),
] 