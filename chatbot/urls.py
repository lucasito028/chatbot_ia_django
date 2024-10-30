from django.contrib import admin
from django.urls import path
from chatbot.views import openai

urlpatterns = [
    path("correcao", openai.correcao, name="correcao")
]
