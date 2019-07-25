# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# our piece of code....
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from assignment1.models import sampleTable

def test_view(requests):
    response = {"message": "API Working Successfully"}
    return JsonResponse(response)

@csrf_exempt

def sample_db_test(requests):
    print(requests.method)
    if(requests.method=='GET'):

        response_obj =sampleTable.objects.all()

        response={"data":[]}
        for i in response_obj:
            response["data"].append({"parking_slotname":i.parking_slotname , "parking_floor":i.parking_floor , "parking_nearest":i.parking_nearest})

        return JsonResponse(response)
    elif(requests.method=="POST"):
        response = {"message": "POST method Working Successfully"}
        request_body=json.loads(requests.body)
        sampleTable.objects.create(**request_body)


        return JsonResponse(response)


