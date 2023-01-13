from rest_framework import serializers
from .models import *

class MeasurerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurer
        fields = (
            'uuid',
            'name',
            'consumption',
            'last_modification'
        )

class MeasurerHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MeasurerHistory
        fields = (
            'uuid',
            'consumption',
            'modification_time'
        )