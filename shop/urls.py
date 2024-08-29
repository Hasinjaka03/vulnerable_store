from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.article_list, name='article_list'),
    path('article/create/', views.article_create, name='article_create'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
]
