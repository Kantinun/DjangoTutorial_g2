from django.urls import path

from . import views

app_name = 'vocab'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vocab_id>/', views.detail , name='detail'),
    path('addPage/', views.addWordPage , name='addPage'),
    path('add/', views.addWord , name='add'),
    path('search/',views.search, name='search'),
]