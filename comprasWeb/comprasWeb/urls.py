
from django.contrib import admin
from django.urls import path, include
# from home.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls','home'))),
    # path('inicio/', inicio, name='inicio')
]
