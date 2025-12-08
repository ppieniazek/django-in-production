from django.urls import path
from . import views

urlpatterns = [
    path('author/create/', views.create_author, name='create_author'),
    path('author/', views.fetch_author, name='fetch_author'),
    path('author/delete/<int:id>/', views.delete_author, name='delete_author'),
    path('author/edit/<int:id>/', views.edit_author, name='edit_author'),
]