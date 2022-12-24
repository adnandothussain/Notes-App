from django.urls import path
from . import views

urlpatterns = [
    # path('', getRoutes, name='routes')
    path('notes/', views.getNotes, name='notes'),
    path('notes/<str:pk>/', views.getNote, name='note'),
    path('notes/create/', views.createNote, name='note'),
    path('notes/delete/<str:pk>', views.deleteNote, name='note'),
]
