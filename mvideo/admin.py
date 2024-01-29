from django.contrib import admin
from django.db.models import QuerySet

from mvideo.models import NetworkUnit, Product
from django.utils.html import format_html


@admin.register(NetworkUnit)
class NetworkUnitAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'email',
                    'country',
                    'city',
                    'street',
                    'house_number',
                    'supplier',
                    'level',
                    'created_at',
                    'debt_to_supplier',
                    'supplier_link',)

    # Добавляем действие - обнуление задолженности

    actions = ('set_null_debt',)

    # Добавляем фильтрацию по городу в админку

    list_filter = ('city',)

    # Добавляем отображение ссылки на поставщика

    list_display_links = ('name', 'supplier_link',)

    @admin.action(description='Обнулить дебиторскую задолженность')
    def set_null_debt(self, request, qs: QuerySet):
        """Обнуляет задолженность перед поставщиком"""

        qs.update(debt_to_supplier=0)

    def supplier_link(self, obj: NetworkUnit):
        """Создает ссылку на поставщика"""

        if obj.supplier is not None:
            return format_html(
                '<a href="/admin/mvideo/networkunit/{id}/">{name}</a>',
                id=obj.supplier.id,
                name=obj.supplier
            )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'model',
                    'release_date',
                    'owner',)
