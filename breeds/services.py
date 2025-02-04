import difflib
import re
from .clients import DogCEOClient


class DogService:
    def __init__(self):
        self.client = DogCEOClient()
        self.valid_breeds = self.client.list_all_breeds()['message'].keys()

    def list_all_breeds(self):
        return self.client.list_all_breeds()

    def list_breed_images(self, breed: str):
        if breed not in self.valid_breeds:
            closest_matches = difflib.get_close_matches(breed, self.valid_breeds, n=1)
            if closest_matches:
                closest_match = closest_matches[0]
                return {'error': f'Did you mean: {closest_match}?'}, 400
            else:
                return {'error': 'Breed not found and no close matches available.'}, 400

        return self.client.list_breed_images(breed), 200

    def random_dog_image(self):
        return self.client.random_dog_image()

    def breed_images_from_random(self):
        random_image_data = self.client.random_dog_image()

        image_url = random_image_data['message']
        match = re.search(r'breeds/([^/]+)/', image_url)
        if not match:
            return {'error': 'Breed not found in image URL'}, 400

        breed = match.group(1)
        return self.client.list_breed_images(breed), 200
