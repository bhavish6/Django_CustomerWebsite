import django_filters
from django_filters import DateFilter
from .models import *
class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="Date_Created" , lookup_expr="gte")
    end_date = DateFilter(field_name="Date_Created", lookup_expr="lte")
    class Meta:
        model =  order
        fields = '__all__'
        exclude = ['Customers' , 'Date_Created']

