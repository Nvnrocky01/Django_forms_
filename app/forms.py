from django import forms
from app.models import *

class Topicform(forms.Form):
    topic_name=forms.CharField()



class Webpageform(forms.Form):
    tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField()
    url=forms.URLField()


class Accessrecordform(forms.Form):
    wl=[[wo.pk,wo.name] for wo in Webpage.objects.all()]
    name=forms.ChoiceField(choices=wl)
    author=forms.CharField()
    date=forms.DateField()




class WebpageRform(forms.Form):
    tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name=forms.MultipleChoiceField(choices=tl,widget=forms.SelectMultiple)
    


class AccessrecordRform(forms.Form):
    wl=[[wo.pk,wo.name] for wo in Webpage.objects.all()]
    name=forms.MultipleChoiceField(choices=wl,widget=forms.SelectMultiple)   

    
