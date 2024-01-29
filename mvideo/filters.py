import django_filters

from mvideo.models import NetworkUnit


class NetworkUnitFilter(django_filters.FilterSet):

    """Фильтрация по стране"""

    country = django_filters.CharFilter(field_name='country', lookup_expr='exact')

    class Meta:
        model = NetworkUnit
        fields = ['country']