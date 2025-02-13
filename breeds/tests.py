from django.test import TestCase, Client
from django.urls import reverse


class TestDogServiceIntegration(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_all_breeds(self):
        response = self.client.get(reverse('list_all_breeds'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 'success')
        self.assertIn('breeds', response.json()['data'])

    def test_list_breed_images(self):
        response = self.client.get(reverse('list_breed_images', args=['weimaraner']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 'success')
        self.assertIn('urls', response.json()['data'])
        self.assertTrue(response.json()['data']['urls'] != [])

    def test_list_breed_images_sub_breed(self):
        response = self.client.get(reverse('list_breed_images', args=['hound-basset']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 'success')
        self.assertIn('urls', response.json()['data'])
        self.assertTrue(response.json()['data']['urls'] != [])

    def test_list_breed_images_invalid_breed(self):
        response = self.client.get(reverse('list_breed_images', args=['invalid-breed']))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['result'], 'error')
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'Breed not found and no close matches available.')

    def test_list_breed_images_close_match(self):
        response = self.client.get(reverse('list_breed_images', args=['weimarane']))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['result'], 'error')
        self.assertIn('message', response.json())
        self.assertIn('Did you mean', response.json()['message'])

    def test_random_dog_image(self):
        response = self.client.get(reverse('random_dog_image'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('url', response.json()['data'])
        self.assertIn('breed', response.json()['data'])
        self.assertEqual(response.json()['result'], 'success')

    def test_breed_images_from_random(self):
        response = self.client.get(reverse('breed_images_from_random'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('urls', response.json()['data'])
        self.assertEqual(response.json()['result'], 'success')
