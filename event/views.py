from django.shortcuts import render

from event.models import Event

def list(request):
    template_name = 'event/list.html'
    events = Event.objects.all()

    event_type = request.GET.get('event_type')

    if event_type == "Оффлайн":
        event_type = 2
    if event_type == "Онлайн":
        event_type = 1

    if event_type:
        print(events[0].event_type)
        print(event_type)
        print('#####################')
        events = Event.objects.filter(event_type=event_type)
    else:
        events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, template_name, context)