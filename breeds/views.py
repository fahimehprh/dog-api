from django.http import HttpRequest

from .api import api, APIJSONResponse
from .services import DogService

service = DogService()


@api
def list_all_breeds(request: HttpRequest):
    return APIJSONResponse(service.list_all_breeds())


@api
def list_breed_images(request: HttpRequest, breed: str):
    return APIJSONResponse(service.list_breed_images(breed))


@api
def random_dog_image(request: HttpRequest):
    return APIJSONResponse(service.random_dog_image())


@api
def breed_images_from_random(request: HttpRequest):
    return APIJSONResponse(service.breed_images_from_random())
