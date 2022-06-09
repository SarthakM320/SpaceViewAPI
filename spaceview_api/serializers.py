from rest_framework import serializers
from .models import Question, Options, User

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Question

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        excluded = ['question']
        model = Options