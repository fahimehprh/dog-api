import re
import urllib.request
import json

from .errors import ClientError
from .models import BreedImages, BreedList, DogImage


class DogCEOClient:
    BASE_URL = 'https://dog.ceo/api/'

    def _fetch_data(self, endpoint: str):
        url = f'{self.BASE_URL}{endpoint}'
        # TODO: retry and error handling
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())

    def list_all_breeds(self) -> BreedList:
        response = self._fetch_data('breeds/list/all')
        breeds = response.get('message')
        if not breeds:
            raise ClientError('Breeds not found in response')

        breeds_list = []
        for breed, sub_breeds in breeds.items():
            if sub_breeds:
                for sub_breed in sub_breeds:
                    breeds_list.append(f"{breed}-{sub_breed}")
            else:
                breeds_list.append(breed)

        return BreedList(breeds=breeds_list)

    def list_breed_images(self, breed: str) -> BreedImages:
        response = self._fetch_data(f'breed/{breed}/images')
        return BreedImages(urls=response.get('message'))

    def list_sub_breed_images(self, breed: str, sub_breed: str) -> BreedImages:
        response = self._fetch_data(f'breed/{breed}/{sub_breed}/images')
        return BreedImages(urls=response.get('message'))

    def random_image(self) -> DogImage:
        response = self._fetch_data('breeds/image/random')

        image_url = response.get('message')
        if not image_url:
            raise ClientError('Image URL not found in response')

        match = re.search(r'breeds/([^/]+)/', image_url)
        if not match:
            raise ClientError('Breed not found in image URL')

        breed = match.group(1)
        return DogImage(url=image_url, breed=breed)




