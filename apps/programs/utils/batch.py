# Programs/Utils/batch.py
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import BatchCreateForm
from ..models import Batch
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

User = get_user_model()


@method_decorator(staff_member_required, name='dispatch')
class AllBatch(View):
    def get(self, request):
        batch = Batch.objects.all().order_by('batch_no')
        users = User.objects.filter(status=True)
        context = {'batch': batch, 'users': users}
        return render(request, "programs/batch.html", context)


@method_decorator(staff_member_required, name='dispatch')
class BatchCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': BatchCreateForm()}
        return render(request, 'programs/batch-create.html', context)

    def post(self, request, *args, **kwargs):
        form = BatchCreateForm(request.POST)
        if form.is_valid():
            batch = form.save()
            batch.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully Created')
            return HttpResponseRedirect(reverse_lazy('programs:batch'))
        return render(request, 'programs/batch-create.html', {'form': form})


# Update Criteria
@method_decorator(staff_member_required, name='dispatch')
class BatchUpdateView(LoginRequiredMixin, UpdateView):
    model = Batch
    form_class = BatchCreateForm
    success_message = "Successfully Updated"
    template_name = 'programs/batch-update.html'

    def get_success_url(self):
        # view_name = 'listCriteria'
        return '{}#criteria'.format(reverse('programs:batch'))

# Approve a User
@login_required()
def approveBatch(request, id):
    if request.method == 'POST':
        batch = Batch.objects.get(id=id)
        batch.status = True
        batch.save()
        messages.add_message(request, messages.SUCCESS, 'Approved Successfully')
        return redirect('/programs/batch')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/programs/batch')


# Disable a User
@login_required()
def disableBatch(request, id):
    if request.method == 'POST':
        batch = Batch.objects.get(id=id)
        batch.status = False
        batch.save()
        messages.add_message(request, messages.WARNING, 'Disabled Successfully')
        return redirect('/programs/batch')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/programs/batch')