from django.db import models
from django.utils import timezone


class my_details(models.Model):
    greeting1 = models.CharField(max_length=50)
    greeting2 = models.CharField(max_length=50)
    my_name = models.CharField(max_length=50)
    my_image = models.ImageField(upload_to="uploads/")
    def __str__(self):
        return f"'{self.greeting1}' '{self.greeting2}' '{self.my_name}' '{self.my_image}'"
class Project(models.Model):
    name = models.CharField(max_length=80, null=True)
    photo = models.ImageField(upload_to="uploads/")
    describe = models.TextField(max_length=500, null=True, blank=True)
    link = models.TextField(max_length=800, null=True, blank=True)
    def __str__(self):
        return f" '{self.name}' '{self.photo}' '{self.describe}' '{self.link}'"

class Icon(models.Model):
    call_icon = models.ImageField(upload_to="uploads/")
    def __str__(self):
        return f"'{self.call_icon}'"
class Doc(models.Model):
    file = models.FileField(upload_to="uploads/")
    def __str__(self):
        return f" '{self.file}'"