from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid

class User_Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  id_user = models.IntegerField()
  phone_number = models.TextField(max_length=10)
  county = models.TextField(max_length=30)
  city = models.TextField(max_length=30)
  town = models.TextField(max_length=30)
  street = models.TextField(max_length=30)
  House_no = models.TextField(max_length=30)
  profileimg = models.ImageField(upload_to='User_profile_images', default='man.png')
  date_created = models.DateTimeField(default=datetime.now())

  def __str__(self):
    return f"{self.user} - {self.county}"

class Pizza(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  name = models.TextField(max_length=30)
  pizza_type = models.TextField(max_length=10)
  no_of_toppings = models.IntegerField()
  small = models.IntegerField()
  large = models.IntegerField()
  itemimg = models.ImageField(upload_to='Item_images', default='not-found.png')

  def __str__(self):
    return f'{self.name} - {self.pizza_type}'

class Topping(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  name = models.TextField(max_length=30)
  price = models.IntegerField()
  itemimg = models.ImageField(upload_to='Item_images', default='not-found.png')

  def __str__(self):
    return self.name

class Sub(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  name = models.TextField(max_length=30)
  price_small = models.IntegerField()
  price_large = models.IntegerField()
  itemimg = models.ImageField(upload_to='Item_images')

  def __str__(self):
    return self.name

class Dinner_platter(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  name = models.TextField(max_length=30)
  price_small = models.IntegerField()
  price_large = models.IntegerField()
  itemimg = models.ImageField(upload_to='Item_images', default='not-found.png')

  def __str__(self):
    return self.name

class Salad(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  name = models.TextField(max_length=30)
  price = models.IntegerField()
  itemimg = models.ImageField(upload_to='Item_images', default='not-found.png')

  def __str__(self):
    return self.name

class Pasta(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  name = models.TextField(max_length=30)
  price = models.IntegerField()
  itemimg = models.ImageField(upload_to='Item_images', default='not-found.png')

  def __str__(self):
    return self.name

class Order(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  status = models.TextField(max_length=10, default="Active")

class Order_items(models.Model):
  item = models.TextField(max_length=20)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=0)
  amount = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.item}-{self.user}"