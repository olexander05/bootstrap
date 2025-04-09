from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_note, name='create_note'),
    path('login/', views.login_view, name='login'),
    path('notes/', views.note_list, name='note_list'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
]
