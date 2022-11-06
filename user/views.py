from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

# Create your views here.
def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        resim = request.FILES['resim']
        tel = request.POST['tel']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']

        if sifre1 == sifre2:
            if User.objects.filter(username = kullanici).exists():
                messages.error(request, 'Kullanıcı adı zaten alınmış')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email kullanımda')
                return redirect('register')
            elif     len(sifre1) < 6:
                messages.error(request, 'Şifre en az 6 karakter olması gerekiyor')
                return redirect('register')
            elif kullanici in sifre1:
                messages.error(request, 'Şifre ile kullanıcı adı benzer olamaz')
                return redirect('register')
            else:
                user = User.objects.create_user(username = kullanici, email = email, password = sifre1)
                Account.objects.create( 
                user = user,
                resim = resim,
                tel = tel
                )
                user.save()
                messages.error(request, 'Kullanıcı oluşturuldu')
                return redirect('login')         
        else:
            messages.error(request, 'Şifreler uyuşmuyor')
            return redirect('register')
    return render(request, 'register.html')        

def userLogin(request):
    next = ''
    if request.GET:
        next = request.GET['next']
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']
        #sifre = request.POST.get['sifre']
        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Yaptınız')
            if next == '':
                return redirect('index')
            else:
                return redirect(next)    
        else:
            messages.error(request, 'Kullanici adı veya şifre hatalı')
            return redirect('login')
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı')
    return redirect('index')


def hesap(request):
    user = request.user.account
    context = {
        'user':user,
        
    }
    return render(request, 'hesap.html', context)

def userDelete(request):
    user = request.user
    user.delete()
    messages.success(request, 'Kullanıcı Silindi')
    return redirect('index')






















