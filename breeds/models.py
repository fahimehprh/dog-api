class BreedList:
    def __init__(self, breeds: list[str]):
        if breeds is None:
            breeds = []
        self.breeds = breeds


class DogImage:
    def __init__(self, url: str, breed: str):
        self.url = url
        self.breed = breed


class BreedImages:
    def __init__(self, urls: list[str]):
        if urls is None:
            urls = []
        self.urls = urls
