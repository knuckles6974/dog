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
    
    
class DogandOwnerView(View):
    def get(self, request):
      result = []
      dogs = Dog.objects.all()
      
      for dog in dogs:
          owner = Owner.objects.get(id=dog.id)
          
          result.append({
              "id" : dog.owner.id,
              "first_name" : dog.owner.first_name,
              "last_name" : dog.owner.last_name,
              "age" : owner.age,
              "dog" : {
                "id" : dog.id, 
                "name" : dog.name,
                "age" : dog.age
              }
          })     
          
      return JsonResponse({"message": result}, status=201)  
    