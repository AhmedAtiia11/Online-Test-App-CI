from django.shortcuts import render,HttpResponse
from django.http import JsonResponse


def healthy(request):
    # response={"msg":"healthy"}
    return JsonResponse({"msg":"healthy"})
# Create your views here.
