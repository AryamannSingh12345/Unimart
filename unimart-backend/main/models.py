from django.db import models
from django.contrib.auth.models import User
#tabel user_details
# class user_details(models.Model):
#     id = models.AutoField(primary_key = True)
#     email_id = models.CharField(max_length=64, unique = True, db_index= True, null = False)
#     first_name = models.CharField(max_length=64, null = False)
#     last_name = models.CharField(max_length=64, null = False)
#     hashed_password = models.CharField(max_length=64, null = False)

#table seller_post
class seller_post(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null= True)
    product_name = models.CharField(max_length=64, db_index=True, null = False)
    price = models.IntegerField()
    exchange_items = models.CharField(max_length = 64)
    img = models.ImageField(upload_to='photos', null=False)
    image_name = models.CharField(max_length=128)
    product_description = models.TextField()
    preferred_location = models.TextField()
    preferred_contact = models.CharField(max_length = 64)
    date = models.DateField(auto_now=True)

#table buyer_post
class buyer_post(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null= True)
    product_name = models.CharField(max_length=64, db_index=True, null=False)
    budget_range = models.CharField(max_length= 64)
    preferred_location = models.TextField()
    preference_details = models.TextField()
    preferred_contact = models.CharField(max_length = 64)
    date = models.DateField(auto_now=True)

#table feedback
class feedback(models.Model):
    id = models.AutoField(primary_key = True)
    email_id = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    message = models.TextField()
