from django.urls import path
from .views import FeedBackView
from . import views


urlpatterns = [
    path('feed/', views.FeedBackView.as_view(), name='feedback_view')

]

