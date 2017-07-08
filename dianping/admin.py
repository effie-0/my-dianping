from django.contrib import admin
from .models import User, Review, Profile
#from .models import Message, DianpingUser

# Register your models here.
#admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Review)