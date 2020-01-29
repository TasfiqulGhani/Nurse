from django.conf.urls import url
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

from django.core.files.storage import FileSystemStorage
from task.models import Task, CareTasks, Medications, RiskAssessment, Notes, EmployeeLocation, DNR, Files
from task.serializer import TaskSerializer, CareTasksSerializer, MedicationsSerializer, RiskAssessmentSerializer, \
    NotesSerializer, EmployeeLocationSerializer, DNRSerializer, FilesSerializer
from user.models import *
from user.serializer import *

from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DNRViewSet(viewsets.ModelViewSet):
    queryset = DNR.objects.all()
    serializer_class = DNRSerializer


@api_view(['POST'])
def employee_login(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email)
            print(password)
            employee = Employee.objects.filter(email=email, password=password)

            if employee.count() > 0:
                employee = Employee.objects.filter(email=email, password=password)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(data=EmployeeSerializer(employee, many=True).data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        employee = Employee.objects.filter(email__contains=email, password__contains=password)

        if employee.count() > 0:
            employee = Employee.objects.filter(email__contains=email, password__contains=password)
            return Response(data=EmployeeSerializer(employee, many=True).data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def customer_login(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email)
            print(password)
            customer = Customer.objects.filter(email=email, password=password)

            if customer.count() > 0:
                customer = Customer.objects.filter(email=email, password=password)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(data=CustomerSerializer(customer, many=True).data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_cares(request):
    # try:
    if request.method == 'GET':
        task_id = request.GET.get('id')
        cares = CareTasks.objects.filter(task=task_id)
        return Response(data=CareTasksSerializer(cares, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_files(request):
    if request.method == 'GET':
        task_id = request.GET.get('id')
        cares = Files.objects.filter(task=task_id)
        return Response(data=FilesSerializer(cares, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cares_check(request):
    # try:
    if request.method == 'GET':
        care_id = request.GET.get('id')
        cares = CareTasks.objects.get(id=care_id)
        cares.is_done = True
        cares.save()
        return Response(data='', status=status.HTTP_200_OK)


@api_view(['GET'])
def get_medications_check(request):
    if request.method == 'GET':
        med_id = request.GET.get('id')
        is_done = request.GET.get('is_done')
        is_excused = request.GET.get('is_excused')
        med = Medications.objects.get(id=med_id)
        med.is_excused = is_excused
        med.is_done = is_done
        med.save()
    return Response(data='', status=status.HTTP_200_OK)


@api_view(['GET'])
def get_medications(request):
    if request.method == 'GET':
        task_id = request.GET.get('id')
        cares = Medications.objects.filter(task=task_id)
        return Response(data=MedicationsSerializer(cares, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_tasks(request):
    try:
        if request.method == 'GET':
            employee_id = request.GET.get('id')
            tasks = Task.objects.filter(employee_id__exact=employee_id)

            return Response(data=TaskSerializer(tasks, many=True).data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_tasks_customer(request):
    try:
        if request.method == 'GET':
            customer_id = request.GET.get('id')
            tasks = Task.objects.filter(customer_id__exact=customer_id)

            return Response(data=TaskSerializer(tasks, many=True).data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def simple_upload(request):
    url(r'^upload/$', simple_upload, name='upload'),
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        return Response({'url': 'http://3.18.112.196:8001' + uploaded_file_url}, status=status.HTTP_201_CREATED)
    return Response({'result': 'Only Post Requ'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_risks(request):
    try:
        if request.method == 'GET':
            task_id = request.GET.get('id')
            risks = RiskAssessment.objects.filter(task_id__exact=task_id)

            return Response(data=RiskAssessmentSerializer(risks, many=True).data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_notes(request):
    try:
        if request.method == 'GET':
            task_id = request.GET.get('id')
            risks = Notes.objects.filter(task_id__exact=task_id)

            return Response(data=NotesSerializer(risks, many=True).data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class EmployeeLocationViewSet(viewsets.ModelViewSet):
    queryset = EmployeeLocation.objects.all()
    serializer_class = EmployeeLocationSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
