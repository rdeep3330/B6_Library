from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
# print("in models.py")
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    # is_active = models.CharField(max_length=1, default="Y")

    class Meta:
        db_table = "book"

    def __str__(self):
        return f"{self.name}"



# sessions, auth, contenttypes, admin --- built in 
# book -- user defined app


class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  

    class Meta:
        db_table = "emp"

    def __str__(self):
        return f"{self.first_name}"


class Company(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255)
    

#     class Meta:
#         db_table = "company"


# class ProductVideo(models.Model):
#     video = models.CharField(max_length=100, null=True)
    
#     class Meta:
#         db_table = "company"
