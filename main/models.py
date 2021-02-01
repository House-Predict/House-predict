from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="property",null=True)
    posted_by=models.CharField(max_length=10)
    under_construction=models.BooleanField()
    rera=models.BooleanField()
    rooms=models.PositiveSmallIntegerField()
    room_type=models.CharField( max_length=4)
    area=models.DecimalField(max_digits=20, decimal_places=10)
    ready_to_move=models.BooleanField()
    resale=models.BooleanField()
    location=models.CharField(max_length=100)
    loc_long=models.DecimalField( max_digits=14, decimal_places=10)
    loc_lat=models.DecimalField( max_digits=14, decimal_places=10)
    price=models.DecimalField( max_digits=15, decimal_places=5)

    def __str__(self):
        return str(self.id)

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.TextField()

    def __str__(self):
        return self.name + "-" +  self.email