from rest_framework import generics

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorListSerializer, SensorDetailSerializer, MeasurementSerializer


# Создать датчик. Указываются название и описание датчика.
# Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.
class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorListSerializer
        return SensorDetailSerializer


# Изменить датчик. Указываются название и описание.
# Получить информацию по конкретному датчику.
class SensorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# Добавить измерение. Указываются ID датчика и температура.
class MeasurementCreateAPIView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

