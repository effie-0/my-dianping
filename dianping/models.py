from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200,default='')
    telephone = models.CharField(max_length=20,default='')
    region = models.CharField(max_length=10,default='')
    category = models.CharField(max_length=10,default='')
    latitude = models.DecimalField(max_digits=10, decimal_places=6,default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=6,default=0)
    avg_rating = models.FloatField(default=-1)
    product_grade = models.FloatField(default=0)
    decoration_grade = models.FloatField(default=0)
    service_grade = models.FloatField(default=0)
    avg_price = models.IntegerField(default=0)
    review_count = models.IntegerField(default=0)
    popular_dishes = models.CharField(max_length=1000,default='')
    sale_text = models.CharField(max_length=200,default='')
    recommend_text = models.CharField(max_length=200,default='')
    photo_url = models.CharField(max_length=200, default='')
    star = models.FloatField(default=0)
    shop_id = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name
"""
class DianpingUser(models.Model):
    user = models.OneToOneField(User, related_name='dianpinguser')
    telephone = models.CharField(max_length=35)
    starred_list = models.ManyToManyField('Business')

    def __str__(self):
        return self.name

@receiver(post_save, sender = User)
def create_user_dianpinguser(sender, instance, created, **kwargs):
    if created:
        DianpingUser.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_user_dianpinguser(sender, instance, **kwargs):
    instance.dianping_user.save()
"""

class Review(models.Model):
    business = models.ForeignKey('Business', related_name='business_review')
    author = models.CharField(max_length=20, default='')
    author_id = models.CharField(max_length=15, default='')
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    excerpt = models.TextField(default='')
    content = models.TextField(default='')
    grade = models.FloatField(default=-1)
    review_id = models.CharField(max_length=15, default='')
    photo_url = models.CharField(max_length=200, default='')
    #user = models.ForeignKey('DianpingUser', related_name='review_user', default=None)

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
    business = models.ForeignKey('Business')

class Message(models.Model):
    sender = models.ForeignKey(DianpingUser,related_name='sender')
    receiver = models.ForeignKey(DianpingUser, related_name='receiver')
    title = models.CharField(max_length=50)
    content = models.TextField()
    read = models.BooleanField()
    
    def __str__(self):
        return self.title
        """
