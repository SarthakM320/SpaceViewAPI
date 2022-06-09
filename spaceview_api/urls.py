from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('questions', QuestionViewSet, basename='questions')
router.register('users', Userinput, basename='users')
# router.register('time', Time.as_view(), basename='time')
urlpatterns = [
    path('time', Time.as_view(), name='time'),
    path('', include(router.urls)),
    path('questions/<int:question_id>/choices/', Choices_View.as_view({'get':'get_queryset', 'post':'create'}) , name='view-choices'),
    path('questions/<int:question_id>/choices/<int:choice_id>', Choices_View.as_view({'get':'get_queryset','put':'update', 'delete':'   '}) , name='view-choices-update'),
    path('users/<int:user_id>/choices/',GetUserChoices.as_view({'get':'get_queryset'}), name='user_choices')
]