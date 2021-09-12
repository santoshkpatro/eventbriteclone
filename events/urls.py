from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.event_add, name='event_add'),
    path('<int:event_id>/', views.event_details, name='event_details'),
    path('delete/<int:event_id>/', views.event_delete, name='event_delete'),
    path('like/<int:event_id>/', views.event_like, name='event_like'),
    path('like/remove/<int:event_id>/', views.event_like_remove, name='event_like_remove'),
]
