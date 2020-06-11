from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):                                               #one to one bec a user can have one customer and vice versa
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)     #the relationship is w user,Cascade means when user is deleted ,delete the relationship
    Name = models.CharField(max_length=200 , null=True)
    Mobile = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
         return self.Name
class Tag(models.Model):
    Name = models.CharField(max_length=200 , null=True)
    def __str__(self):
         return self.Name
class product(models.Model):
    CATEGORY = (
        ('indoor' , 'Indoor') ,
        ('Outdoor' , 'Outdoor'),
    )
    Name = models.CharField(max_length=200 , null=True)
    Price = models.FloatField(null=True)
    Category = models.CharField(max_length=200 , null=True , choices=CATEGORY)
    Description = models.CharField(max_length=200 , null=True, blank=True)
    Date_Created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
         return self.Name

class order(models.Model):
    STATUS = (
        ('Pending' , 'Pending'),
        ('Out For Delivery' , 'Out For Delivery'),
        ('Delivered' ,'Delivered' )
    )
    Date_Created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200 ,null=True,choices=STATUS)
    Customers = models.ForeignKey(Customer,null= True,on_delete=models.SET_NULL )
    Product = models.ForeignKey(product,null= True,on_delete=models.SET_NULL )

    def __str__(self):
        return self.Product.Name
