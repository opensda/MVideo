from django.urls import path, include

from mvideo.apps import MvideoConfig
from mvideo.views import NetworkUnitListAPIView, \
    NetworkUnitCreateAPIView, \
    NetworkUnitDetailAPIView, NetworkUnitUpdateAPIView, NetworkUnitDestroyAPIView

app_name = MvideoConfig.name

urlpatterns = [
    path("networkunit/", NetworkUnitListAPIView.as_view(), name='networkunit_list'),
    path("networkunit/create/", NetworkUnitCreateAPIView.as_view(), name='networkunit_create'),
    path("networkunit/<int:pk>", NetworkUnitDetailAPIView.as_view(), name='networkunit_detail'),
    path("networkunit/<int:pk>/update/", NetworkUnitUpdateAPIView.as_view(), name='networkunit_update'),
    path("networkunit/<int:pk>/delete/", NetworkUnitDestroyAPIView.as_view(), name='networkunit_delete'),

]
