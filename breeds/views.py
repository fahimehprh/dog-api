import urllib.request
import json
import re
import difflib
from django.http import JsonResponse, HttpRequest


def list_all_breeds(request: HttpRequest) -> JsonResponse:
    url = 'https://dog.ceo/api/breeds/list/all'

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    return JsonResponse(data)


VALID_BREEDS_URL = 'https://dog.ceo/api/breeds/list/all'


def get_valid_breeds():
    with urllib.request.urlopen(VALID_BREEDS_URL) as response:
        data = json.loads(response.read().decode())
    return list(data['message'].keys())


VALID_BREEDS = get_valid_breeds()


def list_breed_images(request: HttpRequest, breed: str) -> JsonResponse:

    if breed not in VALID_BREEDS:
        closest_matches = difflib.get_close_matches(breed, VALID_BREEDS, n=1)
        if closest_matches:
            closest_match = closest_matches[0]
            return JsonResponse({'error': f'Did you mean: {closest_match}?'}, status=400)
        else:
            return JsonResponse({'error': 'Breed not found and no close matches available.'}, status=400)

    url = f'https://dog.ceo/api/breed/{breed}/images'

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    return JsonResponse(data)


def random_dog_image(request: HttpRequest) -> JsonResponse:
    url = 'https://dog.ceo/api/breeds/image/random'

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    return JsonResponse(data)


def breed_images_from_random(request: HttpRequest) -> JsonResponse:

    random_image_response = random_dog_image(request)
    random_image_data = json.loads(random_image_response.content)

    image_url = random_image_data['message']
    match = re.search(r'breeds/([^/]+)/', image_url)
    if not match:
        return JsonResponse({'error': 'Breed not found in image URL'}, status=400)

    breed = match.group(1)

    breed_images_response = list_breed_images(request, breed)
    breed_images_data = json.loads(breed_images_response.content)

    return JsonResponse(breed_images_data)
