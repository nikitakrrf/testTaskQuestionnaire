from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import generics, status
from rest_framework.response import Response

from respondent.models import Question, Answer
from respondent.serializers import QuestionSerializer, QuestionCreateSerializer, AnswerCreateSerializer, \
    AnswerSerializer


# Create your views here.

class QuestionView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer


class QuestionCheckDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer

    def create(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['pk'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(question_id=question)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AnswerCheckDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Answer.objects.select_related('question_id').all()
    serializer_class = AnswerSerializer