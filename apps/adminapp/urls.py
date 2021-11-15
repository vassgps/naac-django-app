# AdminApp/Urls
from django.urls import path
from .views import *
from .summury import summury
from .user_management import *
from .utils.criteria_management import *
from .utils.event_management import *
from .summury import MediaGeneration

app_name = "adminapp"

urlpatterns = [
    path("", index, name="index"),
    path("home", AdminHome.as_view(), name="home"),
    path("summury", summury, name="summury"),
    path("reports", reportGeneration, name="reports"),
    # User management
    path('allusers/', AllUsers.as_view(), name="allusers"),
    path('activeusers/', activeUsers, name="activeusers"),
    path('pendingusers/', pendingUsers, name="pendingusers"),
    path('approve-user/<int:id>', approveUser, name="approve-user"),
    path('disable-user/<int:id>', disableUser, name="disable-user"),
    path('edit-user/<int:pk>', UserUpdateView.as_view(), name="edit-user"),
    path('delete-user/<int:pk>', deleteUser, name="delete-user"),

    # For redirect to same page after approval or disable
    path('approve-user/page/<int:id>', approveUserPage, name="approve-user-page"),
    path('disable-user/page/<int:id>', disableUserPage, name="disable-user-page"),

    path('departments', AllDepartment.as_view(), name="departments"),
    path('programs', AllPrograms.as_view(), name="programs"),
    path('papers', AllPapers.as_view(), name="papers"),
    path('clubs', AllClubs.as_view(), name="clubs"),
    path('batch', AllBatch.as_view(), name="batch"),

    # Criteria Management
    path('assign-criterion', ManageCriteria.as_view(), name="assign-criterion"),
    path('assign-new-criteria', CreateCriteria.as_view(), name="assign-new-criteria"),
    path('enable-criteria/<int:id>', approveCriteria, name="enable-criteria"),
    path('disable-criteria/<int:id>', disableCriteria, name="disable-criteria"),
    path('update-question-data/<int:pk>', QuestionDataUpdateView.as_view(), name="update-question-data"),
    path('update-criteria/<int:pk>', CriteriaUpdateView.as_view(), name="update-criteria"),
    # Event Uploader
    path("event", AllEvent.as_view(), name="event"),
    path("event/add", EventCreateView.as_view(), name="event-add"),
    path("event/update/<int:pk>", EventUpdateView.as_view(), name="event-update"),
    path("event/approve/<int:id>", approveEvent, name="event-approve"),
    path("event/disable/<int:id>", disableEvent, name="event-disable"),
    # Additional Settings
    path('general-settings', GeneralSettings.as_view(), name="general-settings"),
    path("media-generation", MediaGeneration.as_view(), name="media-generation"),
    path("update/questions", display_questions, name="update-questions"),
    path("delete/criteria", deleteCriteria, name="delete-criterion"),

]
