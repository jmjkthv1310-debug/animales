from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Pregunta
from .serializers import PreguntaSerializer


@api_view(['GET'])
def listar_preguntas(request):
    preguntas = Pregunta.objects.all()
    serializer = PreguntaSerializer(preguntas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def obtener_pregunta(request, id):
    try:
        pregunta = Pregunta.objects.get(id=id)
    except Pregunta.DoesNotExist:
        return Response({"error": "No existe"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PreguntaSerializer(pregunta)
    return Response(serializer.data)


@api_view(['POST'])
def crear_pregunta(request):
    serializer = PreguntaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def actualizar_pregunta(request, id):
    try:
        pregunta = Pregunta.objects.get(id=id)
    except Pregunta.DoesNotExist:
        return Response({"error": "No existe"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PreguntaSerializer(pregunta, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def eliminar_pregunta(request, id):
    try:
        pregunta = Pregunta.objects.get(id=id)
    except Pregunta.DoesNotExist:
        return Response({"error": "No existe"}, status=status.HTTP_404_NOT_FOUND)

    pregunta.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
