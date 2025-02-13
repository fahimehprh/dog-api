# Django Dog Breeds Project

This Django project provides APIs to interact with [the Dog CEO API](https://dog.ceo/dog-api/). It includes endpoints to list all dog breeds, retrieve images of a specific breed, get a random dog image, and more.

## Requirements

- Python 3.9
- Django 4.2

## How to Run and Test

### Running the Project

1. **Clone the repository**:
    ```bash
    git clone git@github.com:fahimehprh/dog-api.git
    cd dog-api
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Django development server**:
    ```bash
    python manage.py runserver
    ```

### Running Tests

 ```bash
 python manage.py test
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
