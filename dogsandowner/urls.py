from django.urls import path
from .views      import DogsandownerView

urlpatterns = [
      path('', DogsandownerView.as_view()),
      
]