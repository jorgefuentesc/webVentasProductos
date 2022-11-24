from django.urls import path, include

from django.contrib.auth.decorators import login_required

from . import views

# from  django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    # path('', Inicio.as_view(), name ='inicio'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout')
    
]
