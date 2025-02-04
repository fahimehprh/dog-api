import urllib.request
import json
import re
from django.http import JsonResponse, HttpRequest


def list_all_breeds(request: HttpRequest) -> JsonResponse:
    url = 'https://dog.ceo/api/breeds/list/all'

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    return JsonResponse(data)


def list_breed_images(request: HttpRequest, breed: str) -> JsonResponse:
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


