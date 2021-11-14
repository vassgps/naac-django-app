# adminapp/Utils/event.py
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import EventCreateForm
from ..models import EventUploader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

User = get_user_model()


@method_decorator(staff_member_required, name='dispatch')
class AllEvent(View):
    def get(self, request):
        event = EventUploader .objects.all()
        users = User.objects.filter(status=True)
        context = {'event': event, 'users': users}
        return render(request, "adminapp/event.html", context)


@method_decorator(staff_member_required, name='dispatch')
class EventCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': EventCreateForm()}
        return render(request, 'adminapp/event-create.html', context)

    def post(self, request, *args, **kwargs):
        form = EventCreateForm(request.POST)
        if form.is_valid():
            event = form.save()
            event.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully Created')
            return HttpResponseRedirect(reverse_lazy('adminapp:event'))
        return render(request, 'adminapp/event-create.html', {'form': form})


# Update Event
@method_decorator(staff_member_required, name='dispatch')
class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = EventUploader
    form_class = EventCreateForm
    success_message = "Successfully Updated"
    template_name = 'adminapp/event-update.html'

    def get_success_url(self):
        # view_name = 'listCriteria'
        return '{}#criteria'.format(reverse('adminapp:event'))

# Approve a event
@login_required()
def approveEvent(request, id):
    if request.method == 'POST':
        event = EventUploader.objects.get(id=id)
        event.status = True
        event.save()
        messages.add_message(request, messages.SUCCESS, 'Event Marked Successfully')
        return redirect('/adminapp/event')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Allowed')
        return redirect('/adminapp/event')


# Disable a User
@login_required()
def disableEvent(request, id):
    if request.method == 'POST':
        event = EventUploader.objects.get(id=id)
        event.status = False
        event.save()
        messages.add_message(request, messages.WARNING, 'Disabled Successfully')
        return redirect('/adminapp/event')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Allowed')
        return redirect('/adminapp/event')