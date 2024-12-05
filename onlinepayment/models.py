from django.db import models

class Register(models.Model):
    Name=models.CharField(default="",max_length=100)
    Email=models.CharField(default="",max_length=100)
    Mobile=models.CharField(default="",max_length=100)
    Password=models.CharField(default="",max_length=100)
    Address=models.CharField(default="",max_length=100)
    def __str__(self) -> str:
        return self.Name
class History(models.Model):
    Orderid=models.CharField(default="",max_length=100)
    Amount=models.CharField(default="",max_length=100)
    Time=models.CharField(default="",max_length=100)
    Date=models.CharField(default="",max_length=100)
    Email=models.CharField(default="",max_length=100)
    Status=models.CharField(default="",max_length=100)
class test(models.Model):
    Orderid=models.CharField(default="",max_length=100)