from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Answer, Feeling


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        # json で出力するフィールド
        fields = ('id', 'text')
        