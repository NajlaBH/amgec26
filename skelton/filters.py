#filters.py
import django_filters
from .models import Contact

class ContactFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='icontains')
    #created_at = django_filters.DateFromToRangeFilter()
    title = "demande_type"
    parameter_name = 'demande'

    class Meta:
        model = Contact
        fields = ['demande_date','demande']
