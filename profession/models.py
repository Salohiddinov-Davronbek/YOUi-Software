from django.db import models

# Create your models here.




class Car_business(models.Model):
    car_businesss = models.CharField(max_length=100, verbose_name="Профессия")

    def __str__(self):
        return '%s' %(self.car_businesss)

    class Meta:
        verbose_name = '1. Автомобильный бизнес'
        verbose_name_plural = '1. Автомобильный бизнес'

# /////////////////////////////////////////////////////////////////////////////////////////










