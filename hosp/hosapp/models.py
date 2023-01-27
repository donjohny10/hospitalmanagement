from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()
    
class Doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=100)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    dep_image=models.ImageField(upload_to='doctors')