# AdminApp/Utils/Criteria_Management

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.apps import apps
from .forms import MenuCreateForm, CriteriaUpdateForm, QuestionDataUpdateForm
from ..models import CriteriaManager, FinalCriteria
from ...user.models import AllUserScope

User = get_user_model()


class ManageCriteria(LoginRequiredMixin, View):
    def get(self, request):
        menu_obj = CriteriaManager.objects.filter(is_enabled=True).order_by('criteria')
        roles = AllUserScope.USER_SCOPES
        objects = []
        for obj in menu_obj:
            objects.append(obj)
        context = {'objects': objects, 'roles': roles}
        return render(request, "adminapp/manage_criteria.html", context)

    def post(self, request):
        try:
            role = request.POST.get('role')
            criterion = request.POST.get('criterion')
            crn = CriteriaManager.objects.get(pk=criterion)
            crn.assigned_role.set = role
            crn.save()
            msg = str(crn.criteria_id) + " is assigned to " + str(role) + " Successfully"
            messages.add_message(request, messages.SUCCESS, msg)
            return redirect('/adminapp/assign-criterion')
        except:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return redirect('/adminapp/assign-criterion')


# Approve a User
@login_required()
def approveCriteria(request, id):
    if request.method == 'POST':
        menu = CriteriaManager.objects.get(id=id)
        menu.is_active = True
        menu.save()
        messages.add_message(request, messages.SUCCESS, 'Approved Successfully')
        return redirect('/adminapp/assign-criterion')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Allowed')
        return redirect('/adminapp/assign-criterion')


# Disable a User
@login_required()
def disableCriteria(request, id):
    if request.method == 'POST':
        menu = CriteriaManager.objects.get(id=id)
        menu.is_active = False
        menu.save()
        messages.add_message(request, messages.WARNING, 'Disabled Successfully')
        return redirect('/adminapp/assign-criterion')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Allowed')
        return redirect('/adminapp/assign-criterion')


class CreateCriteria(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': MenuCreateForm()}
        return render(request, 'adminapp/criteria-create.html', context)

    def post(self, request, *args, **kwargs):
        form = MenuCreateForm(request.POST)
        if form.is_valid():
            club = form.save()
            club.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully Created')
            return HttpResponseRedirect(reverse_lazy('adminapp:assign-criterion'))
        return render(request, 'adminapp/criteria-create.html', {'form': form})


class CriteriaUpdateView(LoginRequiredMixin, UpdateView):
    model = CriteriaManager
    form_class = CriteriaUpdateForm
    template_name = 'adminapp/criteria-update.html'

    def get_success_url(self, ):
        # view_name = 'listCriteria'
        messages.add_message(self.request, messages.SUCCESS, 'Successfully Updated')
        return '{}#criteria'.format(reverse('adminapp:assign-criterion'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.object.criteria
        return context


# Delete a criterion - Currently Disabled
@login_required()
def deleteCriteria(request):
    if request.method == 'POST':
        try:
            criterion = request.POST.get('criteria_name')
            obj_id = request.POST.get('object_id')
            cr_index = criterion[1]
            app_name = 'criteria' + str(cr_index)
            model_class = apps.get_model(app_name, criterion)
            criteria_obj = model_class.objects.get(id=obj_id)
            criteria_obj.is_deleted = True
            criteria_obj.status = "OTHER"
            criteria_obj.save()
            messages.add_message(request, messages.WARNING, 'Delete Function Disabled for Security Purpose')

        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Error while deleting criterion !')
            print("Error :", e)
        return redirect(f'/criteria/{criterion}')

    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Allowed')
        return redirect('/adminapp/home')


class QuestionDataUpdateView(LoginRequiredMixin, UpdateView):
    model = FinalCriteria
    form_class = QuestionDataUpdateForm
    template_name = 'adminapp/criteria-update.html'

    def get_success_url(self, ):
        # view_name = 'listCriteria'
        messages.add_message(self.request, messages.SUCCESS, 'Successfully Updated')
        return '{}#criteria'.format(reverse('adminapp:update-questions'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.object.criteria
        return context


def display_questions(request):
    objects = FinalCriteria.objects.filter(is_active=True)
    context = {'objects':objects}
    return render(request, 'adminapp/display_data.html', context)
