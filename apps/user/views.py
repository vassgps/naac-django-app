# User/Views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages, auth
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignUpForm, CustomUserChangeForm, UpdatePasswordForm
from ..adminapp.models import CriteriaManager
from ..adminapp.summury import getUserCriteria, userSummury
from ..programs.models import Clubs


# Create your views here.

def index(request):
    return HttpResponse("Welcome to User App")


@login_required(login_url='/accounts/login/')
def home(request):
    user = request.user
    if str(user.user_scope) in ("ADMIN", "STAFF", "NAAC_COD"):
        return redirect("adminapp:home")
    try:
        total_criterions = CriteriaManager.objects.filter(is_active=True, is_enabled=True).count()
        assigned_criterion = getUserCriteria(user)
        data_input = userSummury(user)
        user_input = data_input['enterd_count']
        pending_input = data_input['pending_count']
    except:
        total_criterions = 0
        assigned_criterion = 0
        data_input = 0
        user_input = 0
        pending_input = 0
    context = {'user': user, 'total_criterions': total_criterions, 'assigned_criterion': assigned_criterion,
               'user_input':user_input, 'pending_input':pending_input}
    return render(request, "user/home.html", context)


class GetLogin(View):
    def get(self, request):
        return redirect('/accounts/login/')


# Logout function
def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    django_logout(request)
    return redirect('user:login')


# User Registrations.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Account Created Successfully')
            return redirect('user:home')
    else:
        form = SignUpForm()
    return render(request, 'user/register.html', {'form': form})


# Update User Profile
class UpdateUser(LoginRequiredMixin, View):
    def get(self, request):
        form = CustomUserChangeForm(instance=request.user)
        context = {'form': form}
        return render(request, "user/update_profile.html", context)

    def post(self, request):
        current_user = request.user
        form = CustomUserChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            current_user.save()  # Save the Updated User Details
            messages.add_message(request, messages.SUCCESS, 'User Profile Updated Successfully')
            return redirect('user:home')
        else:
            return render(request, "user/update_profile.html", {'form': form})


# Change User Password
class ChangePassword(LoginRequiredMixin, View):

    def post(self, request):
        current_user = request.user
        form = UpdatePasswordForm(current_user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user:home')
        else:
            return render(request, 'user/update_password.html', {'form': form})

    def get(self, request):
        form = UpdatePasswordForm(request.user)
        return render(request, 'user/update_password.html', {'form': form})


# Criteria Management
class Criterion(generic.View):

    def get(self, request, cid):  # CID - Criteria ID
        print("Criters ID :", cid)
        return HttpResponse("Crietria ID is ", cid)

    def post(self, request, cid):  # CID - Criteria ID
        print("Criters ID :", cid)
        return HttpResponse("Crietria ID is ", cid)


# Assign Criterion Menu Based on User roles
# class LoadMenu(LoginRequiredMixin, APIView):
#
#     def get(self, request, format=None):
#         user_scope = request.user.user_scope
#         queryset = MenuItems.objects.filter(assigned_role=user_scope)
#         serializer = MenuSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         pass


# Change to Club role
class ClubManagement(LoginRequiredMixin, View):
    def get(self, request, id):
        user = request.user
        if id == 0:
            if user.is_teacher:
                user.user_scope = "TEACHER"
                # user.clubs = None
                msg = "Your current role is assigned to TEACHER Successfully"
            else:
                msg = "Your role cannot be set as TEACHER"
                messages.add_message(request, messages.ERROR, msg)
                return redirect('user:home')
        else:
            user.user_scope = "CLUB"
            club = Clubs.objects.get(id=id)
            user.clubs = club
            msg = "Your current role is assigned to Clubs & Forum's  Successfully"
        user.save()
        messages.add_message(request, messages.INFO, msg)
        return redirect('user:home')

    def post(self, request):
        pass
