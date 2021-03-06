from django.db.models.base import Model
from django.test import TestCase
from django.contrib.auth  import get_user_model
from core import models

class ModelTests(TestCase):

    def test_create_user(self):


        email="example@google.com"
        password=1234

        user=get_user_model().objects.create_user(
        email=email,
        password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password)) #return bool


    def test_user_email_normalized(self):
        '''use to check for normalization the user email when creating acc'''

        email="sami@EXAMPLE.COM"
        password=1234
        user=get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email.lower())


    def test_email_validity(self):
        '''check for email validation'''

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,"1234")

    
    def  test_tag_str(self):
        tag=models.Tag.objects.create(

             user=get_user_model().objects.create_user(
              email='example@google.com',
              password='1234'
        ),
           name='vegan'

        )

        self.assertEqual(str(tag),tag.name)


    