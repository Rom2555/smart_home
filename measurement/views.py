# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorListSerializer, SensorDetailSerializer, MeasurementSerializer


# Запросы, которые должны быть реализованы в системе:
#
# 1. Создать датчик. Указываются название и описание датчика.
# 2. Изменить датчик. Указываются название и описание.
# 3. Добавить измерение. Указываются ID датчика и температура.
# 4. Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.

class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorListSerializer
        return SensorDetailSerializer


class SensorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateAPIView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

