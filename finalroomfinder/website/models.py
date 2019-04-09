from django.db import models

# Create your models here.
from django.db.models import AutoField


class RegisterModel(models.Model):
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	image=models.ImageField(upload_to="media/")


	class Meta:
                db_table="users"
                def __str__(self):
                        return self.username


class ItemModel(models.Model):
    id=AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    image1 = models.ImageField(upload_to="media/")
    image2 = models.ImageField(upload_to="media/")
    image3 = models.ImageField(upload_to="media/")
    price = models.CharField(max_length=100)
    buildingtype = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    postedon = models.CharField(max_length=100)
    postedby = models.CharField(max_length=100)

    class Meta:
        db_table = "posts"

    def __str__(self):
        return self.title
