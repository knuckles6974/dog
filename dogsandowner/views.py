import json

from django.views     import View
from .models          import Owner,Dog
from django.http      import JsonResponse


# Create your views here.
class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)

        Owner.objects.create(
            
            first_name = data["first_name"],
            last_name = data["last_name"],
            age = data["age"]
            
        )
        
        return JsonResponse({"message" : "정보등록완료"}, status = 201)
    
class DogView(View):
    def post(self,request):
        data = json.loads(request.body)
        
        Dog.objects.create(
            name = data["name"],
            age = data["age"],
            owner_id = data["owner_id"]
            
        )
        
        return JsonResponse({"message" : "정보등록완료"}, status = 201)
    
    