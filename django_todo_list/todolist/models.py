from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class dailyTasks(models.Model):
    
    dailyTaskID = models.AutoField(primary_key=True)
    dailyTask_name = models.TextField()
    dailyTimeHr = models.IntegerField(
        default=8,
        validators=[
            MaxValueValidator(23),
            MinValueValidator(0)
        ]
    )
    dailyTimeMin = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(59),
            MinValueValidator(0)
        ]
    )
    dailyTaskStatus = models.BooleanField(default=False)

    #return task title
    def __str__(self):
        return self.dailyTask_name