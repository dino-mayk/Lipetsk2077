from django.shortcuts import redirect, render

from feedback import forms, models


def index(request):
    template = 'feedback/index.html'

    form = forms.FormFeedback(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        form.save()
        return redirect('feedback:done')

    return render(request, template, context)


def done(request):
    template = 'feedback/done.html'
    return render(request, template)


def list(request):
    template_name = 'feedback/list.html'
    feedbacks = models.Feedback.objects.all()[::-1]

    context = {
        'feedbacks': feedbacks,
    }

    return render(request, template_name, context)
