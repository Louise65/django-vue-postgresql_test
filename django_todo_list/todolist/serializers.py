from rest_framework import routers, serializers, viewsets
from todolist.models import dailyTasks

class dailyTasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dailyTasks
        fields=['dailyTaskID', 'dailyTask_name', 'dailyStartTime', 'dailyEndTime', 'dailyTaskPriority', 'dailyTaskStatus']