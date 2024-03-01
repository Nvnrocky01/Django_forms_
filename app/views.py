from django.shortcuts import render

# Create your views here.

from app.models import *
from app.forms import *

def topic(request):
    etfo=Topicform()
    d={'etfo':etfo}
    if request.method=='POST':
        tfdo=Topicform(request.POST)
        if tfdo.is_valid():
            tn=tfdo.cleaned_data['topic_name']
            to=Topic.objects.get_or_create(topic_name=tn)[0]
            to.save()
            qlto=Topic.objects.all()
            d1={'topic':qlto}
            return render(request,'display_topic.html',d1)

    return render(request,'djtopic.html',d)




def webpage(request):
    ewfo=Webpageform()
    d={'ewfo':ewfo}
    if request.method=='POST':
        wfdo=Webpageform(request.POST)
        if wfdo.is_valid():
            tn=wfdo.cleaned_data['topic_name']
            tO=Topic.objects.get(topic_name=tn)
            n=wfdo.cleaned_data['name']
            u=wfdo.cleaned_data['url']
            wo=Webpage.objects.get_or_create(topic_name=tO,name=n,url=u)[0]
            wo.save()

            qlwo=Webpage.objects.all()
            d1={'webpage':qlwo}
            return render(request,'display_webpage.html',d1)
    return render(request,'djwebpage.html',d)




def accessrecord(request):
    eafo=Accessrecordform()
    d={'eafo':eafo}
    if request.method=='POST':
        afdo=Accessrecordform(request.POST)
        if afdo.is_valid():
            pk=afdo.cleaned_data['name']
            wo=Webpage.objects.get(pk=pk)
            au=afdo.cleaned_data['author']
            da=afdo.cleaned_data['date']
            ao=AcessRecord.objects.get_or_create(name=wo,author=au,date=da)[0]
            ao.save()

            qlao=AcessRecord.objects.all()
            d1={'accessrecord':qlao}
            return render(request,'display_accessrecord.html',d1)

    return render(request,'djaccessrecord.html',d)



def select_multiple_webpage(request):
    ewfo=WebpageRform()
    d={'ewfo':ewfo}
    if request.method=='POST':
        topiclist=request.POST.getlist('topic_name')
        qlwo=Webpage.objects.none() 
        for tn in topiclist:
            qlwo=qlwo|Webpage.objects.filter(topic_name=tn)
        d1={'webpage':qlwo}
        return render(request,'display_webpage.html',d1)

    return render(request,'multiple_webpage.html',d)


def select_multiple_accessrecord(request):
    eafo=AccessrecordRform()
    d={'eafo':eafo}
    if request.method=='POST':
        wepagelist=request.POST.getlist('name')
        qlwo=AcessRecord.objects.none()
        for wo in wepagelist:
            qlwo=qlwo|AcessRecord.objects.filter(name=wo)  
        d1={'accessrecord':qlwo}
        return render(request,'display_accessrecord.html',d1)
    return render(request,'djaccessrecord.html',d)
