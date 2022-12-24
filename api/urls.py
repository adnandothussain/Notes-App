from django.urls import path
from . import views

urlpatterns = [
    # path('', getRoutes, name='routes')
    path('notes/create/', views.createNote, name='create_note'),
    path('notes/update/<str:pk>', views.updateNote, name='update_note'),
    path('notes/delete/<str:pk>', views.deleteNote, name='delete_note'),
    path('notes/', views.getNotes, name='notes'),
    path('notes/<str:pk>/', views.getNote, name='note'),
]
