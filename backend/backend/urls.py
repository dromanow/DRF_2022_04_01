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
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from library.views import *
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, Contact, License

schema_view = get_schema_view(
    Info(
        title='Library',
        default_version='1.0',
        description='description',
        contact=Contact(email='test@test.com'),
        license=License(name='MIT')
    ),
    public=True,
    permission_classes=(AllowAny, )
)

# router = DefaultRouter()
# # router.register('authors', AuthorModelViewSet)
# router.register('books', BookModelViewSet)
# router.register('bios', BioModelViewSet)
# router.register('tb', TestBioModelViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    path('api/', include('library.urls')),
    # path('api/', include('library.urls', namespace='1.0')),
    # path('api/v1/', include('library.urls', namespace='1.0')),
    # path('api/v2/', include('library.urls', namespace='2.0')),
    # path('api/v3/', include('library.urls', namespace='1.8')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', views.obtain_auth_token),
    path('jwt-token/', TokenObtainPairView.as_view()),
    path('jwt-token-refresh/', TokenRefreshView.as_view()),
    path('swagger/', schema_view.with_ui()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),

    # re_path(r'^api/(?P<version>\d.\d)/authors/', AuthorModelViewSet.as_view({'get': 'list'}))

    # path('book_get/', book_get),
    # path('book_get_api_view/', BookApiView.as_view()),
    # path('book_get_viewset/', BookReadViewSet.as_view({'get': 'list'})),
    # path('book_get_dec/', book_get_dec),
    # path('book_get_conc/', BookListApiView.as_view()),
    # path('bio_get/', bio_get),
    # path('author_get/', author_get),
    # path('author_get_viewset/kwargs/<str:first_name>', AuthorModelViewSet.as_view({'get': 'list'})),
    # path('author_get/<int:pk>', author_get),
    # path('author_post/', author_post),
]
