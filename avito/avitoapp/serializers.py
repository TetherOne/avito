from rest_framework import serializers

from avitoapp.models import Ad



class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            'pk',
            'name',
            'description',
            'price',
            'address',
            'phone',
            'created_at',
            'user'
        )