from .models import Author, Book, Bio, TestBio
from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField, ValidationError, StringRelatedField


class AuthorSerializer(Serializer):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    birthday_year = IntegerField()

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        instance.save()
        return instance

    def create(self, validated_data):
        author = Author(**validated_data)
        author.save()
        return author

    def validate_birthday_year(self, value):
        if value < 500:
            raise ValidationError('Must be gt 500')
        return value

    def validate(self, attrs):
        if attrs['birthday_year'] < 1000:
            raise ValidationError('Must be gt 1000')
        return attrs


class BookSerializer(Serializer):
    title = CharField(max_length=64)
    authors = AuthorSerializer(many=True)


class BioSerializer(Serializer):
    title = CharField(max_length=64)
    author = AuthorSerializer()


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorModelSerializerV2(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']


class BookModelSerializer(ModelSerializer):
    # authors = StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = '__all__'


class BioModelSerializer(ModelSerializer):
    class Meta:
        model = Bio
        fields = '__all__'


class TestBioModelSerializer(ModelSerializer):
    class Meta:
        model = TestBio
        fields = '__all__'
