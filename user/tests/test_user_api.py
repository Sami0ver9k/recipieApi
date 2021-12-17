from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL=reverse('user:create')
TOKEN_URL= reverse('user:token')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicApiTest(TestCase):
    '''test public api without any auth token'''

    def setUp(self) -> None:
        self.client=APIClient()

    def test_create_user(self):
        '''test with payload to create user'''
        payload={
            'email':'test@ilc.com',
            'password':'1234',
            'name': 'test user'
        }
        res=self.client.post(CREATE_USER_URL, data=payload)
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user=get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password'])) #check of pass is send by create_user obj
        self.assertNotIn('password',res.data)


    def test_user_already_exists(self):

        payload={
            'email':'test@ilc.com',
            'password':'1234',
            'name': 'test user'
        }
        create_user(**payload)
        res=self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_user(self):

        payload={
            'email':'test@ilc.com',
            'password':'1234',
            'name': 'test user'
        }
        create_user(**payload)
        res=self.client.post(TOKEN_URL, payload)
        self.assertIn('token',res.data)
        self.assertEqual(res.status_code,status.HTTP_200_OK)

    
    def test_no_user_for_token(self):

        payload={
            'email':'test@ilc.com',
            'password':'1234',
            'name': 'test user'
        }
        
        res=self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token',res.data)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)


