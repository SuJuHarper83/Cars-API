from msilib.schema import SelfReg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer

@api_view (['GET', 'POST'])
def cars_list(request):
    if request.method == "GET":
        cars = Car.objects.all()
    elif request.method == "POST":
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    serializer = CarSerializer(cars, many=True)

    return Response(serializer.data)
