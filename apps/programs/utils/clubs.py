# Programs/Utils/clubs.py
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import ClubCreateForm
from ..models import Clubs
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

User = get_user_model()


@method_decorator(staff_member_required, name='dispatch')
class AllClub(View):
    def get(self, request):
        clubs = Clubs.objects.all().order_by('id')
        users = User.objects.filter(status=True)
        context = {'clubs': clubs, 'users': users}
        return render(request, "programs/clubs.html", context)


@method_decorator(staff_member_required, name='dispatch')
class ClubCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': ClubCreateForm()}
        return render(request, 'programs/club-create.html', context)

    def post(self, request, *args, **kwargs):
        form = ClubCreateForm(request.POST)
        if form.is_valid():
            club = form.save()
            club.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully Created')
            return HttpResponseRedirect(reverse_lazy('programs:clubs'))
        return render(request, 'programs/club-create.html', {'form': form})


# Update Criteria
@method_decorator(staff_member_required, name='dispatch')
class ClubUpdateView(LoginRequiredMixin, UpdateView):
    model = Clubs
    form_class = ClubCreateForm
    success_message = "Successfully Updated"
    template_name = 'programs/club-update.html'

    def get_success_url(self):
        # view_name = 'listCriteria'
        return '{}#criteria'.format(reverse('programs:club'))


# Approve a User
@login_required()
def approveClub(request, id):
    if request.method == 'POST':
        club = Clubs.objects.get(id=id)
        club.status = True
        club.save()
        messages.add_message(request, messages.SUCCESS, 'Approved Successfully')
        return redirect('/programs/club')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/programs/club')


# Disable a User
@login_required()
def disableClub(request, id):
    if request.method == 'POST':
        club = Clubs.objects.get(id=id)
        club.status = False
        club.save()
        messages.add_message(request, messages.WARNING, 'Disabled Successfully')
        return redirect('/programs/club')
    else:
        messages.add_message(request, messages.ERROR, 'Method NOT Alowed')
        return redirect('/programs/club')


@staff_member_required(login_url='/accounts/login')
def assignClub(request):
    if request.method == 'POST':
        try:
            clb = request.POST.get('clubs')
            usr = request.POST.get('users')
            club = Clubs.objects.get(id=clb)
            user = User.objects.filter(pk=usr)
            club.user.set(user)
            club.save()
            username = User.objects.get(pk=usr)
            msg = str(club.name) + " is assigned to " + str(username) + " Successfully"
            messages.add_message(request, messages.SUCCESS, msg)
            return redirect('/programs/club')
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return redirect('/programs/club')

    else:
        messages.add_message(request, messages.WARNING, 'Method NOT Allowed')
        return redirect('/programs/club')

