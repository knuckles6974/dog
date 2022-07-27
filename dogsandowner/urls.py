from django.urls import path
from .views      import OwnerView, DogView, DogandOwnerView

urlpatterns = [
      path('', OwnerView.as_view()),
      path('/dog', DogView.as_view()),
      path('/dogandowner', DogandOwnerView.as_view())
]