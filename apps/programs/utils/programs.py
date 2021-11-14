# Programs/Utils/Departments.py
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views import generic, View
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .forms import ProgramCreateForm
from ..models import Program
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# from django.shortcuts import get_object_or_404

# List all Programs or Corces
@method_decorator(staff_member_required, name='dispatch')
class AllPrograms(View):
    def get(self, request):
        programs = Program.objects.all()
        context = {'programs': programs}
        return render(request, "programs/programs.html", context)


@method_decorator(staff_member_required, name='dispatch')
class PrgmCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': ProgramCreateForm()}
        return render(request, 'programs/program-create.html', context)

    def post(self, request, *args, **kwargs):
        form = ProgramCreateForm(request.POST)
        if form.is_valid():
            dept = form.save()
            dept.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully Created')
            return HttpResponseRedirect(reverse_lazy('programs:programs'))
        return render(request, 'programs/program-create.html', {'form': form})


# Update Criteria
@method_decorator(staff_member_required, name='dispatch')
class ProgramUpdateView(LoginRequiredMixin, UpdateView):
    model = Program
    form_class = ProgramCreateForm
    success_message = "Successfully Updated"
    template_name = 'programs/program-update.html'

    def get_success_url(self):
        # view_name = 'listCriteria'
        return '{}#criteria'.format(reverse('programs:programs'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



# Approve a User
@staff_member_required(login_url='/accounts/login')
def approvePrgm(request, id):
    if request.method == 'POST':
        prgm = Program.objects.get(id=id)
        prgm.status = True
        prgm.save()
        messages.add_message(request, messages.SUCCESS, 'Approved Successfully')
        return redirect('/programs/programs')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/programs/programs')


# Disable a User
@staff_member_required(login_url='/accounts/login')
def disablePrgm(request, id):
    if request.method == 'POST':
        prgm = Program.objects.get(id=id)
        prgm.status = False
        prgm.save()
        messages.add_message(request, messages.WARNING, 'Disabled Successfully')
        return redirect('/programs/programs')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/programs/programs')
