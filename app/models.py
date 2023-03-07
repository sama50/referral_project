from django.db import models
from django.contrib.auth.models import User


class User_Details(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE,related_name='User_Details')
    referral_code = models.CharField(max_length=255,unique=True)
    user_count = models.BigIntegerField(default=0)
    referral_money = models.BigIntegerField(default=0)
     

class User_referral(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name='User_referral1')
    refer_by = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name='User_referral2')