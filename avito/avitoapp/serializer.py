from rest_framework.serializers import ModelSerializer

from avitoapp.models import Ad


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = ['name', 'description', 'price', 'address', 'user', 'phone']
