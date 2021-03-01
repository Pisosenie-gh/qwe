from django.urls import path
from .views import TopBackView
from . import views


urlpatterns = [
    path('topes/', views.TopBackView.as_view(), name='topback_view')

]