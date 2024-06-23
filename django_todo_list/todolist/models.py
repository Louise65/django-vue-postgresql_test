from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class dailyTasks(models.Model):
    
    dailyTaskID = models.AutoField(primary_key=True)
    dailyTask_name = models.TextField()
    dailyStartTime = models.TimeField(auto_now=False, auto_now_add=False)
    dailyEndTime = models.TimeField(auto_now=False, auto_now_add=False)
    dailyTaskPriority = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1)
        ]
    )
    dailyTaskStatus = models.BooleanField(default=False)

    #return task title
    def __str__(self):
        return self.dailyTask_name