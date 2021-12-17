from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse 


class AdminSiteTests(TestCase):

    def setUp(self):
        '''runs before test func'''

        self.client=Client()
        self.admin_user=get_user_model().objects.create_superuser(
            email='admin@ilctech.com',
            password='1234'

        )
        self.client.force_login(self.admin_user)
        self.test_user=get_user_model().objects.create_user(
            email='test@ilctech.com',
            password='1234',
            name='test user'
        )


    def test_listed_user(self):

        '''test for listed user'''
        url= reverse('admin:core_user_changelist')
        res=self.client.get(url)

        self.assertContains(res, self.test_user.name)
        self.assertContains(res, self.test_user.email)


    def test_admin_site_page(self):
        '''user edit func of admin site'''

        url=reverse('admin:core_user_change', args=[self.test_user.id])
        
        res=self.client.get(url)
        self.assertEqual(res.status_code,200)

    def  test_create_user_page(self):

        url=reverse('admin:core_user_add')
        res=self.client.get(url)

        self.assertEqual(res.status_code,200)