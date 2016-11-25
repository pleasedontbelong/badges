from rest_framework import serializers
from accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    badges = serializers.StringRelatedField(many=True)

    class Meta:
        model = Profile
        fields = ('id', 'nb_views', 'badges')
