import json

from django.views     import View
from .models          import Owner
from django.http      import JsonResponse


# Create your views here.
class DogsandownerView(View):
    def post(self, request):
        data = json.loads(request.body)

        Owner.objects.create(
            dog=data["dog_name"],
            type=data["type"],
            name=data["owner_name"],
                                
        )
        
        return JsonResponse({"message" : "댕댕이 등록완료"}, status = 201)