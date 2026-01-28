from rest_framework.serializers import ModelSerializer
from .models import CocaCola
class CocaColaSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CocaCola