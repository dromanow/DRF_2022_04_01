from .models import Author
from rest_framework.serializers import ModelSerializer


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
