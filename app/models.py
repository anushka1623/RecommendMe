from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class Customer(models.Model):
    FoodType = (
        ('Veg' , ' Veg'),
        ('NonVeg', 'NonVeg'),
        ('Both', 'Both')
    )

    CuisineType = (
        ('Indian','Indian'),
        ('Chinese', 'Chinese'),
        ('Thai', 'Thai'),
        ('Indonesian', 'Indonesian'),
        ('Italian', 'Italian'),
        ('Spanish', 'Spanish'),
        ('Japanese', 'Japanese'),
        ('Greece', 'Greece'),
        ('French', 'French'),
        ('Moroccan', 'Moroccan')
    )
    Username = models.CharField(max_length=300, null=True)
    password = models.CharField(max_length=300, null=True)
    FirstName= models.CharField(max_length=300, null=True)
    LastName= models.CharField(max_length=300, null=True)
    Location = models.TextField(null = True)
    foodtype = models.CharField(max_length=300, null=True, choices = FoodType)
    cuisinetype = MultiSelectField(null=True,choices = CuisineType)
    DateOfBirth = models.DateField(null= True)
    Email = models.EmailField(null = True)
    ProfilePic = models.ImageField(null = True)
    ContactNo = models.CharField(max_length=10, null=True)


    def __str__(self):
       return self.Username

class Hotel(models.Model):
    FoodType = (
        ('Veg' , ' Veg'),
        ('NonVeg', 'NonVeg'),
        ('Both', 'Both')
    )

    CuisineType = (
        ('Indian','Indian'),
        ('Chinese', 'Chinese'),
        ('Thai', 'Thai'),
        ('Indonesian', 'Indonesian'),
        ('Italian', 'Italian'),
        ('Spanish', 'Spanish'),
        ('Japanese', 'Japanese'),
        ('Greece', 'Greece'),
        ('French', 'French'),
        ('Moroccan', 'Moroccan')
    )
    HotelName = models.CharField(max_length=300, null=True)
    password = models.CharField(max_length=300, null=True)
    OpeningTime = models.TimeField(null= True)
    TopFoodItems = models.TextField(null = True)
    ClosingTime = models.TimeField(null= True)
    Location = models.TextField(null = True)
    foodtype = models.CharField(max_length=300, null=True, choices = FoodType)
    cuisinetype = MultiSelectField(null=True,choices = CuisineType)
    BusinessID = models.CharField(max_length=300, null=True)
    Email = models.EmailField(null = True)
    ProfilePic = models.ImageField(null = True)
    ContactNo = models.CharField(max_length=10, null=True)


    def __str__(self):
       return self.Username

