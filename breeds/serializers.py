from abc import ABC, abstractmethod
from .models import DogImage, BreedImages, BreedList


class Serializer(ABC):
    @abstractmethod
    def serialize(self):
        pass


class BreedImageListSerializer(Serializer):
    def __init__(self, instance: BreedImages):
        self.instance = instance

    def serialize(self):
        return {
            'urls': self.instance.urls,
        }


class RandomImageSerializer(Serializer):
    def __init__(self, instance: DogImage):
        self.instance = instance

    def serialize(self):
        return {
            'url': self.instance.url,
            'breed': self.instance.breed
        }


class BreedListSerializer(Serializer):
    def __init__(self, instance: BreedList):
        self.instance = instance

    def serialize(self):
        return {
            'breeds': self.instance.breeds
        }
