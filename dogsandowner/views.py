import json

from django.views     import View
from .models          import Owner
from django.http      import JsonResponse


# Create your views here.
class DogsandownerView(View):
    def post(self, request):
          data = json.loads(request.body)

          dog = Owner.objects.create(dog=data["dog_name"])
          type = Owner.objects.create(type=data["type"])
          owner = Owner.objects.create(name=data["owner_name"])

          return JsonResponse({"message" : "개새끼 등록완료"}, status = 201)

# Create your views here.


