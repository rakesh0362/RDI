from django.db import models

class HotMetal(models.Model):
    date = models.DateField()
    castNo = models.CharField(max_length=10)

    tlcNo = models.IntegerField()
    silicon = models.DecimalField(decimal_places=2, max_digits=3)
    sulphur = models.DecimalField(decimal_places=3, max_digits=4)
    manganese = models.DecimalField(decimal_places=3, max_digits=4)
    phosphorus = models.DecimalField(decimal_places=3, max_digits=4)
    hmTemperature = models.IntegerField()
    receiveTime = models.TimeField()
    reportTime = models.TimeField()


