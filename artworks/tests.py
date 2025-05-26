from django.contrib.auth.models import User
from .models import Artwork
from rest_framework import status
from rest_framework.test import APITestCase


class ArtworkListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username="adam", password="pass")

    def test_can_list_artworks(self):
        adam = User.objects.get(username="adam")
        Artwork.objects.create(
            owner=adam,
            title="A Masterpiece",
            description="Amazing abstract art.",
            image_filter_choices="hudson"
        )
        response = self.client.get("/artworks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_artwork(self):
        self.client.login(username="adam", password="pass")
        response = self.client.post(
            "/artworks/",
            {
                "title": "A Masterpiece",
                "description": "Colorful shapes",
                "image_filter_choices": "normal"
            }
        )
        count = Artwork.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_artwork(self):
        response = self.client.post(
            "/artworks/",
            {
                "title": "A Masterpiece",
                "description": "Colorful shapes",
                "image_filter_choices": "normal"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ArtworkDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username="adam", password="pass")
        brian = User.objects.create_user(username="brian", password="pass")
        Artwork.objects.create(
            owner=adam,
            title="Adam's Art",
            description="Blue on blue",
            image_filter_choices="earlybird"
        )
        Artwork.objects.create(
            owner=brian,
            title="Brian's Art",
            description="Red explosion",
            image_filter_choices="toaster"
        )

    def test_can_retrieve_artwork_using_valid_id(self):
        response = self.client.get("/artworks/1/")
        self.assertEqual(response.data["title"], "Adam's Art")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_artwork_using_invalid_id(self):
        response = self.client.get("/artworks/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_artwork(self):
        self.client.login(username="adam", password="pass")
        response = self.client.put(
            "/artworks/1/",
            {
                "title": "Updated Title",
                "description": "Updated description",
                "image_filter_choices": "valencia"
            }
        )
        artwork = Artwork.objects.get(pk=1)
        self.assertEqual(artwork.title, "Updated Title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_artwork(self):
        self.client.login(username="adam", password="pass")
        response = self.client.put(
            "/artworks/2/",
            {
                "title": "Hacked Title",
                "description": "Oops",
                "image_filter_choices": "kelvin"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
