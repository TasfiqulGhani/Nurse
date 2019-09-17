from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from task.views import RiskAssessmentViewSet
from user.views import EmployeeViewSet, CustomerViewSet, UserViewSet, employee_login, get_tasks, get_risks

router = SimpleRouter()

router.register('employee', EmployeeViewSet, 'review')
router.register('customer', CustomerViewSet, 'fuel')
router.register('user', UserViewSet, 'station')
router.register('risk', RiskAssessmentViewSet, 'risk')

urlpatterns = [
    # url('', include(router.urls), name='router'),
    url(r'^api/', include(router.urls), name='api'),
    url('employee/login/', employee_login, name='history-list'),
    url('employee/tasks/', get_tasks, name='get-tasks-list'),
    url('employee/risk/', get_risks, name='get-get_risks-list'),

]
