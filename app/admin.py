from django.contrib import admin
from app.models import User_Details , User_referral
# Register your models here.

@admin.register(User_Details)
class User_DetailsAdmin(admin.ModelAdmin):
    list_display = ('id','user','referral_code')

@admin.register(User_referral)
class User_referralAdmin(admin.ModelAdmin):
    list_display =('id','user','refer_by')


