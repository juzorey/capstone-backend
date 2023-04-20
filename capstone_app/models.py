from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    weight = None
    USERNAME_FIELD = 'email'
    # we want to log in with an email and a password and not the django default of username and password (see if we can change this!)
    REQUIRED_FIELDS = []



# class User(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=300)
#     email = models.EmailField()
#     name = models.CharField(max_length = 200)
#     weight = models.IntegerField(default=0, null=True)


# class FoodCtg(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
    
# default drop down of 3 catg
class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Food')
    food_name = models.CharField(max_length=100)
    image_url = models.TextField(null=True, blank = True)
    # category = models.ForeignKey(FoodCtg, on_delete=models.CASCADE)
    calories = models.IntegerField(null=True, blank = True)

    def __str__(self):
        return self.name









class Fitness(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Fitness', default = 0, blank = True)
    fitness_name = models.CharField(max_length= 255)
    duration = models.IntegerField(default=0, null=True)
    img_url = models.CharField(max_length=300)

    def __str__(self):
        return self.name

