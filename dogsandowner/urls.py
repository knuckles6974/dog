from django.urls import path
from .views      import OwnerView, DogView

urlpatterns = [
      path('', OwnerView.as_view()),
      path('/dog', DogView.as_view()) 
      
]