import urllib.request
import json


class DogCEOClient:
    BASE_URL = 'https://dog.ceo/api/'

    def _fetch_data(self, endpoint: str):
        url = f'{self.BASE_URL}{endpoint}'
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())

    def list_all_breeds(self):
        return self._fetch_data('breeds/list/all')

    def list_breed_images(self, breed: str):
        return self._fetch_data(f'breed/{breed}/images')

    def random_dog_image(self):
        return self._fetch_data('breeds/image/random')
