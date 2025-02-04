# Django Dog Breeds Project

This Django project provides APIs to interact with [the Dog CEO API](https://dog.ceo/dog-api/). It includes endpoints to list all dog breeds, retrieve images of a specific breed, get a random dog image, and more.

## Requirements

- Python 3.x
- comming later

## Installation

1. comming later:
    ```bash
    comming later
    ```


## API Endpoints

### List All Breeds

- **URL**: `/breeds/list`
- **Method**: GET
- **Description**: Retrieves a list of all dog breeds available.

#### Example Request
```bash
GET http://127.0.0.1:8000/breeds/list
```

### List Images of a Specific Breed

- **URL**: `/breeds/{breed}/images`
- **Method**: GET
- **Description**: Retrieves a list of images of a specific dog breed.

#### Example Request
```bash
GET http://127.0.0.1:8000/breeds/weimaraner/images
```

### Get a Random Dog Image

- **URL**: `/breeds/random-image`
- **Method**: GET
- **Description**: Retrieves a random dog image.

#### Example Request
```bash
GET http://127.0.0.1:8000/breeds/random-image
```

### Get Images of the Breed from a Random Image

- **URL**: `/breeds/breed-images-from-random`
- **Method**: GET
- **Description**: Retrieves a random dog image, extracts the breed from the image URL, and lists all images of that breed.

#### Example Request
```bash
GET http://127.0.0.1:8000/breeds/breed-images-from-random
```
