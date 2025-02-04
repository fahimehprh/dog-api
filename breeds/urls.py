from django.urls import path
from .views import list_all_breeds, list_breed_images

urlpatterns = [
    path('list/', list_all_breeds, name='list_all_breeds'),
    path('<str:breed>/images/', list_breed_images, name='list_breed_images'),
]