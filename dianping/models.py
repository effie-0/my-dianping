from django.db import models
from django.utils import timezone

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=50)
    #branch_name = models.CharField(max_length=50,default = '')
    address = models.CharField(max_length=200,default='')
    telephone = models.CharField(max_length=20,default='')
    region = models.CharField(max_length=10,default='')
    category = models.CharField(max_length=10,default='')
    latitude = models.DecimalField(max_digits=10, decimal_places=6,default=0)
    longtitude = models.DecimalField(max_digits=10, decimal_places=6,default=0)
    avg_rating = models.FloatField(default=0)
    product_grade = models.FloatField(default=0)
    decoration_grade = models.FloatField(default=0)
    service_grade = models.FloatField(default=0)
    avg_price = models.IntegerField(default=0)
    review_count = models.IntegerField(default=0)
    #hours = models.CharField(max_length=100,default = '')
    popular_dishes = models.CharField(max_length=100,default='')
    #s_photo_url, photo_count, photo_list_url
    has_takeaway = models.CharField(max_length=100, default='')
    has_online_reservation = models.CharField(max_length=100, default='')
    recommend_text = models.CharField(max_length=200,default='')
    photo_url = models.CharField(max_length=200, default='')
    star = models.FloatField(default=0)
    shop_id = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)  #?
    browsed_list = models.ManyToManyField('Business')

    def __str__(self):
        return self.name

class Review(models.Model):
    business = models.ForeignKey('Business')
    author = models.CharField(max_length=20, default='')
    author_id = models.CharField(max_length=15, default='')
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    excertpt = models.CharField(max_length=50, default='')
    content = models.TextField(default='')
    grade = models.FloatField(default=-1)
    review_id = models.CharField(max_length=15, default='')
    photo_url = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.excertpt

"""class MyRequest(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longtitude = models.DecimalField(max_digits=10, decimal_places=6)
    radius = models.IntegerField()
    region = models.CharField(max_length=10)
    catagory = models.CharField(max_length=10)
    keyword = models.CharField(max_length=50)
    sort = models.IntegerField()
    business = models.ForeignKey('Business')"""

class Message(models.Model):
    sender = models.ForeignKey(User,related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    title = models.CharField(max_length=50)
    content = models.TextField()
    read = models.BooleanField()

    def __str__(self):
        return self.title
