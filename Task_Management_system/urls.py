
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show, name='show_page'),
    path('task/',include('tasks.urls')),
    path('category/',include('categorys.urls')),
]
