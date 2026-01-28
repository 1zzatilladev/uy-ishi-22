from django.db import models

class CocaCola(models.Model):
    class VolumeMl(models.TextChoices):
        ML_330 = '330', '330 ml'
        ML_500 = '500', '500 ml'
        ML_1000 = '1000', '1 L'
        ML_1500 = '1500', '1.5 L'
        ML_2000 = '2000', '2 L'

    name = models.CharField(max_length=34)
    stock = models.IntegerField(default=0)
    price = models.IntegerField()
    description = models.CharField(max_length=233, blank=True, null=True)
    volume_ml = models.CharField(
        max_length=10,
        choices=VolumeMl.choices,
        default=VolumeMl.ML_500
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.volume_ml} ml"
