from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Person, Team


class TeamTests(APITestCase):
    def setUp(self):
        self.team_data = {'name': 'Engineering'}
        self.team = Team.objects.create(name='HR')
        Team.objects.create(name='Finance')

    def test_create_team(self):
        url = reverse('team-list')
        response = self.client.post(url, self.team_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(Team.objects.get(id=response.data['id']).name, 'Engineering')

    def test_get_team_list(self):
        url = reverse('team-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_team_detail(self):
        url = reverse('team-detail', kwargs={'pk': self.team.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'HR')

    def test_update_team(self):
        url = reverse('team-detail', kwargs={'pk': self.team.id})
        data = {'name': 'Finance'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.team.refresh_from_db()
        self.assertEqual(self.team.name, 'Finance')

    def test_delete_team(self):
        url = reverse('team-detail', kwargs={'pk': self.team.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Team.objects.count(), 1)


class PersonTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Engineering')
        self.person_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'team': self.team.id
        }
        self.person = Person.objects.create(
            first_name='Jane',
            last_name='Smith',
            email='jane.smith@example.com',
            team=self.team
        )

    def test_create_person(self):
        url = reverse('person-list')
        response = self.client.post(url, self.person_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 2)
        self.assertEqual(Person.objects.get(id=response.data['id']).first_name, 'John')

    def test_get_person_list(self):
        url = reverse('person-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_person_detail(self):
        url = reverse('person-detail', kwargs={'pk': self.person.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Jane')

    def test_update_person(self):
        url = reverse('person-detail', kwargs={'pk': self.person.id})
        data = {
            'first_name': 'Janet',
            'last_name': 'Smith',
            'email': 'janet.smith@example.com',
            'team': self.team.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.person.refresh_from_db()
        self.assertEqual(self.person.first_name, 'Janet')

    def test_delete_person(self):
        url = reverse('person-detail', kwargs={'pk': self.person.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)
