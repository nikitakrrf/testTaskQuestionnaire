from django.urls import path, include

from respondent.views import QuestionView, QuestionCheckDeleteView, AnswerCreateView, AnswerCheckDeleteView

question_patterns_ = ([
    path('', QuestionView.as_view(), name='questions-start'),
    path('<int:pk>/', QuestionCheckDeleteView.as_view(), name='questions-detail'),
    path('<int:pk>/answers/', AnswerCreateView.as_view(), name='questions-check'),
], 'questions')

answer_patterns_ = ([
    path('<int:pk>/', AnswerCheckDeleteView.as_view(), name='answer-detail'),
], 'answer')

urlpatterns = [
    path("questions/",include(question_patterns_)),
    path("answers/",include(answer_patterns_)),
]