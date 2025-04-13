from django.contrib import admin
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import TokenProxy

# Register your models here.
admin.site.register(User)
admin.site.register(Token)
admin.site.unregister(TokenProxy)   ##Django registers this internally. Unregistered to eliminate two Tokens table on Admin portal.