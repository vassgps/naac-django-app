# Adminapp/Summury.py
from django.views import generic, View
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from .models import FinalCriteria, CriteriaManager

# List All Criterion Names
all_criterion = ["c1_1_1", "c1_1_2", "c1_1_3", "c1_2_1", "c1_2_2", "c1_3_1", "c1_3_2", "c1_3_3", "c1_3_4", "c1_4_1",
                 "c1_4_2",
                 "c2_1_1", "c2_1_2", "c2_1_3", "c2_2_1", "c2_2_2", "c2_2_3", "c2_3_1", "c2_3_2", "c2_3_3", "c2_3_4",
                 "c2_4_1",
                 "c2_4_2", "c2_4_3", "c2_4_4", "c2_4_5", "c2_5_1", "c2_5_2", "c2_5_3", "c2_5_4", "c2_5_5", "c2_6_1",
                 "c2_6_2",
                 "c2_6_3", "c2_7_1", "c3_1_1", "c3_1_2", "c3_1_3", "c3_1_4", "c3_2_1", "c3_2_2", "c3_2_3", "c3_2_4",
                 "c3_3_1",
                 "c3_3_2", "c3_3_3", "c3_4_1", "c3_4_2", "c3_4_3", "c3_4_4", "c3_4_5", "c3_4_6", "c3_4_7", "c3_4_8",
                 "c3_5_1",
                 "c3_5_2", "c3_5_3", "c3_6_1", "c3_6_2", "c3_6_3", "c3_6_4", "c3_7_1", "c3_7_2", "c3_7_3", "c4_1_1",
                 "c4_1_2",
                 "c4_1_2A", "c4_1_2B", "c4_1_2C", "c4_1_2D", "c4_1_2E", "c4_1_3", "c4_1_4", "c4_2_1", "c4_2_2",
                 "c4_2_3",
                 "c4_2_4", "c4_2_5", "c4_2_6", "c4_3_1", "c4_3_2", "c4_3_3", "c4_3_4", "c4_4_1", "c4_4_2", "c5_1_1",
                 "c5_1_2",
                 "c5_1_3", "c5_1_3A", "c5_1_3B", "c5_1_3C", "c5_1_3D", "c5_1_3E", "c5_1_3F", "c5_1_3G", "c5_1_3H",
                 "c5_1_4",
                 "c5_1_5", "c5_1_6", "c5_2_1", "c5_2_2", "c5_2_3", "c5_3_1", "c5_3_2", "c5_3_2A", "c5_3_2B", "c5_3_3",
                 "c5_4_1A", "c5_4_1B",
                 "c5_4_2", "c6_1_1", "c6_1_2", "c6_2_1", "c6_2_2", "c6_2_3", "c6_2_4", "c6_3_1", "c6_3_2", "c6_3_3",
                 "c6_3_4",
                 "c6_3_5", "c6_4_1", "c6_4_2", "c6_4_3", "c6_5_1", "c6_5_2", "c6_5_3", "c6_5_4", "c6_5_5", "c7_1_1",
                 "c7_1_10",
                 "c7_1_11", "c7_1_12", "c7_1_13", "c7_1_14", "c7_1_15", "c7_1_16", "c7_1_17", "c7_1_18", "c7_1_19",
                 "c7_1_2",
                 "c7_1_2A", "c7_1_2B", "c7_1_2C", "c7_1_3", "c7_1_4", "c7_1_5", "c7_1_6", "c7_1_7", "c7_1_8", "c7_1_9",
                 "c7_2_1",
                 "c7_3_1"]


# Show total criterion entered by all for admin summary page
def summury(request):
    current_dict = {}
    for obj in all_criterion:
        criterion = str(obj).lower()
        try:
            cid = ContentType.objects.get(model=criterion)
            model_class = cid.model_class()
            count = model_class.objects.all().count()
        except:
            count = "x"
        obj_dict = {criterion: count}  # Create Temporary Dict
        current_dict.update(obj_dict)  # Update all count to Context Dictionary
    return render(request, "adminapp/summury.html", current_dict)


# Show total criterion entered by current user in home page
def userSummury(user):
    enterd_count = 0
    pending_count = 0
    for obj in all_criterion:
        criterion = str(obj)
        try:
            #Get the Model class using App name & Slug
            cr_index = criterion[1]
            app_name = 'criteria' + str(cr_index)
            Model = apps.get_model(app_name, criterion)
            count1 = Model.objects.filter(user=user).count()
            if count1 > 0:
                enterd_count = enterd_count + 1

            count2 = Model.objects.filter(user=user,status="PENDING").count()
            if count2 > 0:
                pending_count = pending_count + 1
        except Exception as e:
            return "NA"
    return {'enterd_count':enterd_count, 'pending_count':pending_count}


# Get Assigned criteria for current user
def getUserCriteria(user):
    try:
        if str(user.user_scope) == "TEACHER":
            cr_count = CriteriaManager.objects.filter(is_enabled=True, is_active=True, TEACHER=True).count()

        elif str(user.user_scope) == "CLUB":
            user_club_instance = str(user.clubs)
            cr_count = CriteriaManager.objects.filter(is_enabled=True, is_active=True, CLUB=True,
                                                      assigned_clubs__contains={user_club_instance: 'True'}).count()

        elif str(user.user_scope) == "DEPT_COD":
            cr_count = CriteriaManager.objects.filter(is_enabled=True, is_active=True, DEPT_COD=True).count()

        elif str(user.user_scope) == "NAAC_COD":
            cr_count = CriteriaManager.objects.filter(is_enabled=True, is_active=True, NAAC_COD=True).count()

        elif str(user.user_scope) == "STAFF":
            cr_count = CriteriaManager.objects.filter(is_enabled=True, is_active=True, STAFF=True).count()

        elif str(user.user_scope) == "OTHER":
            cr_count = CriteriaManager.objects.filter(is_enabled=True, is_active=True, OTHER=True).count()
        else:
            cr_count = 0
        return cr_count
    except Exception as e:
        print("E :", e)
        return "NA"


# Show media files download page
@method_decorator(staff_member_required, name='dispatch')
class MediaGeneration(View):
    def get(self, request):
        objects = FinalCriteria.objects.all()
        context = {'objects': objects}
        return render(request, "adminapp/media_generation.html", context)

    def post(self, request):
        form_data = request.POST.get('media')
        url = str('/criteria/' + form_data + '/media-downloads')
        return redirect(url)
