import urllib.request
import json
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
