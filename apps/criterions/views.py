# Apps/Criterions/views.py

from django.shortcuts import render, redirect
from ..adminapp.models import FinalCriteria
from django.db.models import Q
from ..programs.models import Subject  # Form Making Cascad Menu
from .models import CriterionMaster
from .fields.field_names import all_field_keys, all_field_values


# Create your views here.

def index(request):
    context = {}
    return render(request, 'criterions/index.html', context)


# Show Detailed view of enterd data in criterion Tables
def detailed_view(request, slug, id):
    try:
        obj = CriterionMaster.objects.get(id=id)
        fld = all_field_keys[slug]
        val = all_field_values[slug]
        fields = {}
        context = {'obj': obj, 'field_dict': val}
    except:
        context = {}
    return render(request, f"criteria/tables/{slug}.html", context)


# Normal search
def search(request):
    query = request.GET.get('query', '')
    criterion = FinalCriteria.objects.filter(
        Q(final_title__icontains=query) | Q(final_description__icontains=query) | Q(keywords__icontains=query))
    if str(request.user.user_scope) in ("NAAC_COD", "CLUB", "ADMIN"):
        return render(request, 'criterions/search2.html', {'criterion': criterion, 'query': query})
    else:
        return render(request, 'criterions/search.html', {'criterion': criterion, 'query': query})


# AJAX Load Cascad Menu
def load_subject(request):
    program_id = request.GET.get('program_id')
    papers = Subject.objects.filter(program_id=program_id).all()
    return render(request, 'criterions/dropdown_list_options.html', {'papers': papers})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
