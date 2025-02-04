import urllib.request
import json
import re
import difflib
from django.http import JsonResponse, HttpRequest
from .clients import DogCEOClient


client = DogCEOClient()
VALID_BREEDS = client.list_all_breeds()['message'].keys()


def list_all_breeds(request: HttpRequest) -> JsonResponse:
    data = client.list_all_breeds()
    return JsonResponse(data)


def list_breed_images(request: HttpRequest, breed: str) -> JsonResponse:
    if breed not in VALID_BREEDS:
        closest_matches = difflib.get_close_matches(breed, VALID_BREEDS, n=1)
        if closest_matches:
            closest_match = closest_matches[0]
            return JsonResponse({'error': f'Did you mean: {closest_match}?'}, status=400)
        else:
            return JsonResponse({'error': 'Breed not found and no close matches available.'}, status=400)

    data = client.list_breed_images(breed)
    return JsonResponse(data)


def random_dog_image(request: HttpRequest) -> JsonResponse:
    data = client.random_dog_image()
    return JsonResponse(data)


def breed_images_from_random(request: HttpRequest) -> JsonResponse:
    random_image_data = client.random_dog_image()

    image_url = random_image_data['message']
    match = re.search(r'breeds/([^/]+)/', image_url)
    if not match:
        return JsonResponse({'error': 'Breed not found in image URL'}, status=400)

    breed = match.group(1)
    breed_images_data = client.list_breed_images(breed)

    return JsonResponse(breed_images_data)
