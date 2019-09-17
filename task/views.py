from django.shortcuts import render
from rest_framework import viewsets
from task.models import *
from task.serializer import *


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CareTasksViewSet(viewsets.ModelViewSet):
    queryset = CareTasks.objects.all()
    serializer_class = CareTasksSerializer


class MedicationsViewSet(viewsets.ModelViewSet):
    queryset = Medications.objects.all()
    serializer_class = MedicationsSerializer


class RiskAssessmentViewSet(viewsets.ModelViewSet):
    queryset = RiskAssessment.objects.all()
    serializer_class = RiskAssessmentSerializer
