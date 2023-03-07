from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from app.models import User_Details , User_referral
import uuid
# Create your views here.

def index(request):
    
    if request.method =='POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        referralcode = request.POST.get('referralcode')
        user = User.objects.create_user(username, email,password)

        if referralcode !="":
            if  User_Details.objects.filter(referral_code=referralcode).exists():

                get_referral_user = User_Details.objects.get(referral_code=referralcode)
                get_referral_user.referral_money = get_referral_user.referral_money+100 
                get_referral_user.user_count = get_referral_user.user_count+1  
                get_referral_user.save() 

                User_referral(user=user,refer_by=get_referral_user.user).save()
                User_Details(user=user,referral_code=uuid.uuid4(),referral_money=0).save()

                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('home')

        
    return render(request,'index.html')

def home(request):
    if request.user.is_authenticated:

        all_user_ref = User_referral.objects.filter(refer_by=request.user)
        user_data = User_Details.objects.get(user=request.user)
        
        return render(request,'home.html' ,{'all_user_ref':all_user_ref,'user_data':user_data})
    else:
        return redirect('index')