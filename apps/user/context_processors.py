# Users/Context Processor.py
from django.contrib.auth.decorators import login_required
from ..adminapp.models import CriteriaManager
from ..programs.models import Clubs


# @login_required(login_url='/accounts/login/')
# Display  Assigned criterions on Top Menu based on User scopes
def add_menu_to_context(request):
    try:
        user_scope = request.user.user_scope
        user_club = str(request.user.clubs)
        showroles = False
        if str(user_scope) not in ["NAAC_COD", "STAFF", "ADMIN"]:
            show_dashboard = False  # Don't show the Admin Panel for Other  users
            try:
                if str(user_scope) == "TEACHER":
                    menu = CriteriaManager.objects.filter(is_enabled=True, is_active=True, TEACHER=True).order_by('ordering')
                    showroles = True
                elif str(user_scope) == "CLUB":
                    # Get club name by user.club
                    # Filter it by clubname with json filter
                    menu = CriteriaManager.objects.filter(is_enabled=True, is_active=True,assigned_clubs__contains={user_club: 'True'}).order_by('ordering')
                    #assigned_clubs=user_club
                    showroles = True

                # Disabled Club Changing option for Department and No Filtering for Top Menu list
                elif str(user_scope) == "DEPT_COD": 
                    menu = CriteriaManager.objects.filter(is_enabled=True, is_active=True).order_by('ordering')
                    showroles = False

            except Exception as e:
                pass
                print("Menu Exception:", e)
        else:
            show_dashboard = True       # Show Admin Panel Side Menu bar
            menu = CriteriaManager.objects.filter(is_enabled=True, is_active=True).order_by('ordering')
        return {'menu': menu, 'user': request.user, 'showroles': showroles,'show_dashboard': show_dashboard}
    except Exception as e:
        print("Error :", e)
        return {'menu': "menu", 'user': request.user, 'showroles': False, 'show_dashboard': False}


def add_club_to_context(request):
    try:
        user_scope = request.user.user_scope
        if str(user_scope) not in ["NAAC_COD", "STAFF", "ADMIN"]:
            user = request.user
            clubs = user.club_user.all()
        else:
            clubs = Clubs.objects.all()
        return {'clubs': clubs}

    except Exception as e:
        print("Clubs Error :", e)
        return {'clubs': "clubs"}
