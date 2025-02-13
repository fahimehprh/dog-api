import difflib

from .clients import DogCEOClient
from .errors import ClientError, ServiceError
from .serializers import BreedImageListSerializer, BreedListSerializer, RandomImageSerializer


class ServiceErrors:
    INTERNAL = ServiceError('Internal error occurred. Please try again later.')
    NOT_FOUND = ServiceError('Breed not found.')


class DogService:
    def __init__(self):
        self.client = DogCEOClient()
        self.valid_breeds = self.client.list_all_breeds().breeds

    def _get_breed_images_or_error(self, breed: str):
        try:
            if '-' in breed:
                breed_images = self.client.list_sub_breed_images(*breed.split('-'))
            else:
                breed_images = self.client.list_breed_images(breed)
        except ClientError:
            raise ServiceErrors.INTERNAL
        if breed_images is None:
            raise ServiceErrors.INTERNAL
        return breed_images

    def _get_random_image_or_error(self):
        try:
            random_image = self.client.random_image()
        except ClientError:
            raise ServiceErrors.INTERNAL
        if random_image is None:
            raise ServiceErrors.NOT_FOUND

        return random_image

    def list_all_breeds(self) -> BreedListSerializer:
        try:
            breed_list = self.client.list_all_breeds()
        except ClientError:
            raise ServiceErrors.INTERNAL

        return BreedListSerializer(instance=breed_list)

    def list_breed_images(self, breed: str):
        if breed not in self.valid_breeds:
            closest_matches = difflib.get_close_matches(breed, self.valid_breeds, n=1)
            if closest_matches:
                closest_match = closest_matches[0]
                raise ServiceError(f'Did you mean: {closest_match}?')
            else:
                raise ServiceError('Breed not found and no close matches available.')

        breed_images = self._get_breed_images_or_error(breed)
        return BreedImageListSerializer(instance=breed_images)

    def random_dog_image(self):
        random_image = self._get_random_image_or_error()
        return RandomImageSerializer(instance=random_image)

    def breed_images_from_random(self):
        random_image = self._get_random_image_or_error()
        breed = random_image.breed

        breed_images = self._get_breed_images_or_error(breed)
        return BreedImageListSerializer(instance=breed_images)
