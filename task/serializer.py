from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from task.models import *


class TaskSerializer(serializers.ModelSerializer):
    customer_name = SerializerMethodField()

    def get_customer_name(self, ob):

        cat = Customer.objects.filter(id=ob.customer.id)
        if cat.count() > 0:

            return cat.first().full_name

        else:
            return None

    class Meta:
        model = Task
        fields = '__all__'



class CareTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareTasks
        fields = '__all__'


class MedicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medications
        fields = '__all__'

class RiskAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskAssessment
        fields = '__all__'

        
class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'