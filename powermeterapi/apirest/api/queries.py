from .models import *
from django.db.models import Sum, Max, Min, Avg
def max_consumption(queryset, uuid=""):
    if uuid == "":
        return queryset.values('uuid', 'uuid__name').annotate(max_consumption=Max('consumption')).order_by('-max_consumption')
    else:
        return queryset.get(uuid=uuid).values('uuid', 'uuid__name').annotate(max_consumption=Max('consumption')).order_by('-max_consumption')

def min_consumption(queryset, uuid=""):
    if uuid == "":
        return queryset.values('uuid', 'uuid__name').annotate(min_consumption=Min('consumption')).order_by('min_consumption')
    else:
        return queryset.get(uuid=uuid).values('uuid', 'uuid__name').annotate(min_consumption=Min('consumption')).order_by('min_consumption')

def avg_consumption(queryset, uuid=""):
    if uuid == "":
        return queryset.values('uuid', 'uuid__name').annotate(avg_consumption=Avg('consumption')).order_by('-avg_consumption')
    else:
        return queryset.get(uuid=uuid).annotate(avg_consumption=Avg('consumption')).order_by('-avg_consumption')

def total_consumption(queryset, uuid=""):
    if uuid == "":
        return queryset.values('uuid', 'uuid__name').annotate(total_consumption=Sum('consumption')).order_by('-total_consumption')
    else:
        return queryset.get(uuid=uuid).values('uuid', 'uuid__name').annotate(total_consumption=Sum('consumption')).order_by('-total_consumption')

def full_consumption_info(queryset):
    return queryset.values('uuid', 'uuid__name').annotate(
        max_consumption=Max('consumption'),
        min_consumption=Min('consumption'),
        avg_consumption=Avg('consumption'),
        total_consumption=Sum('consumption')
    ).order_by('-total_consumption')