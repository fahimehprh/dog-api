from django.urls import path
from .views import list_all_breeds, list_breed_images, random_dog_image, breed_images_from_random

urlpatterns = [
    path('list/', list_all_breeds, name='list_all_breeds'),
    path('<str:breed>/images/', list_breed_images, name='list_breed_images'),
    path('random-image/', random_dog_image, name='random_dog_image'),
    path('breed-images-from-random/', breed_images_from_random, name='breed_images_from_random'),
]
