from . import models, serializers
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
# from django.core import serializers
from rest_framework.renderers import JSONRenderer
from datetime import datetime
# Create your views here.

class Time(APIView):
    # renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        time = str(datetime.utcnow())
        data = {'Current Time': time}
        try:
            # json_data = JSONRenderer().render(data)
            return Response(data, status=status.HTTP_200_OK)
        except:
            error_message = {'Error':'Bad Request'}
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer

class Userinput(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class Choices_View(viewsets.ModelViewSet):
    # queryset = models.Options.objects.all()
    serializer_class = serializers.ChoiceSerializer

    def get_queryset(self, *args, **kwargs):
        
        question_id = self.kwargs['question_id']
        choice_id = self.kwargs.get('choice_id', None)
        if choice_id:
            return Response(self.serializer_class(models.Options.objects.filter(question=question_id, id = choice_id), many=True).data)
        else:
            return Response(self.serializer_class(models.Options.objects.filter(question=question_id), many=True).data)

    
    def create(self, *args, **kwargs):
        data = args[0].data
        question = get_object_or_404(models.Question, pk=kwargs.pop('question_id', None))
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(question=question)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, *args, **kwargs):
        data = args[0].data
        choice_id = kwargs.get('choice_id')
        choice = get_object_or_404(models.Options, pk = choice_id)
        question = get_object_or_404(models.Question, pk=kwargs.get('question_id'))
        serializer = self.serializer_class(instance=choice,data=data,partial=True)
        if serializer.is_valid():
            serializer.save(question = question)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, *args, **kwargs):
        choice_id = kwargs.get('choice_id')
        question_id = kwargs.get('question_id')
        choice = get_object_or_404(models.Options, pk =choice_id, question=question_id)
        present = self.serializer_class(data = choice)
        if not choice:
            return Response(
                {"res": "Object with choice_id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        choice.delete()
        return Response({'result':'Object Deleted'}, status=status.HTTP_200_OK)

class GetUserChoices(APIView):
    def get(self, request, user_id):
        choices = models.Options.objects.filter(user=user_id, selected=True)
        serializer = serializers.ChoiceSerializer(choices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

# class Choices_View(APIView):
#     def post(self,request,question_id, *args, **kwargs):
#         choices = models.Options.objects.filter(question=question_id)
#         if ('id' in list(request.data.keys())) and (request.data['id'] == choices.count()):
#             chosen = choices.get(id = request.data['id'] )
#             chosen.choice_text = request.data['choice_text']
#             chosen.selected = request.data['selected']
#             chosen.save()
#             return Response('Added', status=status.HTTP_200_OK)
#         question =  get_object_or_404(models.Question, pk=question_id)
#         serializer = serializers.ChoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             choice = serializer.save(question=question)
#             return Response(serializers.ChoiceSerializer(choice).data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def get(self, request,question_id, *args, **kwargs):
#         choices = models.Options.objects.filter(question=question_id)
#         serializer = serializers.ChoiceSerializer(choices, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request,question_id):
#         id = request.data.get('id')
#         choice = models.Options.objects.filter(id = id).first()
#         # print(choice)
#         serializer = serializers.ChoiceSerializer(choice, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




