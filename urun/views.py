from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages
# Create your views here.

def index(request):
    urunler = Urun.objects.all()
    kategoriler = Kategori.objects.all()

    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(
            Q(isim__icontains = search) |
            Q(kategori__isim__icontains = search)
        )
        
    context = {
        'urunler':urunler,
        'search':search,
        'kategoriler':kategoriler
    }
    return render(request, 'index.html', context)


def urun(request, urunId):
    urun = Urun.objects.filter(id = urunId)
    context = {
        'urun':urun

    }
    return render(request, 'urun.html', context)

# blog yapıcaktım sonra e ticaret sitesinde işi ne diyip kampanyalı ürüne çevirdim .d
def ucuz(request):
    ucuz = Ucuz.objects.all()
    context = {
        'ucuz':ucuz
    }
    return render(request, 'ucuz.html', context)  

def olustur(request):
    form = UrunForm()
    if request.method == 'POST':
        form = UrunForm(request.POST, request.FILES)
        if form.is_valid():
            urun = form.save(commit=False)
            urun.olusturan = request.user
            urun.save()
            messages.success(request, 'Ürününüz Oluşturuldu')
            return redirect('index')
    context  = {
        'form':form
    }
    return render(request, 'olustur.html', context)


def alisveris(request):
    return render(request, 'alisveris.html')



        