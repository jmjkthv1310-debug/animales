import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .data import animales

# -----------------------------------
# GET LISTA / POST CREAR ANIMAL
# -----------------------------------
class AnimalListCreate(APIView):

    def get(self, request):
        return Response(animales)

    def post(self, request):
        nuevo = request.data
        nuevo["id"] = len(animales) + 1
        animales.append(nuevo)
        return Response(nuevo, status=status.HTTP_201_CREATED)


# -----------------------------------
# GET / PUT / DELETE por ID
# -----------------------------------
class AnimalDetail(APIView):

    def get(self, request, animal_id):
        for animal in animales:
            if animal["id"] == animal_id:
                return Response(animal)
        return Response({"error": "Animal no encontrado"}, status=404)

    def put(self, request, animal_id):
        for animal in animales:
            if animal["id"] == animal_id:
                animal.update(request.data)
                return Response(animal)
        return Response({"error": "Animal no encontrado"}, status=404)

    def delete(self, request, animal_id):
        for animal in animales:
            if animal["id"] == animal_id:
                animales.remove(animal)
                return Response({"mensaje": "Animal eliminado"})
        return Response({"error": "Animal no encontrado"}, status=404)


# -----------------------------------
# ANIMAL RANDOM
# -----------------------------------
class AnimalRandom(APIView):
    def get(self, request):
        return Response(random.choice(animales))
