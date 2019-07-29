from django.http import JsonResponse
from rest_framework.views import APIView





class UserView(APIView):


    def get(self,requests):
        print(requests.GET)
        Response={"success":True,"message":"GET API WORKING SUSCCEFULLY"}
        return JsonResponse(Response)
    def post(self,requests):
        print(requests.data)
        Response = {"success": True, "message": "POST API WORKING SUSCCEFULLY"}
        return JsonResponse(Response)
