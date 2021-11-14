#Programs/Urls
from django.urls import path
from .views import *
from .utils.departments import *
from .utils.programs import *
from .utils.subjects import *
from .utils.clubs import *
from .utils.batch import *
app_name = "programs"

urlpatterns = [
    path("", home, name="home"),
    path('load-programs', load_programs, name='ajax_load_programs'),

    path("departments", AllDepartment.as_view() , name="departments"),
    path("departments/add", DeptCreateView.as_view(), name="departments-add"),
    path("departments/update/<int:pk>", DeptUpdateView.as_view(), name="departments-add"),
    path("departments/approve/<int:id>", approveDept, name="departments-approve"),
    path("departments/disable/<int:id>", disableDept, name="departments-disable"),

    path("programs",  AllPrograms.as_view(), name="programs"),
    path("programs/add", PrgmCreateView.as_view(), name="programs-add"),
    path("programs/update/<int:pk>", ProgramUpdateView.as_view(), name="programs-update"),
    path("programs/approve/<int:id>", approvePrgm, name="programs-approve"),
    path("programs/disable/<int:id>", disablePrgm, name="programs-dsiable"),

    path("subjects",  AllSubjects.as_view(), name="subjects"),
    path("subjects/add", SbjtCreateView.as_view(), name="subjects-add"),
    path("subjects/update/<int:pk>", SubjectUpdateView.as_view(), name="subjects-update"),
    path("subjects/approve/<int:id>", approveSbjt, name="subjects-approve"),
    path("subjects/disable/<int:id>", disableSbjt, name="subjects-dsiable"),

    path("club", AllClub.as_view(), name="club"),
    path("club/add", ClubCreateView.as_view(), name="club-add"),
    path("club/update/<int:pk>", ClubUpdateView.as_view(), name="club-update"),
    path("club/approve/<int:id>", approveClub, name="club-approve"),
    path("club/disable/<int:id>", disableClub, name="club-dsiable"),
    path("assign-club",assignClub, name="assign-club"),

    path("batch", AllBatch.as_view(), name="batch"),
    path("batch/add", BatchCreateView.as_view(), name="batch-add"),
    path("batch/update/<int:pk>", BatchUpdateView.as_view(), name="batch-update"),
    path("batch/approve/<int:id>", approveBatch, name="batch-approve"),
    path("batch/disable/<int:id>", disableBatch, name="batch-disable"),
]
