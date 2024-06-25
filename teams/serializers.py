from rest_framework import serializers

from teams.models import Person, Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']


class PersonSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), write_only=True)

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'team_id', 'team_name']
