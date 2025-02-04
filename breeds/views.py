from django.http import JsonResponse, HttpRequest
from .services import DogService

service = DogService()


def list_all_breeds(request: HttpRequest) -> JsonResponse:
    data = service.list_all_breeds()
    return JsonResponse(data)


def list_breed_images(request: HttpRequest, breed: str) -> JsonResponse:
    data, status = service.list_breed_images(breed)
    return JsonResponse(data, status=status)


def random_dog_image(request: HttpRequest) -> JsonResponse:
    data = service.random_dog_image()
    return JsonResponse(data)


def breed_images_from_random(request: HttpRequest) -> JsonResponse:
    data, status = service.breed_images_from_random()
    return JsonResponse(data, status=status)
