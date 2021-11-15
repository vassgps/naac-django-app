# Subjects/Utils/Departments.py
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .forms import SubjectCreateForm
from ..models import Subject
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


# from django.shortcuts import get_object_or_404

# List all Subjects or Corces
@method_decorator(staff_member_required, name='dispatch')
class AllSubjects(View):
    def get(self, request):
        Subjects = Subject.objects.all().order_by('id')
        context = {'Subjects': Subjects}
        return render(request, "programs/subjects.html", context)


@method_decorator(staff_member_required, name='dispatch')
class SbjtCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': SubjectCreateForm()}
        return render(request, 'programs/subject-create.html', context)

    def post(self, request, *args, **kwargs):
        form = SubjectCreateForm(request.POST)
        if form.is_valid():
            dept = form.save()
            dept.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully Created')
            return HttpResponseRedirect(reverse_lazy('programs:subjects'))
        return render(request, 'programs/subject-create.html', {'form': form})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(SbjtCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs


# Update Criteria
@method_decorator(staff_member_required, name='dispatch')
class SubjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Subject
    form_class = SubjectCreateForm
    success_message = "Successfully Updated"
    template_name = 'programs/subject-update.html'

    def get_success_url(self):
        # view_name = 'listCriteria'
        return '{}#criteria'.format(reverse('programs:subjects'))


# Approve a User
@staff_member_required(login_url='/accounts/login')
def approveSbjt(request, id):
    if request.method == 'POST':
        sbjt = Subject.objects.get(id=id)
        sbjt.status = True
        sbjt.save()
        messages.add_message(request, messages.SUCCESS, 'Approved Successfully')
        return redirect('/programs/subjects')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/programs/subjecs')


# Disable a User
@staff_member_required(login_url='/accounts/login')
def disableSbjt(request, id):
    if request.method == 'POST':
        sbjt = Subject.objects.get(id=id)
        sbjt.status = False
        sbjt.save()
        messages.add_message(request, messages.WARNING, 'Disabled Successfully')
        return redirect('/programs/subjects')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/programs/subjects')
