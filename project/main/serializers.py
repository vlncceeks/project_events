from rest_framework import serializers
from .models import Events  # Убедитесь, что модель Event существует

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
