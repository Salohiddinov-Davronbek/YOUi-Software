from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField


# UMUMIY TEKSHIRUV MODELI USERNAME, PASSWORD
class User(AbstractUser):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)    
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = '1. All users Database'
        verbose_name_plural = '1. All users Database'
# ////////////////////////////////////////////////////////////////////////////
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# MODEL FAQAT ADMINISTRATOR UCHUN  
class Useradminpage(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    father_name = models.CharField(max_length=60)
    admin_image = models.ImageField(null=True, blank=True, upload_to='images/') 

    
    class Meta:
        verbose_name = '2. Database for Administrators'
        verbose_name_plural = '2. Database for Administrators'
# //////////////////////////////////////////////////////////////////////////////////////////
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# MODEL FAQAT ADMINISTRATOR UCHUN  
class Vacancies(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    father_name = models.CharField(max_length=60)
    phone_numer = models.CharField(max_length=10)
    name_company = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    
    class Meta:
        verbose_name = '2. Database for Vacancies'
        verbose_name_plural = '2. Database for Vacancies'
# /////////////////////////////////////////////////////////////////////////////////////////
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\






# MODEL FAQAT ADMINISTRATOR UCHUN  
class Summaries(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    father_name = models.CharField(max_length=60, blank=True)
    summary_image_u = models.ImageField(null=True, blank=True, upload_to='images')

    
    class Meta:
        verbose_name = '3. Database for Summary'
        verbose_name_plural = '3. Database for Summary'
# /////////////////////////////////////////////////////////////////////////////////////////
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\