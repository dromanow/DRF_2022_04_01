from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)
router.register('bios', BioModelViewSet)
router.register('tb', TestBioModelViewSet)


app_name = 'library'

urlpatterns = [
    path('', include(router.urls))
]
