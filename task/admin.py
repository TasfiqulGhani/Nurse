from django.contrib import admin

from task.models import *

admin.site.register(Files)
admin.site.register(CareTasks)
admin.site.register(Medications)
admin.site.register(Task)
admin.site.register(RiskAssessment)
admin.site.register(Notes)
admin.site.register(EmployeeLocation)

admin.site.register(DNR)


