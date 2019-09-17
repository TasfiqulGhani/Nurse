from django.db import models
from django.utils import timezone

from user.models import Customer, Employee


class Task(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200, default='')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default='')
    lat = models.FloatField(max_length=100, null=False, blank=False)
    lon = models.FloatField(max_length=100, null=False, blank=False)
    entry_note = models.CharField(max_length=200, default='')
    deadline = models.DateTimeField(default=timezone.now)
    notes = models.CharField(max_length=200, default='')
    isDone = models.BooleanField(default=False)
    isStarted = models.BooleanField(default=False)
    done_time = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)


class Medications(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    is_done = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)


class RiskAssessment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False)
    note = models.CharField(max_length=200, default='')
    date = models.DateTimeField(default=timezone.now)


class CareTasks(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    is_done = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
