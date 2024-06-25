from rest_framework import viewsets

from teams.models import Person, Team
from teams.serializers import PersonSerializer, TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().select_related('team')
    serializer_class = PersonSerializer
