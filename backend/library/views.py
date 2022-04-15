import io

from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
from rest_framework.pagination import LimitOffsetPagination
from .models import Author, Book, Bio, TestBio
from .serializer import AuthorModelSerializer, AuthorSerializer, BookModelSerializer, BioModelSerializer, \
    BookSerializer, BioSerializer, TestBioModelSerializer


class AuthorLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class AuthorModelViewSet(ModelViewSet):
    # pagination_class = AuthorLimitOffsetPagination
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()

    @action(detail=False, methods=['get'])
    def get_author_name(self, request, pk=None):
        author = get_object_or_404(Author, pk=pk)
        return Response({'name': str(author)})

    def get_queryset(self):
        first_name = self.request.query_params.get('first_name', None)
        if first_name:
            return Author.objects.filter(first_name=first_name)
        first_name = self.request.query_params.get('first_name', None)
        if first_name:
            return Author.objects.filter(first_name__contains=first_name)
        return Author.objects.all()


class BookModelViewSet(ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()


class BioModelViewSet(ModelViewSet):
    serializer_class = BioModelSerializer
    queryset = Bio.objects.all()


class TestBioModelViewSet(ModelViewSet):
    serializer_class = TestBioModelSerializer
    queryset = TestBio.objects.all()


class BookReadViewSet(ListModelMixin, GenericViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()


def author_get(request, pk=None):
    if pk is None:
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
    else:
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)


class BookApiView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def book_get_dec(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


class BookListApiView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    renderer_classes = [JSONRenderer]


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



