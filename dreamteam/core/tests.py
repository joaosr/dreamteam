import uuid
import json
from django.test import TestCase
from datetime import datetime
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status
from dreamteam.core.models import UserMember, Team
from dreamteam.core.forms import (UserMemberForm, TeamForm)
from dreamteam.core.api.views import LoginAPIView
from dreamteam.core.views import send_confirmation_email



class UserTest(APITestCase):
    def setUp(self):
        pass

    def test_register_user_service(self):
        data = {
            'email': 'js@joao.com',
            'password': '234567',
            'first_name': 'Joao',
            'last_name': 'Soares'
        }
        response = self.client.post('/api/user_members/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_service(self):
        user_member = UserMember(
            first_name = "João",
            last_name = "Soares",
            email = "eng.jmsoares@gmail.com",
            password = "12345678",
        )
        user_member.set_password(user_member.password)
        user_member.save()

        data = {'email': 'eng.jmsoares@gmail.com', 'password': '12345678'}
        response = self.client.post('/api/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_send_confirmation_email(self):
        email = "eng.jmsoares@gmail.com"
        token = ""
        result = send_confirmation_email(email, token)
        self.assertEqual(1, result)

    def test_confirmation_email(self):
        token = uuid.uuid4().hex
        data = {
            'email': 'js@joao.com',
            'password': '234567',
            'first_name': 'Joao',
            'last_name': 'Soares'
        }
        response = self.client.post('/api/user_members/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user_members =  json.loads(response.content.decode('utf-8'))
        token = user_members['token']

        response = self.client.get('/api/confirmation_email/'+'fake_token', format='json')

        self.assertEqual(response.status_code, 404)

        response = self.client.get('/api/confirmation_email/'+token, format='json')

        user_members =  json.loads(response.content.decode('utf-8'))

        self.assertEqual(200, response.status_code)
        self.assertTrue(user_members['verifeid'])
