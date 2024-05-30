from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer