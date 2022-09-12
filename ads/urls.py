from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers

from ads.views.ad import *
from ads.views.category import CategoryViewSet
from ads.views.index import index
from ads.views.location import LocationViewSet
from ads.views.selection import *
from my_project import settings


"""Definition of category router"""
category_router = routers.SimpleRouter()
category_router.register('category', CategoryViewSet)


"""Definition of location router"""
location_router = routers.SimpleRouter()
location_router.register('location', LocationViewSet)


urlpatterns = [
    path('', index, name="index"),
    path('ad/', AdListView.as_view()),
    path('ad/<int:pk>/', AdRetrieveView.as_view()),
    path('ad/create/', AdCreateView.as_view()),
    path('ad/<int:pk>/update/', AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', AdDestroyView.as_view()),
    path('ad/<int:pk>/upload_image/', AdImageView.as_view()),

    path('selection/', SelectionListView.as_view()),
    path('selection/<int:pk>/', SelectionRetrieveView.as_view()),
    path('selection/create/', SelectionCreateView.as_view()),
    path('selection/<int:pk>/update/', SelectionUpdateView.as_view()),
    path('selection/<int:pk>/delete/', SelectionDestroyView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""Including all ViewSets urls"""
urlpatterns += category_router.urls
urlpatterns += location_router.urls
