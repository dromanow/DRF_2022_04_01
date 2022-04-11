"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from library.views import AuthorModelViewSet, author_get, author_post, BioModelViewSet, BookModelViewSet, book_get, \
    bio_get

router = SimpleRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)
router.register('bios', BioModelViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('author_get/', author_get),
    path('book_get/', book_get),
    path('bio_get/', bio_get),
    path('author_get/<int:pk>', author_get),
    path('author_post/', author_post),
]
