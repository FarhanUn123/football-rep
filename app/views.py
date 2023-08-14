from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Lat_news, Nex_match, Ranking, Video, Blog, Score, Event, Comment, Video2, Comment2, Blog2

def index(request):
    ln=Lat_news.objects.all()
    nm=Nex_match.objects.all()
    rg=Ranking.objects.all()
    vo=Video.objects.all()
    bg=Blog.objects.all()
    se=Score.objects.all()
    et=Event.objects.all()
    return render(request, 'index.html', {'ln':ln, 'nm':nm, 'rg':rg, 'vo':vo, 'bg':bg, 'se':se, 'et':et})

def matches(request):
    nm=Nex_match.objects.all()
    vo=Video.objects.all()
    bg=Blog.objects.all()
    se=Score.objects.all()
    return render(request, 'matches.html', {'nm':nm, 'vo':vo, 'bg':bg, 'se':se})

def players(request):
    vo2=Video2.objects.all()
    bg=Blog.objects.all()
    return render(request, 'players.html', {'vo2':vo2, 'bg':bg})

def blog(request):
    bg=Blog.objects.all()

    return render(request, 'blog.html', {'bg':bg})

@csrf_exempt
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        ct3=Comment2(name=name, email=email, subject=subject, message=message)
        ct3.save()
        return redirect('contact')
    return render(request, 'contact.html')
    
@csrf_exempt
def single(request):
    if request.method=='POST':
        name=request.POST.get('name')
        image=request.FILES.get('image')
        time=request.POST.get('time')
        message=request.POST.get('message')
        ct=Comment(name=name, image=image, time=time, message=message)
        ct.save()
        return redirect('single')
    ln=Lat_news.objects.all()
    bg=Blog.objects.all()
    bg2=Blog2.objects.all()
    ct2=Comment.objects.all()
    return render(request, 'single.html',{'ln':ln, 'bg':bg, 'ct2':ct2, 'bg2':bg2})