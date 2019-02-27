from django.db import models

# Create your models here.
class Emp(models.Model):
    userid=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    fullname=models.CharField(max_length=30)
    mailid=models.CharField(max_length=30)
    address=models.CharField(max_length=30)

    def __str__(self):
        return self.userid+","+self.password+","+self.fullname+","+self.mailid+","+self.address