# Adminapp/ User_management.py

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .forms import UserUpdateForm

User = get_user_model()


# List All Users

class AllUsers(LoginRequiredMixin, generic.View):
    # permission_required =
    def get(self, request):
        try:
            users = User.objects.filter(user_scope__in=['TEACHER', 'CLUB', 'DEPT_COD', 'OTHER']).order_by('-id')
            context = {'users': users}
        except:
            context = {'user':None}
            messages.add_message(request, messages.ERROR, 'User listing failed')
        return render(request, 'adminapp/list_users.html', context)


# Approve a User
@login_required()
def approveUser(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.status = True
        user.save()
        messages.add_message(request, messages.SUCCESS, 'User Approved Successfully')
        return redirect('adminapp:allusers')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/adminapp/allusers/')


# Disable a User
@login_required()
def disableUser(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.status = False
        user.save()
        messages.add_message(request, messages.ERROR, 'User Disabled Successfully')
        return redirect('adminapp:allusers')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/adminapp/allusers/')


# List All Active Users
@login_required()
def activeUsers(request):
    users = User.objects.filter(status=True, user_scope__in=['TEACHER', 'CLUB', 'DEPT_COD', 'OTHER']).order_by('-id')
    context = {'users': users}
    return render(request, 'adminapp/active_users.html', context)


# List All Pending Users
@login_required()
def pendingUsers(request):
    users = User.objects.filter(status=False, user_scope__in=['TEACHER', 'CLUB', 'DEPT_COD', 'OTHER']).order_by('-id')
    context = {'users': users}
    return render(request, 'adminapp/pending_users.html', context)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "user/edit_user.html"
    success_url = '/adminapp/allusers/'

    def get_success_url(self):
        return '{}#adminapp'.format(reverse('adminapp:allusers'))

    def form_valid(self, form):
        if str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.SUCCESS, "User profile Updated")
            return super(UserUpdateView, self).form_valid(form)
        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(UserUpdateView, self).get_form_kwargs(*args, **kwargs)
        # kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        context["user"] = User.objects.get(id=pk)
        return context

@login_required()
def deleteUser(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.is_active = False
        user.is_verified = False
        user.status = False
        user.save()
        messages.add_message(request, messages.ERROR, 'User Deleted Successfully')
        return redirect('adminapp:pendingusers')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/adminapp/allusers/')

# Approve or Disable user and redirect to same page

# Approve a User
@login_required()
def approveUserPage(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.status = True
        user.save()
        messages.add_message(request, messages.SUCCESS, 'User Approved Successfully')
        return redirect('adminapp:pendingusers')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/adminapp/allusers/')


# Disable a User
@login_required()
def disableUserPage(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.status = False
        user.save()
        messages.add_message(request, messages.ERROR, 'User Disabled Successfully')
        return redirect('adminapp:activeusers')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/adminapp/allusers/')