
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
# from home.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include(('home.urls','home'))),
    path('', include('users.urls'), name='users')
    # path('login/', LoginView.as_view(template_name='users/usuario/inicio.html'), name="login"),
    # path('', include('users.urls'), name="users")
]
