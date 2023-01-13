from django.db import models
from django.http import JsonResponse
# Create your models here.

class MeasurerHistory(models.Model):
    uuid = models.ForeignKey(
        "apirest.Measurer", 
        verbose_name="Measurer historical model", 
        on_delete=models.CASCADE
        )
    consumption = models.FloatField(default=0)
    modification_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"({self.uuid}) {dir(self.uuid)}"
class Measurer(models.Model):
    """
Description
-----------
    Measurer model, saves an instance and updates it every time
    (Not a historical model, check MeasurerHistory for that).
    """
    uuid = models.UUIDField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=255)
    consumption = models.BigIntegerField(default=0)
    last_modification = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.consumption < 0:
            return JsonResponse({"error": "Consumption can not be a negative value"})
        else:
            super(Measurer, self).save(*args, **kwargs)
            MeasurerHistory(uuid=self, consumption=self.consumption).save()
        return True
    
    def __str__(self):
        return f"({self.uuid}) {self.uuid}"