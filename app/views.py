from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_topic(request):
    sno=int(input('Enter No.'))
    topic_name=input('Enter name')
    TO=Topic.objects.get_or_create(sno=sno, topic_name=topic_name)[0]
    TO.save()
    return HttpResponse(request, 'Topic data inserted successfully')


def insert_webpage(request):
    sno=int(input('Enter No.'))
    topic_name=input('Enter name')
    player_ID=int(input('Enter ID'))
    player_name=input('Enter Player Name')
    TO=Topic.objects.get_or_create(sno=sno, topic_name=topic_name)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO, player_ID=player_ID, player_name=player_name)[0]
    WO.save()
    return HttpResponse(request, 'Webpage is inserted')

def insert_about(request):
    sno=int(input('Enter No.'))
    topic_name=input('Enter name')
    player_ID=int(input('Enter ID'))
    player_name=input('Enter Player Name')
    Jersey_No=int(input('Enter No.'))
    country=input('Enter Country Name')
    TO=Topic.objects.get_or_create(sno=sno, topic_name=topic_name)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO, player_ID=player_ID, player_name=player_name)[0]
    WO.save()
    AO=About.objects.get_or_create(player_name=WO, Jersey_No=Jersey_No, country=country)[0]
    AO.save()
    return HttpResponse(request, 'About is created')





