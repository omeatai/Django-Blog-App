from django.urls import path
from .views import (article_list, article_details, user_login, register,
                    article_form, update_article, delete_article)
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView,
                                       PasswordChangeDoneView)

urlpatterns = [
    path('', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    path('add/', article_form, name='article_form'),
    path('update/<slug:slug>/', update_article, name='update_article'),
    path('delete/<slug:slug>/', delete_article, name='delete_article'),
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
