from django.db import models
from django.utils import timezone

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    region = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longtitude = models.DecimalField(max_digits=10, decimal_places=6)
    avg_rating = models.FloatField()
    product_grade = models.FloatField()
    decoration_grade = models.FloatField()
    service_grade = models.FloatField()
    avg_price = models.IntegerField()
    review_count = models.IntegerField()
    hours = models.CharField(max_length=100)
    popular_dishes = []  #todo
    #photo_url, s_photo_url, photo_count, photo_list_url
    has_takeaway = models.BooleanField()
    has_online_reservation = models.BooleanField()
    recommend_text = models.CharField(max_length=200)

class User(models.Model):
    name = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)  #?
    browsed_list = models.ManyToManyField('Business')

    def __str__(self):
        return self.name

class Review(models.Model):
    bussiness = models.ForeignKey('Business')
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    excertpt = models.CharField(max_length=50)
    grade = models.FloatField()

    def __str__(self):
        return self.excertpt

class Request(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longtitude = models.DecimalField(max_digits=10, decimal_places=6)
    radius = models.IntegerField()
    region = models.CharField(max_length=10)
    catagory = models.CharField(max_length=10)
    keyword = models.CharField(max_length=50)
    sort = models.IntegerField()
    business = models.ForeignKey('Business')

class Message(models.Model):
    sender = models.ForeignKey(User,related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    title = models.CharField(max_length=50)
    content = models.TextField()
    read = models.BooleanField()

    def __str__(self):
        return self.title