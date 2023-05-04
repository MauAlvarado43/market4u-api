"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json
from rest_framework import status
from rest_framework.test import APITestCase
from seed.util.test_util import fill_test_database
from rest_auth.models import TokenModel
from app.models import User

class TestRest(APITestCase):
    def setUp(self):
        fill_test_database()
        user = User.objects.all().first()
        token, created = TokenModel.objects.get_or_create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    
    def test_get_carts(self):
        response = self.client.get('/api/carts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_cart(self):
        response = self.client.get('/api/carts/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_cart(self):
        data = {
            "buyer_id":  1,
            "payment_id":  1,
        }
        response = self.client.post('/api/carts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_cart(self):
        data = {
            "buyer_id":  1,
            "payment_id":  1,
        }
        response = self.client.put('/api/carts/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_cart(self):
        response = self.client.delete('/api/carts/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_categories(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_category(self):
        response = self.client.get('/api/categories/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_category(self):
        data = {
            "name": "",
        }
        response = self.client.post('/api/categories/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_category(self):
        data = {
            "name": "",
        }
        response = self.client.put('/api/categories/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_category(self):
        response = self.client.delete('/api/categories/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_companies(self):
        response = self.client.get('/api/companies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_company(self):
        response = self.client.get('/api/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_company(self):
        data = {
            "name": "",
            "common_name": "",
            "rfc": "",
            "address": "",
            "phone": "",
            "email": "",
            "active": False,
            "photo_id": 1,
        }
        response = self.client.post('/api/companies/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_company(self):
        data = {
            "name": "",
            "common_name": "",
            "rfc": "",
            "address": "",
            "phone": "",
            "email": "",
            "active": False,
            "photo_id": 1,
        }
        response = self.client.put('/api/companies/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_company(self):
        response = self.client.delete('/api/companies/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_messages(self):
        response = self.client.get('/api/messages/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_message(self):
        response = self.client.get('/api/messages/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_message(self):
        data = {
            "content": "",
            "sender_id":  1,
            "target_id":  1,
        }
        response = self.client.post('/api/messages/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_message(self):
        data = {
            "content": "",
            "sender_id":  1,
            "target_id":  1,
        }
        response = self.client.put('/api/messages/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_message(self):
        response = self.client.delete('/api/messages/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_opinions(self):
        response = self.client.get('/api/opinions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_opinion(self):
        response = self.client.get('/api/opinions/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_opinion(self):
        data = {
            "title": "",
            "description": "",
            "rate": 128,
            "product_id":  1,
            "user_id":  1,
        }
        response = self.client.post('/api/opinions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_opinion(self):
        data = {
            "title": "",
            "description": "",
            "rate": 128,
            "product_id":  1,
            "user_id":  1,
        }
        response = self.client.put('/api/opinions/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_opinion(self):
        response = self.client.delete('/api/opinions/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_payments(self):
        response = self.client.get('/api/payments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_payment(self):
        response = self.client.get('/api/payments/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_payment(self):
        data = {
            "card_number": "",
            "expire_date": "",
            "type": "DEBIT",
            "user_id":  1,
            "address": "",
        }
        response = self.client.post('/api/payments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_payment(self):
        data = {
            "card_number": "",
            "expire_date": "",
            "type": "DEBIT",
            "user_id":  1,
            "address": "",
        }
        response = self.client.put('/api/payments/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_payment(self):
        response = self.client.delete('/api/payments/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_product(self):
        response = self.client.get('/api/products/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_product(self):
        data = {
            "name": "",
            "short_description": "",
            "description": "",
            "user_id":  1,
            "sales_id":  1,
            "category_id":  1,
        }
        response = self.client.post('/api/products/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_product(self):
        data = {
            "name": "",
            "short_description": "",
            "description": "",
            "user_id":  1,
            "sales_id":  1,
            "category_id":  1,
        }
        response = self.client.put('/api/products/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_product(self):
        response = self.client.delete('/api/products/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_purchases(self):
        response = self.client.get('/api/purchases/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_purchase(self):
        response = self.client.get('/api/purchases/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_purchase(self):
        data = {
            "amount": 128,
            "product": "{}",
            "sale": "{}",
            "shipping_id":  1,
        }
        response = self.client.post('/api/purchases/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_purchase(self):
        data = {
            "amount": 128,
            "product": "{}",
            "sale": "{}",
            "shipping_id":  1,
        }
        response = self.client.put('/api/purchases/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_purchase(self):
        response = self.client.delete('/api/purchases/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_sales(self):
        response = self.client.get('/api/sales/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_sale(self):
        response = self.client.get('/api/sales/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_sale(self):
        data = {
            "name": "",
            "disscount": 128.0,
            "start_date": "2020-01-01T12:00:00+00:00",
            "end_date": "2020-01-01T12:00:00+00:00",
            "user_id":  1,
            "banner_id": 1,
        }
        response = self.client.post('/api/sales/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_sale(self):
        data = {
            "name": "",
            "disscount": 128.0,
            "start_date": "2020-01-01T12:00:00+00:00",
            "end_date": "2020-01-01T12:00:00+00:00",
            "user_id":  1,
            "banner_id": 1,
        }
        response = self.client.put('/api/sales/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_sale(self):
        response = self.client.delete('/api/sales/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_shippings(self):
        response = self.client.get('/api/shippings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_shipping(self):
        response = self.client.get('/api/shippings/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_shipping(self):
        data = {
            "info": "",
            "folio": "",
            "address": "",
            "status": "CREATED",
            "seller_id":  1,
            "cart_id":  1,
        }
        response = self.client.post('/api/shippings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_shipping(self):
        data = {
            "info": "",
            "folio": "",
            "address": "",
            "status": "CREATED",
            "seller_id":  1,
            "cart_id":  1,
        }
        response = self.client.put('/api/shippings/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_shipping(self):
        response = self.client.delete('/api/shippings/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_user(self):
        response = self.client.get('/api/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_user(self):
        data = {
            "username": "email_1@test.com",
            "first_name": "FirstName",
            "last_name": "LastName",
            "email": "email_1@test.com",
            "password": "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
            "is_active": False,
            "address": "",
            "active": False,
            "type": "SUPERADMIN",
            "photo_id": 1,
            "company_id":  1,
            "token": "",
            "token_verified": False,
        }
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_user(self):
        data = {
            "username": "email_1@test.com",
            "first_name": "FirstName",
            "last_name": "LastName",
            "email": "email_1@test.com",
            "password": "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
            "is_active": False,
            "address": "",
            "active": False,
            "type": "SUPERADMIN",
            "photo_id": 1,
            "company_id":  1,
            "token": "",
            "token_verified": False,
        }
        response = self.client.put('/api/users/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_user(self):
        response = self.client.delete('/api/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_variants(self):
        response = self.client.get('/api/variants/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_variant(self):
        response = self.client.get('/api/variants/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_variant(self):
        data = {
            "product_id":  1,
            "price": 128.0,
            "stock": 128,
            "shipment": 128.0,
        }
        response = self.client.post('/api/variants/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_variant(self):
        data = {
            "product_id":  1,
            "price": 128.0,
            "stock": 128,
            "shipment": 128.0,
        }
        response = self.client.put('/api/variants/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_variant(self):
        response = self.client.delete('/api/variants/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_variantoptions(self):
        response = self.client.get('/api/variantoptions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_variantoption(self):
        response = self.client.get('/api/variantoptions/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_variantoption(self):
        data = {
            "title": "",
            "value": "",
            "variant_id":  1,
        }
        response = self.client.post('/api/variantoptions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_variantoption(self):
        data = {
            "title": "",
            "value": "",
            "variant_id":  1,
        }
        response = self.client.put('/api/variantoptions/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_variantoption(self):
        response = self.client.delete('/api/variantoptions/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)