from rest_framework import serializers
from Home.models import Packages


class PackagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Packages
        fields = ('name', 'img', 'description')