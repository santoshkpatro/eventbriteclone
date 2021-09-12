from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from .forms import AddEventForm


@login_required(login_url='login')
def event_add(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('index')
        else:
            messages.warning(request, 'Something went wrong while filling up the form!')
    return render(request, 'events/add.html')


def event_details(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        context = {
            'event': event
        }
        return render(request, 'events/details.html', context)
    except Event.DoesNotExist:
        messages.warning(request, 'Something went wrong!')
        return redirect('index')


@login_required(login_url='login')
def event_delete(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        if not event.user == request.user:
            messages.warning(request, 'Something went wrong!')
            return redirect('index')
        event.delete()
    except Event.DoesNotExist:
        messages.warning(request, 'Something went wrong!')
    return redirect('index')


@login_required(login_url='login')
def event_like(request, event_id):
    next_url = request.GET['next']
    try:
        event = Event.objects.get(id=event_id)
        event.likes.add(request.user)
        return redirect(next_url)
    except Event.DoesNotExist:
        messages.warning(request, 'Something went wrong!')
        return redirect(next_url)


@login_required(login_url='login')
def event_like_remove(request, event_id):
    next_url = request.GET['next']
    try:
        event = Event.objects.get(id=event_id)
        event.likes.remove(request.user)
        return redirect(next_url)
    except Event.DoesNotExist:
        messages.warning(request, 'Something went wrong!')
        return redirect(next_url)
