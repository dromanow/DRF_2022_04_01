import io

from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
from .models import Author, Book, Bio
from .serializer import AuthorModelSerializer, AuthorSerializer, BookModelSerializer, BioModelSerializer, \
    BookSerializer, BioSerializer


class AuthorModelViewSet(ModelViewSet):
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()


class BookModelViewSet(ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()


class BioModelViewSet(ModelViewSet):
    serializer_class = BioModelSerializer
    queryset = Bio.objects.all()


def author_get(request, pk=None):
    if pk is None:
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
    else:
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)


def book_get(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)


def bio_get(request):
    bio = Bio.objects.all()
    serializer = BioSerializer(bio, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)



@csrf_exempt
def author_post(request):
    data = JSONParser().parse(io.BytesIO(request.body))

    if request.method == 'POST':
        serializer = AuthorSerializer(data=data)
    elif request.method == 'PUT':
        author = Author.objects.get(pk=4)
        serializer = AuthorSerializer(author, data=data)
    elif request.method == 'PATCH':
        author = Author.objects.get(pk=4)
        serializer = AuthorSerializer(author, data=data, partial=True)

    if serializer.is_valid():
        author = serializer.save()

        serializer = AuthorSerializer(author)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)
    else:
        return HttpResponseBadRequest(JSONRenderer().render(serializer.errors))



