from django.shortcuts import render
from main.models import Company, HomePage, Slider, Message, AboutPage
from django.db.models import Q, Count

def home(request):
    error = None
    success = None
    if request.method == "POST":
        try:
            Message.objects.create(
                name = request.POST['name'],
                email = request.POST['email'],
                subject = request.POST['subject'],
                message = request.POST['message']
            )
            success = "ثبت شد"
        except:
            error = "اطلاعات را به صورت صحیح وارد کنید"

    sub_companies = Company.objects.filter(subs__isnull=False).values_list('subs', flat=True)
    objs = Company.objects.exclude(id__in=sub_companies)[:6]
    sliders = Slider.objects.all()
    return render(request,'home.html', {'objs':objs, 'sliders':sliders, 'error':error, 'success': success})

def company(request, pk):
    obj = Company.objects.get(pk=pk)
    return render(request,'company.html', {'obj':obj})

def companies(request):
    sub_companies = Company.objects.filter(subs__isnull=False).values_list('subs', flat=True)
    objs = Company.objects.exclude(id__in=sub_companies)
    return render(request,'companies.html', {'objs':objs})

def about(request):
    page = AboutPage.objects.first()
    return render(request,'about.html', {'page':page})

def master(request):
    return {
        'info': HomePage.objects.first()
    }