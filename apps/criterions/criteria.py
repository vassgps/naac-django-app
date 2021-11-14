# CR1 /Views.py
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import HttpResponse
from ..adminapp.models import FinalCriteria, CriteriaManager
from .models import CriterionMaster
# Test import
from .fields.field_names import all_field_values


def home(request):
    return HttpResponse("Welcome to App Home ..!")


# Unknown Function
def listTables(request, slug):
    obj_list = CriterionMaster.objects.all()
    ktest = ('date', 'url1', 'text1')
    context = {'object_list': obj_list, 'data_dict': "dc1_1_1"}
    return render(request, f"criteria/tables/c1_1_1.html", context)


# Display The List of Criteria
@login_required()
def show_criteria(request, slug):
    current_user = request.user
    user_dept = current_user.department
    cr_index = slug[1]
    data_dict = {}
    try:
        for key, value in all_field_values.items():
            if key == slug: data_dict.update(value)
    except:
        messages.add_message(request, messages.ERROR, "Table Headers Loading failed!")
        return render(request, "criterions/error.html")

    try:
        cid = FinalCriteria.objects.get(criteria_id=slug)  # Get Exact Criterion Object based on current page
        criteria_manager = CriteriaManager.objects.get(criteria=slug)  # Get Assigned Criteria details
    except Exception as ex:
        return render(request, "criterions/error.html")

    # Check for user and criterion permissions
    if not criteria_manager.is_enabled:
        messages.add_message(request, messages.ERROR, "This criterion is not Enabled by Administrator..!")
        return render(request, "criterions/error.html")
    if not criteria_manager.is_active:
        messages.add_message(request, messages.ERROR, "This criterion is Disabled..!")
        return render(request, "criterions/error.html")
    if not current_user.status:
        messages.add_message(request, messages.ERROR, "User not Activated !")
        return redirect('user:home')

    # Display All criteria to NAAC Coordinator with Add Button
    if str(current_user.user_scope) in ("NAAC_COD", "STAFF"):
        object_list = CriterionMaster.objects.filter(criterion=slug, is_deleted=False).order_by('-id')
        add_button = True
        show_tab = True
        context = {'object_list': object_list, 'cid': cid, 'add_button': add_button,
                   "show_tab": show_tab, 'data_dict': data_dict}
        return render(request, f"criteria/list_table.html", context)

    # Display All Table to Department Coordinator and Add button is only for Assigned criterions
    elif str(current_user.user_scope) == "DEPT_COD":
        if criteria_manager.DEPT_COD:
            object_list = CriterionMaster.objects.filter(criterion=slug, is_deleted=False,
                                                         program__department=user_dept).order_by('-id')
            add_button = True
            context = {'object_list': object_list, 'cid': cid, 'add_button': add_button}
            return render(request, f"criteria/list_table.html", context)
        else:
            object_list = CriterionMaster.objects.filter(criterion=slug, is_deleted=False,
                                                         program__department=user_dept).order_by('-id')
            add_button = False
            show_tab = True
            hide_table = False
            context = {'object_list': object_list, 'cid': cid, 'add_button': add_button,
                       "show_tab": show_tab, "hide_table": hide_table}
            messages.add_message(request, messages.INFO, "This criterion NOT assigned to your role..!")
            return render(request, f"criteria/list_table.html", context)

    # Display Only Assigned Criterion to Teacher
    elif str(current_user.user_scope) == "TEACHER":
        if criteria_manager.TEACHER:
            object_list = CriterionMaster.objects.filter(criterion=slug, is_deleted=False, user=current_user).order_by(
                '-id')
            add_button = True
            context = {'object_list': object_list, 'cid': cid, 'add_button': add_button}
            return render(request, f"criteria/list_table.html", context)
        else:
            try:
                object_list = CriterionMaster.objects.filter(criterion=slug, is_deleted=False,
                                                             user=current_user).order_by('-id')
            except:
                object_list = []
            add_button = False
            show_tab = True
            hide_table = True
            context = {'object_list': object_list, 'cid': cid, 'add_button': add_button,
                       "show_tab": show_tab, "hide_table": hide_table}
            messages.add_message(request, messages.INFO, "This criterion NOT assigned to your role..!")
            return render(request, f"criteria/list_table.html", context)

    # Check for the user Club is assigned to the Criterion
    elif str(current_user.user_scope) == "CLUB":
        try:
            club_string = criteria_manager.assigned_clubs  # .keys()
            club_dict = json.loads(club_string)
        except:
            club_dict = {}

        # Check for club entry
        user_club = str(current_user.clubs)
        if user_club in club_dict.keys():
            club_entry = True
        else:
            club_entry = False

        if club_entry:
            object_list = CriterionMaster.objects.filter(criterion=slug, is_deleted=False, user=current_user).order_by(
                '-id')
            add_button = True
            context = {'object_list': object_list, 'cid': cid, 'add_button': add_button}
            return render(request, f"criteria/list_table.html", context)
        else:
            try:
                object_list = CriterionMaster.objects.filter(criterion=slug, is_deleted=False,
                                                             user=current_user).order_by('-id')
            except:
                object_list = []
            add_button = False
            show_tab = True
            hide_table = True
            context = {'object_list': object_list, 'cid': cid, 'add_button': add_button,
                       "show_tab": show_tab, "hide_table": hide_table}
            messages.add_message(request, messages.WARNING, "Check your Club role Selected")
            return render(request, f"criteria/list_table.html", context)

    messages.add_message(request, messages.INFO, "This criterion NOT assigned to current user role..!")
    return redirect(f'/criteria/list/{cr_index}')


# Bug on cr_index above.-----

# Approve a Criteria by Department
@login_required()
def approveCriteria(request, slug, pk):
    current_user = request.user
    try:
        object = CriterionMaster.objects.get(id=pk)
        success_url = '/criteria/show/' + str(object.criterion)

        if str(current_user.user_scope) in ("ADMIN", "NAAC_COD"):
            object.status = "APPROVED"
            object.save()
            messages.add_message(request, messages.SUCCESS, "Successfully Approved..!")
            return redirect(success_url)

        elif str(current_user.user_scope) == "DEPT_COD":
            object.status = "VERIFIED"
            object.is_verified = True
            object.save()
            messages.add_message(request, messages.SUCCESS, "Successfully Verified..!")
            return redirect(success_url)

        else:
            messages.add_message(request, messages.ERROR, "User Permission Error.!")
            return redirect(success_url)
    except:
        messages.add_message(request, messages.ERROR, "Something went wrong.!")
        return redirect(success_url)


# Revert a Criteria by Department
@login_required()
def revertCriteria(request, slug, pk):
    current_user = request.user
    try:
        object = CriterionMaster.objects.get(id=pk)
        success_url = '/criteria/show/' + str(object.criterion)

        if str(current_user.user_scope) in ("ADMIN", "NAAC_COD", "DEPT_COD"):
            object.status = "REVERTED"
            object.save()
            messages.add_message(request, messages.WARNING, "Criteria Reverted..!")
            return redirect(success_url)
        else:
            messages.add_message(request, messages.ERROR, "User Permission Error.!")
            return redirect(success_url)
    except:
        messages.add_message(request, messages.ERROR, "Something went wrong.!")
        return redirect(success_url)


# Delete a Criteria by Department
@login_required()
def deleteCriteria(request,pk):
    current_user = request.user

    try:
        object = CriterionMaster.objects.get(id=pk)
        success_url = '/criteria/show/' + str(object.criterion)

        if str(current_user.user_scope) in ("ADMIN", "NAAC_COD", "DEPT_COD"):
            object.status = "OTHER"
            object.is_deleted = True
            object.save()
            messages.add_message(request, messages.ERROR, "Criteria Deleted..!")
            return redirect(success_url)
        else:
            messages.add_message(request, messages.WARNING, "User Permission Error.!")
            return redirect(success_url)
    except:
        messages.add_message(request, messages.ERROR, "Something went wrong.!")
        return redirect(success_url)
