from django.conf.urls import url, include
from django.db import router
from rest_framework.routers import SimpleRouter

from task.views import *
from user.views import get_cares, get_medications, get_medications_check, get_cares_check, get_files

router = SimpleRouter()

router.register('task', TaskViewSet, 'TaskViewSet')
router.register('caretasks', CareTasksViewSet, 'CareTasksViewSet')
router.register('medications', MedicationsViewSet, 'MedicationsViewSet')

urlpatterns = [
    # url('', include(router.urls), name='router'),
    url(r'^api/', include(router.urls), name='api'),
    url('employee/cares/', get_cares, name='get-tasks-get_cares'),
    url('employee/files/', get_files, name='get-tasks-get_cares'),
    url('employee/medications/', get_medications, name='get-tasks-list'),
    url('employee/medicationscheck/', get_medications_check, name='get-tasks-list'),
    url('employee/carescheck/', get_cares_check, name='get-tasks-list'),

]

