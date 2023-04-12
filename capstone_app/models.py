from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    email = models.EmailField()
    name = models.CharField(max_length = 200)
    weight = models.IntegerField(default=0, null=True)

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Food', default = 0, blank = True)
    food_name = models.CharField(max_length=100)
    image_url = models.TextField(null=True, blank = True)

    def __str__(self):
        return self.name

class Fitness(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Fitness', default = 0, blank = True)
    fitness_name = models.CharField(max_length= 255)
    duration = models.IntegerField(default=0, null=True)
    img_url = models.CharField(max_length=300)

    def __str__(self):
        return self.name

