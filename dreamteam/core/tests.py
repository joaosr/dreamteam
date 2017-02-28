from django.test import TestCase
from dreamteam.core.models import UserMember, Team
from dreamteam.core.forms import (UserMemberForm, TeamForm)
from datetime import datetime
from rest_framework.test import APIRequestFactory
from dreamteam.core.api.views import LoginAPIView
from rest_framework.test import APITestCase
from rest_framework import status


class UserTest(APITestCase):
    def setUp(self):
        pass

    def test_register_user(self):
        data = {
            'email': 'js@joao.com',
            'password': '234567',
            'first_name': 'Joao',
            'last_name': 'Soares'
        }
        response = self.client.post('/api/user_members/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
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



# # Create your tests here.
# class UserMemberModelTest(TestCase):
#     def setUp(self):
#         team = Team(name="Code")
#         team.save()
#         self.user_member = UserMember(
#             first_name = "João",
#             last_name = "Soares",
#             email = "eng.jmsoares@gmail.com",
#             password = "1234",
#             team = team
#         )
#
#         self.user_member.save()
#
#
#     def test_create(self):
#         self.assertTrue(UserMember.objects.exists())
#
#     def test_create_at(self):
#         """ User member must have an auto created at attr."""
#         self.assertIsInstance(self.user_member.created_at, datetime)
#
# class TeamModelTest(TestCase):
#     def setUp(self):
#         self.team = Team(name="Code")
#         self.team.save()
#
#     def test_create(self):
#         self.assertTrue(Team.objects.exists())
#
#     def test_create_at(self):
#         """ User member must have an auto created at attr."""
#         self.assertIsInstance(self.team.created_at, datetime)
#
#
# class UserMemberFormTest(TestCase):
#     def setUp(self):
#         team = Team(name="Code")
#         self.user_member = UserMember(
#             first_name = "João",
#             last_name = "Soares",
#             email = "eng.jmsoares@gmail.com",
#             password = "1234",
#             team = team
#         )
#
#     def test_valid_data(self):
#         form = UserMemberForm({
#             'first_name': "João",
#             'last_name': "Soares",
#             'email': "eng.jmsoares@gmail.com",
#             'password': "1234",
#             'confirm_password': "1234"
#         }, self.user_member)
#
#         self.assertTrue(form.is_valid())
#         user_member = form.save()
#         self.assertEqual(user_member.first_name, "João")
#         self.assertEqual(user_member.last_name, "Soares")
#         self.assertEqual(user_member.email, "eng.jmsoares@gmail.com")
#         self.assertEqual(user_member.password, "1234")
#
#     def test_blank_data(self):
#         form = UserMemberForm({}, self.user_member)
#         self.assertFalse(form.is_valid())
#         self.assertEqual(form.errors, {
#             'last_name': ['This field is required.'],
#             'first_name': ['This field is required.'],
#             'password': ['This field is required.'],
#             'confirm_password': ['This field is required.'],
#             'email': ['This field is required.'],
#         })
#
# class TeamFormTest(TestCase):
#     def setUp(self):
#         self.team = Team(name="Frontend")
#
#     def test_valid_data(self):
#         form = TeamForm({
#             'name': "Frontend",
#         }, self.team)
#
#         self.assertTrue(form.is_valid())
#         team = form.save()
#         self.assertEqual(team.name, "Frontend")
#
#     def test_blank_data(self):
#         form = TeamForm({}, self.team)
#         self.assertFalse(form.is_valid())
#         self.assertEqual(form.errors, {
#             'name': ['This field is required.'],
#         })
