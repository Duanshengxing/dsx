from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class LearnAOp(MiddlewareMixin):
    def process_request(self,request):
       print(request.path)
