from django.shortcuts import render

from .models import Profession, Sector


def list(request):
    template_name = 'profession/list.html'
    sectors = Sector.objects.all()

    selected_sector = request.GET.get('sector')

    if selected_sector:
        professions = Profession.objects.filter(sector__title=selected_sector)
    else:
        professions = Profession.objects.all()

    context = {
        'professions': professions,
        'sectors': sectors,
    }

    return render(request, template_name, context)
