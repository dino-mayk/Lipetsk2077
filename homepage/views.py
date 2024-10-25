from django.shortcuts import render

from profession.models import Profession


def index(request):
    template_name = 'homepage/index.html'
    first_professions = Profession.objects.all()[:3]

    context = {
        'first_professions': first_professions,
    }

    return render(request, template_name, context=context)
