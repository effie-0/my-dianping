from django.contrib import admin
from .models import User, Review, Message

# Register your models here.
admin.site.register(Message)
admin.site.register(User)
admin.site.register(Review)