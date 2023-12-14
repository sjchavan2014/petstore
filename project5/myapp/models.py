from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

# Create your models here.
class Django_sagar(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.ImageField(upload_to=' images',null=True,blank=True)
    time = models.TimeField(auto_now_add=True)
    gender = models.CharField(max_length=40,default=False)
    English = models.BooleanField(default=False)
    Hindi = models.BooleanField(default=False)
    Marathi = models.BooleanField(default=False)
    city = models.CharField(max_length=100,default=False)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Django_sagar = models.ForeignKey(Django_sagar,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1,null=True)

class Address(models.Model):
    city = models.CharField(max_length=100,null=True)
    pincode = models.IntegerField()
    state = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    #product = models.ForeignKey(Django_sagar,on_delete=models.CASCADE,null=True)
    


class  Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Django_sagar = models.ForeignKey(Django_sagar,on_delete=models.CASCADE, null=True)
    Cart = models.ForeignKey(Cart,on_delete=models.CASCADE , null=True)
    time = models.TimeField(auto_now=True, null=True)
    data = models.DateField(auto_now_add=True,null=True)
    Order_id = models.CharField(max_length=100, null=True,unique=True)
    address = models.ForeignKey(Address,on_delete=models.CASCADE,null=True)


    def save(self,*args,**kwargs):
        if not self.Order_id:
            current_time = timezone.now()
            Order_id = f"{current_time.strftime('%Y%d%m%H%M%S')}--{uuid.uuid4().hex[:5]}"
            self.Order_id = Order_id
        super().save(*args,**kwargs)

    