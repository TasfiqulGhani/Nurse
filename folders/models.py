from django.db import models
from django.utils import timezone

# Create your models here.
from user.models import Employee


class ApplicationForm(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name


class CV(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name


class JobDescription(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name


class InterviewNotes(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name


class JobOfferLetter(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name


class IdentityDocuments(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name


class DBSChecks(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name


class RightToWorkRecordscks(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name


class References(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name


class TrainingRecords(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name


class NewStarterPack(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name


class Supervisions(models.Model):
    document = models.FileField(upload_to='documents/', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'document'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee.full_name
