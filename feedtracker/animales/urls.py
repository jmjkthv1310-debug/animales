from django.urls import path
from .views import AnimalListCreate, AnimalDetail, AnimalRandom

urlpatterns = [
    path('', AnimalListCreate.as_view()),
    path('<int:animal_id>/', AnimalDetail.as_view()),
    path('random/', AnimalRandom.as_view()),
]
