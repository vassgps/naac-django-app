# Programs/Utils/Departments.py
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .forms import DeptCreateForm
from ..models import Departments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


@method_decorator(staff_member_required, name='dispatch')
class AllDepartment(View):
    def get(self, request):
        departments = Departments.objects.all()
        context = {'departments': departments}
        return render(request, "programs/departments.html", context)


@method_decorator(staff_member_required, name='dispatch')
class DeptCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': DeptCreateForm()}
        return render(request, 'programs/dept-create.html', context)

    def post(self, request, *args, **kwargs):
        form = DeptCreateForm(request.POST)
        if form.is_valid():
            dept = form.save()
            dept.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully Created')
            return HttpResponseRedirect(reverse_lazy('programs:departments'))
        return render(request, 'programs/dept-create.html', {'form': form})


# Update Criteria
@method_decorator(staff_member_required, name='dispatch')
class DeptUpdateView(LoginRequiredMixin, UpdateView):
    model = Departments
    form_class = DeptCreateForm
    success_message = "Successfully Updated"
    template_name = 'programs/department-update.html'

    def get_success_url(self):
        # view_name = 'listCriteria'
        return '{}#criteria'.format(reverse('programs:departments'))


# Approve a User
@staff_member_required(login_url='/accounts/login')
def approveDept(request, id):
    if request.method == 'POST':
        dept = Departments.objects.get(id=id)
        dept.status = True
        dept.save()
        messages.add_message(request, messages.SUCCESS, 'Approved Successfully')
        return redirect('/programs/departments')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/programs/departments')


# Disable a User
@staff_member_required(login_url='/accounts/login')
def disableDept(request, id):
    if request.method == 'POST':
        dept = Departments.objects.get(id=id)
        dept.status = False
        dept.save()
        messages.add_message(request, messages.WARNING, 'Disabled Successfully')
        return redirect('/programs/departments')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/programs/departments')
