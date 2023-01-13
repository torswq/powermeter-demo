from django.db.models import Max, Min, Avg, Sum
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializers import *
from .models import *
from . import queries

class MeasurerViewset(ModelViewSet):
    serializer_class = MeasurerSerializer
    queryset = Measurer.objects.all()
    
class MeasurerHistoryViewset(ModelViewSet):
    serializer_class = MeasurerHistorySerializer
    queryset = MeasurerHistory.objects.all()
    @action(["GET"], detail=False, url_path='max_consumption')
    def max_consumption(self, request):
        data = queries.max_consumption(self.queryset)
        print(data[0])
        return JsonResponse({"data": [*data]})
    @action(["GET"], detail=False, url_path='min_consumption')
    def min_consumption(self, request):
        data = queries.min_consumption(self.queryset)
        print(data[0])
        return JsonResponse({"data": [*data]})

    @action(["GET"], detail=False, url_path='avg_consumption')
    def avg_consumption(self, request):
        data = queries.avg_onsumption(self.queryset)
        return JsonResponse({"data": [*data]})

    @action(["GET"], detail=False, url_path='total_consumption')
    def total_consumption(self, request):
        data = queries.total_consumption(self.queryset)
        return JsonResponse({"data": [*data]})

    @action(["GET"], detail=False, url_path='consumption_info')
    def consumption_info(self, request):
        data = queries.full_consumption_info(self.queryset)
        return JsonResponse([*data], safe=False)
        
    


