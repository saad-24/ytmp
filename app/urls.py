from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('admin/', admin, name='admin'),
    path('', home, name='index'),
    path('convert/', converter, name='converter'),
    path('blogs/', blogs, name='blogs'),
    path('contact/', contact, name='contact'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
    path('blogs/', blogs, name='blogs'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail')
]