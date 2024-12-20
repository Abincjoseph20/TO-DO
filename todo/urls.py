# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('create', views.create, name='create'),
    path('list', views.list, name='list'),
    path('todo/details/<int:pk>/', views.details, name='details'),
    path('todo/<int:pk>/update/', views.update, name='update'),
    path('todo/<int:pk>/delete/', views.delete, name='delete'),
    
    path('', views.Registration.as_view(), name="registration"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm, next_page='create'), name='login'),
    path('logout/', views.loggout, name='logout'),  
]
