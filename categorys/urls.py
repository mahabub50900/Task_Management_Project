from django.urls import path
from . import views 
urlpatterns = [
    path('adds/category_page/',views.add_category, name = 'add_category'),
]
