# Programs /Views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Program


# Create your views here.

def home(request):
    return HttpResponse("Welcome to App Home ..!")


# AJAX Load Cascad Menu
def load_programs(request):
    department_id = request.GET.get('department_id')
    programs = Program.objects.filter(department_id=department_id).all()
    return render(request, 'programs/dropdown_list_options.html', {'programs': programs})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
