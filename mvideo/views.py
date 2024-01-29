from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from mvideo.filters import NetworkUnitFilter
from mvideo.models import NetworkUnit
from users.permissions import IsActiveEmployeePermission
from mvideo.serializers import NetworkUnitSerializer, NetworkUnitUpdateSerializer


class NetworkUnitListAPIView(generics.ListAPIView):
    serializer_class = NetworkUnitSerializer
    queryset = NetworkUnit.objects.all()

    # Фильтрация по стране

    filter_backends = [DjangoFilterBackend]
    filterset_class = NetworkUnitFilter

    # Права доступа

    permission_classes = [IsActiveEmployeePermission]





class NetworkUnitCreateAPIView(generics.CreateAPIView):
    serializer_class = NetworkUnitSerializer
    permission_classes = [IsActiveEmployeePermission]


class NetworkUnitDetailAPIView(generics.RetrieveAPIView):
    serializer_class = NetworkUnitSerializer
    queryset = NetworkUnit.objects.all()
    permission_classes = [IsActiveEmployeePermission]


class NetworkUnitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NetworkUnitUpdateSerializer
    queryset = NetworkUnit.objects.all()
    permission_classes = [IsActiveEmployeePermission]


class NetworkUnitDestroyAPIView(generics.DestroyAPIView):
    queryset = NetworkUnit.objects.all()
    permission_classes = [IsActiveEmployeePermission]