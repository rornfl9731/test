from django.urls import path, include
from .views import photo_list,PhotoDetailView

urlpatterns = [
    path('',photo_list,name ='list'),
    path('detail/<int:pk>/',PhotoDetailView.as_view(),name='detail')
]