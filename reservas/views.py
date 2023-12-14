from django.shortcuts import render
from .models import Reserva
from .serializers import ReservasSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def ListarReservas(request):
    reservas  = Reserva.objects.all()
    serializer = ReservasSerializer(reservas, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def FiltrarReserva(request, pk):
    reserva = Reserva.objects.get(id_reserva=pk)
    serializer = ReservasSerializer(reserva, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CrearReserva(request):
    serializer = ReservasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['POST'])
def ActualizarReserva(request, pk):
    reserva = Reserva.objects.get(id_reserva=pk)
    serializer = ReservasSerializer(instance=reserva, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def EliminarReserva(request, pk):
    reserva = Reserva.objects.get(id_reserva=pk)
    reserva.delete()

    return Response('Reserva eliminado')