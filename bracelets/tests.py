from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Bracelet


class CollectionFilterVisibilityTests(TestCase):
    def setUp(self):
        self.user, _ = get_user_model().objects.get_or_create(username='admin')
        self.user.set_password('secret-pass-123')
        self.user.save()
        Bracelet.objects.create(
            name='Amethyst Harmony',
            description='Polished crystal bracelet',
            price='1299.00',
            material='Amethyst',
            color='Purple',
            size='Medium',
            stock=12,
        )

    def assert_filter_is_visible(self, response):
        self.assertContains(response, 'class="col-12 col-lg-3 mb-4 filter-sidebar"')
        self.assertContains(response, 'id="filterForm"')

    def test_collection_keeps_filter_for_anonymous_users(self):
        response = self.client.get(reverse('bracelets_list'))

        self.assertEqual(response.status_code, 200)
        self.assert_filter_is_visible(response)

    def test_login_redirect_keeps_user_on_collection_with_filter(self):
        response = self.client.post(reverse('login_admin'), {
            'username': 'admin',
            'password': 'secret-pass-123',
        }, follow=True)

        self.assertRedirects(response, reverse('bracelets_list'))
        self.assert_filter_is_visible(response)

    def test_logout_returns_to_collection_with_filter(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('logout_admin'), follow=True)

        self.assertRedirects(response, reverse('bracelets_list'))
        self.assert_filter_is_visible(response)


class BraceletApiTests(APITestCase):
    def test_api_can_create_bracelet_rows(self):
        response = self.client.post('/api/bracelets/', {
            'name': 'Green Aventurine',
            'description': 'Fresh crystal bracelet',
            'price': '899.00',
            'material': 'Aventurine',
            'color': 'Green',
            'size': 'Medium',
            'stock': 5,
        }, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Bracelet.objects.filter(name='Green Aventurine').exists())


class CartTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='customer',
            password='secret-pass-123',
        )
        self.bracelet = Bracelet.objects.create(
            name='Rose Quartz Glow',
            description='Soft pink crystal bracelet',
            price='999.00',
            material='Rose Quartz',
            color='Pink',
            size='Medium',
            stock=8,
        )

    def test_logged_in_user_can_add_to_cart(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('add_to_cart', args=[self.bracelet.pk]))

        self.assertRedirects(response, reverse('cart'))
        self.assertEqual(self.user.cart_items.count(), 1)
        self.assertEqual(self.user.cart_items.first().bracelet, self.bracelet)
