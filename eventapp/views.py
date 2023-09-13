from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import Apllicationform
# Create your views here.
def index(request):
    events=Event.objects.all()
    context={
        'events':events
    }
    return render(request,"eventapp/index.html",context)
    
def page(request,pk):
    eventss=Event.objects.all()
    for event in eventss:
        if event.pk==pk:
            req_event=event
    if request.method == 'POST':
        form=Apllicationform(request.POST)
        if form.is_valid():
            participant=form.save(commit=False)
            participant.event = req_event
            participant.save()
    
    form=Apllicationform()
    content={
        'event': req_event,
        'form' : form
    }
    return render(request,"eventapp/page.html",content)