from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .utils import butcher
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def api(request):
    if request.method == 'GET':
        return JsonResponse(butcher.generate_butchered_quote())
    elif request.method == 'POST':
        return JsonResponse(request.POST.get('quote'))
        
    return HttpResponse("bad request")