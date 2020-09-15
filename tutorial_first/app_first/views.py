from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee


def employeeView(request):
    # emp={
    #     'id': 123,
    #     'name': 'Anthony',
    #     'salary': 1000000,
    # }
    data = Employee.objects.all()
    response = {'employees': list(data.values('id','name', 'sal'))}
    return JsonResponse(response)
