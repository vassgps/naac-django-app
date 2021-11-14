# Adminapp / Views.py
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date
from .models import FinalCriteria, EventUploader, CriteriaManager
from ..programs.models import Departments,Clubs, Program, Subject
from .summury import getUserCriteria

User = get_user_model()
today = date.today()  # Get Today date


# Create your views here.
@staff_member_required(login_url='/accounts/login')
def index(request):
    return redirect('adminapp:home')


# Admin Home
@method_decorator(staff_member_required, name='dispatch')
class AdminHome(View):
    def get(self, request):
        user = request.user
        total_criteria = CriteriaManager.objects.filter(is_enabled=True).count()
        total_events = EventUploader.objects.all().count()
        total_users = User.objects.filter(is_staff=False).count()
        joined_today = User.objects.filter(created_at__contains=today).count()
        active_criteria = CriteriaManager.objects.filter(is_enabled=True, is_active=True).count()
        assigned_for_naac = getUserCriteria(user)
        total_clubs = Clubs.objects.filter(status=True).count()
        total_dept = Departments.objects.filter(status=True).count()
        total_programs = Program.objects.filter(status=True).count()
        total_paper = Subject.objects.filter(status=True).count()

        if str(user.user_scope) in ["NAAC_COD", "STAFF", "ADMIN"]:
            context = {'user': user, 'total_criteria': total_criteria, 'total_events': total_events,
                       'total_users': total_users, 'joined_today': joined_today, 'active_criteria': active_criteria,
                       'assigned_for_naac': assigned_for_naac,'total_clubs': total_clubs, 'total_dept': total_dept,
                       'total_programs': total_programs,'total_paper': total_paper}
            return render(request, "adminapp/home.html", context)
        else:
            messages.add_message(request, messages.WARNING, 'User NOT Allowed to Access Admin panel')
            return redirect('/accounts/login/')

    def post(self, request):
        pass


@staff_member_required(login_url='/accounts/login')
def reportGeneration(request):
    cr_data = CriteriaManager.objects.filter(is_enabled=True).order_by('ordering')
    context = {'user': request.user, 'cr_data': cr_data}
    return render(request, "adminapp/reports.html", context)


@method_decorator(staff_member_required, name='dispatch')
class GeneralSettings(LoginRequiredMixin, View):
    def get(self, request):
        context = {'user': request.user, }
        return render(request, "adminapp/settings.html", context)

    def post(self, request):
        pass


@method_decorator(staff_member_required, name='dispatch')
class AllDepartment(View):
    def get(self, request):
        departments = Departments.objects.all()
        context = {'departments': departments}
        return render(request, "adminapp/departments.html", context)


@method_decorator(staff_member_required, name='dispatch')
class AllPrograms(View):
    def get(self, request):
        return redirect('programs:programs')


@method_decorator(staff_member_required, name='dispatch')
class AllPapers(View):
    def get(self, request):
        return redirect('programs:subjects')


@method_decorator(staff_member_required, name='dispatch')
class AllClubs(View):
    def get(self, request):
        return redirect('programs:club')


@method_decorator(staff_member_required, name='dispatch')
class AllBatch(View):
    def get(self, request):
        return redirect('programs:batch')
