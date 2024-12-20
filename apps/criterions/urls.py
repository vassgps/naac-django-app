from django.urls import path
from .views import *
from .criteria import *
from .fields.data_management import *
from .reports import *

app_name = 'criterions'

urlpatterns = [
    path('home', index, name="index"),
    path('show/<str:slug>', show_criteria, name="show-criteria"),
    path('detailed-view/<str:slug>/<int:id>', detailed_view, name="detailed-view"),

    path('search/', search, name='search'),
    path('cr/load-subject/', load_subject, name='cr-ajax_load_subject'),  # AJAX
    path('approve/<str:slug>/<int:pk>', approveCriteria, name="approve-criteria"),
    path('revert/<str:slug>/<int:pk>', revertCriteria, name="revert-criteria"),
    path('delete/<int:pk>', deleteCriteria, name="delete-criteria"),

    path("create/c1_1_1", CV1_1_1CreateView.as_view(), name="cc1_1_1"),
    path("edit/c1_1_1/<int:pk>", CV1_1_1UpdateView.as_view(), name="uc1_1_1"),
    path("adv-reports/c1_1_1/", C1_1_1Reports.as_view(),  name="rc1_1_1"),

    path("create/c1_1_2", CV1_1_2CreateView.as_view(), name="cc1_1_2"),
    path("edit/c1_1_2/<int:pk>", CV1_1_2UpdateView.as_view(), name="uc1_1_2"),
    path("adv-reports/c1_1_2/", C1_1_2Reports.as_view(),  name="rc1_1_2"),

    path("create/c1_1_3", CV1_1_3CreateView.as_view(), name="cc1_1_3"),
    path("edit/c1_1_3/<int:pk>", CV1_1_3UpdateView.as_view(), name="uc1_1_3"),
    path("adv-reports/c1_1_3/", C1_1_3Reports.as_view(),  name="rc1_1_3"),

    path("create/c1_2_1", CV1_2_1CreateView.as_view(), name="cc1_2_1"),
    path("edit/c1_2_1/<int:pk>", CV1_2_1UpdateView.as_view(), name="uc1_2_1"),
    path("adv-reports/c1_2_1/", C1_2_1Reports.as_view(), name="rc1_2_1"),

    path("create/c1_2_2", CV1_2_2CreateView.as_view(), name="cc1_2_2"),
    path("edit/c1_2_2/<int:pk>", CV1_2_2UpdateView.as_view(), name="uc1_2_2"),
    path("adv-reports/c1_2_2/", C1_2_2Reports.as_view(), name="rc1_2_2"),

    path("create/c1_3_1", CV1_3_1CreateView.as_view(), name="cc1_3_1"),
    path("edit/c1_3_1/<int:pk>", CV1_3_1UpdateView.as_view(), name="uc1_3_1"),
    path("adv-reports/c1_3_1/", C1_3_1Reports.as_view(), name="rc1_3_1"),

    path("create/c1_3_2", CV1_3_2CreateView.as_view(), name="cc1_3_2"),
    path("edit/c1_3_2/<int:pk>", CV1_3_2UpdateView.as_view(), name="uc1_3_2"),
    path("adv-reports/c1_3_2/", C1_3_2Reports.as_view(), name="rc1_3_2"),

    path("create/c1_3_3", CV1_3_3CreateView.as_view(), name="cc1_3_3"),
    path("edit/c1_3_3/<int:pk>", CV1_3_3UpdateView.as_view(), name="uc1_3_3"),
    path("adv-reports/c1_3_3/", C1_3_3Reports.as_view(), name="rc1_3_3"),

    path("create/c1_3_4", CV1_3_4CreateView.as_view(), name="cc1_3_4"),
    path("edit/c1_3_4/<int:pk>", CV1_3_4UpdateView.as_view(), name="uc1_3_4"),
    path("adv-reports/c1_3_4/", C1_3_4Reports.as_view(), name="rc1_3_4"),

    path("create/c1_4_1", CV1_4_1CreateView.as_view(), name="cc1_4_1"),
    path("edit/c1_4_1/<int:pk>", CV1_4_1UpdateView.as_view(), name="uc1_4_1"),
    path("adv-reports/c1_4_1/", C1_4_1Reports.as_view(), name="rc1_4_1"),

    path("create/c1_4_2", CV1_4_2CreateView.as_view(), name="cc1_4_2"),
    path("edit/c1_4_2/<int:pk>", CV1_4_2UpdateView.as_view(), name="uc1_4_2"),
    path("adv-reports/c1_4_2/", C1_4_2Reports.as_view(), name="rc1_4_2"),

    path("create/c2_1_1", CV2_1_1CreateView.as_view(), name="cc2_1_1"),
    path("edit/c2_1_1/<int:pk>", CV2_1_1UpdateView.as_view(), name="uc2_1_1"),
    path("adv-reports/c2_1_1/", C2_1_1Reports.as_view(), name="rc2_1_1"),

    path("create/c2_1_2", CV2_1_2CreateView.as_view(), name="cc2_1_2"),
    path("edit/c2_1_2/<int:pk>", CV2_1_2UpdateView.as_view(), name="uc2_1_2"),
    path("adv-reports/c2_1_2/", C2_1_2Reports.as_view(), name="rc2_1_2"),

    path("create/c2_1_3", CV2_1_3CreateView.as_view(), name="cc2_1_3"),
    path("edit/c2_1_3/<int:pk>", CV2_1_3UpdateView.as_view(), name="uc2_1_3"),
    path("adv-reports/c2_1_3/", C2_1_3Reports.as_view(), name="rc2_1_3"),

    path("create/c2_2_1", CV2_2_1CreateView.as_view(), name="cc2_2_1"),
    path("edit/c2_2_1/<int:pk>", CV2_2_1UpdateView.as_view(), name="uc2_2_1"),
    path("adv-reports/c2_2_1/", C2_2_1Reports.as_view(), name="rc2_2_1"),

    path("create/c2_2_2", CV2_2_2CreateView.as_view(), name="cc2_2_2"),
    path("edit/c2_2_2/<int:pk>", CV2_2_2UpdateView.as_view(), name="uc2_2_2"),
    path("adv-reports/c2_2_2/", C2_2_2Reports.as_view(), name="rc2_2_2"),

    path("create/c2_2_3", CV2_2_3CreateView.as_view(), name="cc2_2_3"),
    path("edit/c2_2_3/<int:pk>", CV2_2_3UpdateView.as_view(), name="uc2_2_3"),
    path("adv-reports/c2_2_3/", C2_2_3Reports.as_view(), name="rc2_2_3"),

    path("create/c2_3_1", CV2_3_1CreateView.as_view(), name="cc2_3_1"),
    path("edit/c2_3_1/<int:pk>", CV2_3_1UpdateView.as_view(), name="uc2_3_1"),
    path("adv-reports/c2_3_1/", C2_3_1Reports.as_view(), name="rc2_3_1"),

    path("create/c2_3_2", CV2_3_2CreateView.as_view(), name="cc2_3_2"),
    path("edit/c2_3_2/<int:pk>", CV2_3_2UpdateView.as_view(), name="uc2_3_2"),
    path("adv-reports/c2_3_2/", C2_3_2Reports.as_view(), name="rc2_3_2"),

    path("create/c2_3_3", CV2_3_3CreateView.as_view(), name="cc2_3_3"),
    path("edit/c2_3_3/<int:pk>", CV2_3_3UpdateView.as_view(), name="uc2_3_3"),
    path("adv-reports/c2_3_3/", C2_3_3Reports.as_view(), name="rc2_3_3"),

    path("create/c2_3_4", CV2_3_4CreateView.as_view(), name="cc2_3_4"),
    path("edit/c2_3_4/<int:pk>", CV2_3_4UpdateView.as_view(), name="uc2_3_4"),
    path("adv-reports/c2_3_4/", C2_3_4Reports.as_view(), name="rc2_3_4"),

    path("create/c2_4_1", CV2_4_1CreateView.as_view(), name="cc2_4_1"),
    path("edit/c2_4_1/<int:pk>", CV2_4_1UpdateView.as_view(), name="uc2_4_1"),
    path("adv-reports/c2_4_1/", C2_4_1Reports.as_view(), name="rc2_4_1"),

    path("create/c2_4_2", CV2_4_2CreateView.as_view(), name="cc2_4_2"),
    path("edit/c2_4_2/<int:pk>", CV2_4_2UpdateView.as_view(), name="uc2_4_2"),
    path("adv-reports/c2_4_2/", C2_4_2Reports.as_view(), name="rc2_4_2"),

    path("create/c2_4_3", CV2_4_3CreateView.as_view(), name="cc2_4_3"),
    path("edit/c2_4_3/<int:pk>", CV2_4_3UpdateView.as_view(), name="uc2_4_3"),
    path("adv-reports/c2_4_3/", C2_4_3Reports.as_view(), name="rc2_4_3"),

    path("create/c2_4_4", CV2_4_4CreateView.as_view(), name="cc2_4_4"),
    path("edit/c2_4_4/<int:pk>", CV2_4_4UpdateView.as_view(), name="uc2_4_4"),
    path("adv-reports/c2_4_4/", C2_4_4Reports.as_view(), name="rc2_4_4"),

    path("create/c2_4_5", CV2_4_5CreateView.as_view(), name="cc2_4_5"),
    path("edit/c2_4_5/<int:pk>", CV2_4_5UpdateView.as_view(), name="uc2_4_5"),
    path("adv-reports/c2_4_5/", C2_4_5Reports.as_view(), name="rc2_4_5"),

    path("create/c2_5_1", CV2_5_1CreateView.as_view(), name="cc2_5_1"),
    path("edit/c2_5_1/<int:pk>", CV2_5_1UpdateView.as_view(), name="uc2_5_1"),
    path("adv-reports/c2_5_1/", C2_5_1Reports.as_view(), name="rc2_5_1"),

    path("create/c2_5_2", CV2_5_2CreateView.as_view(), name="cc2_5_2"),
    path("edit/c2_5_2/<int:pk>", CV2_5_2UpdateView.as_view(), name="uc2_5_2"),
    path("adv-reports/c2_5_2/", C2_5_2Reports.as_view(), name="rc2_5_2"),

    path("create/c2_5_3", CV2_5_3CreateView.as_view(), name="cc2_5_3"),
    path("edit/c2_5_3/<int:pk>", CV2_5_3UpdateView.as_view(), name="uc2_5_3"),
    path("adv-reports/c2_5_3/", C2_5_3Reports.as_view(), name="rc2_5_3"),

    path("create/c2_5_4", CV2_5_4CreateView.as_view(), name="cc2_5_4"),
    path("edit/c2_5_4/<int:pk>", CV2_5_4UpdateView.as_view(), name="uc2_5_4"),
    path("adv-reports/c2_5_4/", C2_5_4Reports.as_view(), name="rc2_5_4"),

    path("create/c2_5_5", CV2_5_5CreateView.as_view(), name="cc2_5_5"),
    path("edit/c2_5_5/<int:pk>", CV2_5_5UpdateView.as_view(), name="uc2_5_5"),
    path("adv-reports/c2_5_5/", C2_5_5Reports.as_view(), name="rc2_5_5"),

    path("create/c2_6_1", CV2_6_1CreateView.as_view(), name="cc2_6_1"),
    path("edit/c2_6_1/<int:pk>", CV2_6_1UpdateView.as_view(), name="uc2_6_1"),
    path("adv-reports/c2_6_1/", C2_6_1Reports.as_view(), name="rc2_6_1"),

    path("create/c2_6_2", CV2_6_2CreateView.as_view(), name="cc2_6_2"),
    path("edit/c2_6_2/<int:pk>", CV2_6_2UpdateView.as_view(), name="uc2_6_2"),
    path("adv-reports/c2_6_2/", C2_6_2Reports.as_view(), name="rc2_6_2"),

    path("create/c2_6_3", CV2_6_3CreateView.as_view(), name="cc2_6_3"),
    path("edit/c2_6_3/<int:pk>", CV2_6_3UpdateView.as_view(), name="uc2_6_3"),
    path("adv-reports/c2_6_3/", C2_6_3Reports.as_view(), name="rc2_6_3"),

    path("create/c2_7_1", CV2_7_1CreateView.as_view(), name="cc2_7_1"),
    path("edit/c2_7_1/<int:pk>", CV2_7_1UpdateView.as_view(), name="uc2_7_1"),
    path("adv-reports/c2_7_1/", C2_7_1Reports.as_view(), name="rc2_7_1"),

    path("create/c3_1_1", CV3_1_1CreateView.as_view(), name="cc3_1_1"),
    path("edit/c3_1_1/<int:pk>", CV3_1_1UpdateView.as_view(), name="uc3_1_1"),
    path("adv-reports/c3_1_1/", C3_1_1Reports.as_view(), name="rc3_1_1"),

    path("create/c3_1_2", CV3_1_2CreateView.as_view(), name="cc3_1_2"),
    path("edit/c3_1_2/<int:pk>", CV3_1_2UpdateView.as_view(), name="uc3_1_2"),
    path("adv-reports/c3_1_2/", C3_1_2Reports.as_view(), name="rc3_1_2"),

    path("create/c3_1_3", CV3_1_3CreateView.as_view(), name="cc3_1_3"),
    path("edit/c3_1_3/<int:pk>", CV3_1_3UpdateView.as_view(), name="uc3_1_3"),
    path("adv-reports/c3_1_3/", C3_1_3Reports.as_view(), name="rc3_1_3"),

    path("create/c3_1_4", CV3_1_4CreateView.as_view(), name="cc3_1_4"),
    path("edit/c3_1_4/<int:pk>", CV3_1_4UpdateView.as_view(), name="uc3_1_4"),
    path("adv-reports/c3_1_4/", C3_1_4Reports.as_view(), name="rc3_1_4"),

    path("create/c3_2_1", CV3_2_1CreateView.as_view(), name="cc3_2_1"),
    path("edit/c3_2_1/<int:pk>", CV3_2_1UpdateView.as_view(), name="uc3_2_1"),
    path("adv-reports/c3_2_1/", C3_2_1Reports.as_view(), name="rc3_2_1"),

    path("create/c3_2_2", CV3_2_2CreateView.as_view(), name="cc3_2_2"),
    path("edit/c3_2_2/<int:pk>", CV3_2_2UpdateView.as_view(), name="uc3_2_2"),
    path("adv-reports/c3_2_2/", C3_2_2Reports.as_view(), name="rc3_2_2"),

    path("create/c3_2_3", CV3_2_3CreateView.as_view(), name="cc3_2_3"),
    path("edit/c3_2_3/<int:pk>", CV3_2_3UpdateView.as_view(), name="uc3_2_3"),
    path("adv-reports/c3_2_3/", C3_2_3Reports.as_view(), name="rc3_2_3"),

    path("create/c3_2_4", CV3_2_4CreateView.as_view(), name="cc3_2_4"),
    path("edit/c3_2_4/<int:pk>", CV3_2_4UpdateView.as_view(), name="uc3_2_4"),
    path("adv-reports/c3_2_4/", C3_2_4Reports.as_view(), name="rc3_2_4"),

    path("create/c3_3_1", CV3_3_1CreateView.as_view(), name="cc3_3_1"),
    path("edit/c3_3_1/<int:pk>", CV3_3_1UpdateView.as_view(), name="uc3_3_1"),
    path("adv-reports/c3_3_1/", C3_3_1Reports.as_view(), name="rc3_3_1"),

    path("create/c3_3_2", CV3_3_2CreateView.as_view(), name="cc3_3_2"),
    path("edit/c3_3_2/<int:pk>", CV3_3_2UpdateView.as_view(), name="uc3_3_2"),
    path("adv-reports/c3_3_2/", C3_3_2Reports.as_view(), name="rc3_3_2"),

    path("create/c3_3_3", CV3_3_3CreateView.as_view(), name="cc3_3_3"),
    path("edit/c3_3_3/<int:pk>", CV3_3_3UpdateView.as_view(), name="uc3_3_3"),
    path("adv-reports/c3_3_3/", C3_3_3Reports.as_view(), name="rc3_3_3"),

    path("create/c3_4_1", CV3_4_1CreateView.as_view(), name="cc3_4_1"),
    path("edit/c3_4_1/<int:pk>", CV3_4_1UpdateView.as_view(), name="uc3_4_1"),
    path("adv-reports/c3_4_1/", C3_4_1Reports.as_view(), name="rc3_4_1"),

    path("create/c3_4_2", CV3_4_2CreateView.as_view(), name="cc3_4_2"),
    path("edit/c3_4_2/<int:pk>", CV3_4_2UpdateView.as_view(), name="uc3_4_2"),
    path("adv-reports/c3_4_2/", C3_4_2Reports.as_view(), name="rc3_4_2"),

    path("create/c3_4_3", CV3_4_3CreateView.as_view(), name="cc3_4_3"),
    path("edit/c3_4_3/<int:pk>", CV3_4_3UpdateView.as_view(), name="uc3_4_3"),
    path("adv-reports/c3_4_3/", C3_4_3Reports.as_view(), name="rc3_4_3"),

    path("create/c3_4_4", CV3_4_4CreateView.as_view(), name="cc3_4_4"),
    path("edit/c3_4_4/<int:pk>", CV3_4_4UpdateView.as_view(), name="uc3_4_4"),
    path("adv-reports/c3_4_4/", C3_4_4Reports.as_view(), name="rc3_4_4"),

    path("create/c3_4_5", CV3_4_5CreateView.as_view(), name="cc3_4_5"),
    path("edit/c3_4_5/<int:pk>", CV3_4_5UpdateView.as_view(), name="uc3_4_5"),
    path("adv-reports/c3_4_5/", C3_4_5Reports.as_view(), name="rc3_4_5"),

    path("create/c3_4_6", CV3_4_6CreateView.as_view(), name="cc3_4_6"),
    path("edit/c3_4_6/<int:pk>", CV3_4_6UpdateView.as_view(), name="uc3_4_6"),
    path("adv-reports/c3_4_6/", C3_4_6Reports.as_view(), name="rc3_4_6"),

    path("create/c3_4_7", CV3_4_7CreateView.as_view(), name="cc3_4_7"),
    path("edit/c3_4_7/<int:pk>", CV3_4_7UpdateView.as_view(), name="uc3_4_7"),
    path("adv-reports/c3_4_7/", C3_4_7Reports.as_view(), name="rc3_4_7"),

    path("create/c3_4_8", CV3_4_8CreateView.as_view(), name="cc3_4_8"),
    path("edit/c3_4_8/<int:pk>", CV3_4_8UpdateView.as_view(), name="uc3_4_8"),
    path("adv-reports/c3_4_8/", C3_4_8Reports.as_view(), name="rc3_4_8"),

    path("create/c3_5_1", CV3_5_1CreateView.as_view(), name="cc3_5_1"),
    path("edit/c3_5_1/<int:pk>", CV3_5_1UpdateView.as_view(), name="uc3_5_1"),
    path("adv-reports/c3_5_1/", C3_5_1Reports.as_view(), name="rc3_5_1"),

    path("create/c3_5_2", CV3_5_2CreateView.as_view(), name="cc3_5_2"),
    path("edit/c3_5_2/<int:pk>", CV3_5_2UpdateView.as_view(), name="uc3_5_2"),
    path("adv-reports/c3_5_2/", C3_5_2Reports.as_view(), name="rc3_5_2"),

    path("create/c3_5_3", CV3_5_3CreateView.as_view(), name="cc3_5_3"),
    path("edit/c3_5_3/<int:pk>", CV3_5_3UpdateView.as_view(), name="uc3_5_3"),
    path("adv-reports/c3_5_3/", C3_5_3Reports.as_view(), name="rc3_5_3"),

    path("create/c3_6_1", CV3_6_1CreateView.as_view(), name="cc3_6_1"),
    path("edit/c3_6_1/<int:pk>", CV3_6_1UpdateView.as_view(), name="uc3_6_1"),
    path("adv-reports/c3_6_1/", C3_6_1Reports.as_view(), name="rc3_6_1"),

    path("create/c3_6_2", CV3_6_2CreateView.as_view(), name="cc3_6_2"),
    path("edit/c3_6_2/<int:pk>", CV3_6_2UpdateView.as_view(), name="uc3_6_2"),
    path("adv-reports/c3_6_2/", C3_6_2Reports.as_view(), name="rc3_6_2"),

    path("create/c3_6_3", CV3_6_3CreateView.as_view(), name="cc3_6_3"),
    path("edit/c3_6_3/<int:pk>", CV3_6_3UpdateView.as_view(), name="uc3_6_3"),
    path("adv-reports/c3_6_3/", C3_6_3Reports.as_view(), name="rc3_6_3"),

    path("create/c3_6_4", CV3_6_4CreateView.as_view(), name="cc3_6_4"),
    path("edit/c3_6_4/<int:pk>", CV3_6_4UpdateView.as_view(), name="uc3_6_4"),
    path("adv-reports/c3_6_4/", C3_6_4Reports.as_view(), name="rc3_6_4"),

    path("create/c3_7_1", CV3_7_1CreateView.as_view(), name="cc3_7_1"),
    path("edit/c3_7_1/<int:pk>", CV3_7_1UpdateView.as_view(), name="uc3_7_1"),
    path("adv-reports/c3_7_1/", C3_7_1Reports.as_view(), name="rc3_7_1"),

    path("create/c3_7_2", CV3_7_2CreateView.as_view(), name="cc3_7_2"),
    path("edit/c3_7_2/<int:pk>", CV3_7_2UpdateView.as_view(), name="uc3_7_2"),
    path("adv-reports/c3_7_2/", C3_7_2Reports.as_view(), name="rc3_7_2"),

    path("create/c3_7_3", CV3_7_3CreateView.as_view(), name="cc3_7_3"),
    path("edit/c3_7_3/<int:pk>", CV3_7_3UpdateView.as_view(), name="uc3_7_3"),
    path("adv-reports/c3_7_3/", C3_7_3Reports.as_view(), name="rc3_7_3"),

    path("create/c4_1_1", CV4_1_1CreateView.as_view(), name="cc4_1_1"),
    path("edit/c4_1_1/<int:pk>", CV4_1_1UpdateView.as_view(), name="uc4_1_1"),
    path("adv-reports/c4_1_1/", C4_1_1Reports.as_view(), name="rc4_1_1"),

    path("create/c4_1_2A", CV4_1_2ACreateView.as_view(), name="cc4_1_2A"),
    path("edit/c4_1_2A/<int:pk>", CV4_1_2AUpdateView.as_view(), name="uc4_1_2A"),
    path("adv-reports/c4_1_2A/", C4_1_2AReports.as_view(), name="rc4_1_2A"),

    path("create/c4_1_2B", CV4_1_2BCreateView.as_view(), name="cc4_1_2B"),
    path("edit/c4_1_2B/<int:pk>", CV4_1_2BUpdateView.as_view(), name="uc4_1_2B"),
    path("adv-reports/c4_1_2B/", C4_1_2BReports.as_view(), name="rc4_1_2B"),

    path("create/c4_1_2C", CV4_1_2CCreateView.as_view(), name="cc4_1_2C"),
    path("edit/c4_1_2C/<int:pk>", CV4_1_2CUpdateView.as_view(), name="uc4_1_2C"),
    path("adv-reports/c4_1_2C/", C4_1_2CReports.as_view(), name="rc4_1_2C"),

    path("create/c4_1_2D", CV4_1_2DCreateView.as_view(), name="cc4_1_2D"),
    path("edit/c4_1_2D/<int:pk>", CV4_1_2DUpdateView.as_view(), name="uc4_1_2D"),
    path("adv-reports/c4_1_2D/", C4_1_2DReports.as_view(), name="rc4_1_2D"),

    path("create/c4_1_2E", CV4_1_2ECreateView.as_view(), name="cc4_1_2E"),
    path("edit/c4_1_2E/<int:pk>", CV4_1_2EUpdateView.as_view(), name="uc4_1_2E"),
    path("adv-reports/c4_1_2E/", C4_1_2EReports.as_view(), name="rc4_1_2E"),

    path("create/c4_1_3", CV4_1_3CreateView.as_view(), name="cc4_1_3"),
    path("edit/c4_1_3/<int:pk>", CV4_1_3UpdateView.as_view(), name="uc4_1_3"),
    path("adv-reports/c4_1_3/", C4_1_3Reports.as_view(), name="rc4_1_3"),

    path("create/c4_1_4", CV4_1_4CreateView.as_view(), name="cc4_1_4"),
    path("edit/c4_1_4/<int:pk>", CV4_1_4UpdateView.as_view(), name="uc4_1_4"),
    path("adv-reports/c4_1_4/", C4_1_4Reports.as_view(), name="rc4_1_4"),

    path("create/c4_2_1", CV4_2_1CreateView.as_view(), name="cc4_2_1"),
    path("edit/c4_2_1/<int:pk>", CV4_2_1UpdateView.as_view(), name="uc4_2_1"),
    path("adv-reports/c4_2_1/", C4_2_1Reports.as_view(), name="rc4_2_1"),

    path("create/c4_2_2", CV4_2_2CreateView.as_view(), name="cc4_2_2"),
    path("edit/c4_2_2/<int:pk>", CV4_2_2UpdateView.as_view(), name="uc4_2_2"),
    path("adv-reports/c4_2_2/", C4_2_2Reports.as_view(), name="rc4_2_2"),

    path("create/c4_2_3", CV4_2_3CreateView.as_view(), name="cc4_2_3"),
    path("edit/c4_2_3/<int:pk>", CV4_2_3UpdateView.as_view(), name="uc4_2_3"),
    path("adv-reports/c4_2_3/", C4_2_3Reports.as_view(), name="rc4_2_3"),

    path("create/c4_2_4", CV4_2_4CreateView.as_view(), name="cc4_2_4"),
    path("edit/c4_2_4/<int:pk>", CV4_2_4UpdateView.as_view(), name="uc4_2_4"),
    path("adv-reports/c4_2_4/", C4_2_4Reports.as_view(), name="rc4_2_4"),

    path("create/c4_2_5", CV4_2_5CreateView.as_view(), name="cc4_2_5"),
    path("edit/c4_2_5/<int:pk>", CV4_2_5UpdateView.as_view(), name="uc4_2_5"),
    path("adv-reports/c4_2_5/", C4_2_5Reports.as_view(), name="rc4_2_5"),

    path("create/c4_2_6", CV4_2_6CreateView.as_view(), name="cc4_2_6"),
    path("edit/c4_2_6/<int:pk>", CV4_2_6UpdateView.as_view(), name="uc4_2_6"),
    path("adv-reports/c4_2_6/", C4_2_6Reports.as_view(), name="rc4_2_6"),

    path("create/c4_3_1", CV4_3_1CreateView.as_view(), name="cc4_3_1"),
    path("edit/c4_3_1/<int:pk>", CV4_3_1UpdateView.as_view(), name="uc4_3_1"),
    path("adv-reports/c4_3_1/", C4_3_1Reports.as_view(), name="rc4_3_1"),

    path("create/c4_3_2", CV4_3_2CreateView.as_view(), name="cc4_3_2"),
    path("edit/c4_3_2/<int:pk>", CV4_3_2UpdateView.as_view(), name="uc4_3_2"),
    path("adv-reports/c4_3_2/", C4_3_2Reports.as_view(), name="rc4_3_2"),

    path("create/c4_3_3", CV4_3_3CreateView.as_view(), name="cc4_3_3"),
    path("edit/c4_3_3/<int:pk>", CV4_3_3UpdateView.as_view(), name="uc4_3_3"),
    path("adv-reports/c4_3_3/", C4_3_3Reports.as_view(), name="rc4_3_3"),

    path("create/c4_3_4", CV4_3_4CreateView.as_view(), name="cc4_3_4"),
    path("edit/c4_3_4/<int:pk>", CV4_3_4UpdateView.as_view(), name="uc4_3_4"),
    path("adv-reports/c4_3_4/", C4_3_4Reports.as_view(), name="rc4_3_4"),

    path("create/c4_4_1", CV4_4_1CreateView.as_view(), name="cc4_4_1"),
    path("edit/c4_4_1/<int:pk>", CV4_4_1UpdateView.as_view(), name="uc4_4_1"),
    path("adv-reports/c4_4_1/", C4_4_1Reports.as_view(), name="rc4_4_1"),

    path("create/c4_4_2", CV4_4_2CreateView.as_view(), name="cc4_4_2"),
    path("edit/c4_4_2/<int:pk>", CV4_4_2UpdateView.as_view(), name="uc4_4_2"),
    path("adv-reports/c4_4_2/", C4_4_2Reports.as_view(), name="rc4_4_2"),

    path("create/c5_1_1", CV5_1_1CreateView.as_view(), name="cc5_1_1"),
    path("edit/c5_1_1/<int:pk>", CV5_1_1UpdateView.as_view(), name="uc5_1_1"),
    path("adv-reports/c5_1_1/", C5_1_1Reports.as_view(), name="rc5_1_1"),

    path("create/c5_1_2", CV5_1_2CreateView.as_view(), name="cc5_1_2"),
    path("edit/c5_1_2/<int:pk>", CV5_1_2UpdateView.as_view(), name="uc5_1_2"),
    path("adv-reports/c5_1_2/", C5_1_2Reports.as_view(), name="rc5_1_2"),

    path("create/c5_1_3A", CV5_1_3ACreateView.as_view(), name="cc5_1_3A"),
    path("edit/c5_1_3A/<int:pk>", CV5_1_3AUpdateView.as_view(), name="uc5_1_3A"),
    path("adv-reports/c5_1_3A/", C5_1_3AReports.as_view(), name="rc5_1_3A"),

    path("create/c5_1_3B", CV5_1_3BCreateView.as_view(), name="cc5_1_3B"),
    path("edit/c5_1_3B/<int:pk>", CV5_1_3BUpdateView.as_view(), name="uc5_1_3B"),
    path("adv-reports/c5_1_3B/", C5_1_3BReports.as_view(), name="rc5_1_3B"),

    path("create/c5_1_3C", CV5_1_3CCreateView.as_view(), name="cc5_1_3C"),
    path("edit/c5_1_3C/<int:pk>", CV5_1_3CUpdateView.as_view(), name="uc5_1_3C"),
    path("adv-reports/c5_1_3C/", C5_1_3CReports.as_view(), name="rc5_1_3C"),

    path("create/c5_1_3D", CV5_1_3DCreateView.as_view(), name="cc5_1_3D"),
    path("edit/c5_1_3D/<int:pk>", CV5_1_3DUpdateView.as_view(), name="uc5_1_3D"),
    path("adv-reports/c5_1_3D/", C5_1_3DReports.as_view(), name="rc5_1_3D"),

    path("create/c5_1_3E", CV5_1_3ECreateView.as_view(), name="cc5_1_3E"),
    path("edit/c5_1_3E/<int:pk>", CV5_1_3EUpdateView.as_view(), name="uc5_1_3E"),
    path("adv-reports/c5_1_3E/", C5_1_3EReports.as_view(), name="rc5_1_3E"),

    path("create/c5_1_3F", CV5_1_3FCreateView.as_view(), name="cc5_1_3F"),
    path("edit/c5_1_3F/<int:pk>", CV5_1_3FUpdateView.as_view(), name="uc5_1_3F"),
    path("adv-reports/c5_1_3F/", C5_1_3FReports.as_view(), name="rc5_1_3F"),

    path("create/c5_1_3G", CV5_1_3GCreateView.as_view(), name="cc5_1_3G"),
    path("edit/c5_1_3G/<int:pk>", CV5_1_3GUpdateView.as_view(), name="uc5_1_3G"),
    path("adv-reports/c5_1_3G/", C5_1_3GReports.as_view(), name="rc5_1_3G"),

    path("create/c5_1_3H", CV5_1_3HCreateView.as_view(), name="cc5_1_3H"),
    path("edit/c5_1_3H/<int:pk>", CV5_1_3HUpdateView.as_view(), name="uc5_1_3H"),
    path("adv-reports/c5_1_3H/", C5_1_3HReports.as_view(), name="rc5_1_3H"),

    path("create/c5_1_4", CV5_1_4CreateView.as_view(), name="cc5_1_4"),
    path("edit/c5_1_4/<int:pk>", CV5_1_4UpdateView.as_view(), name="uc5_1_4"),
    path("adv-reports/c5_1_4/", C5_1_4Reports.as_view(), name="rc5_1_4"),

    path("create/c5_1_5", CV5_1_5CreateView.as_view(), name="cc5_1_5"),
    path("edit/c5_1_5/<int:pk>", CV5_1_5UpdateView.as_view(), name="uc5_1_5"),
    path("adv-reports/c5_1_5/", C5_1_5Reports.as_view(), name="rc5_1_5"),

    path("create/c5_1_6", CV5_1_6CreateView.as_view(), name="cc5_1_6"),
    path("edit/c5_1_6/<int:pk>", CV5_1_6UpdateView.as_view(), name="uc5_1_6"),
    path("adv-reports/c5_1_6/", C5_1_6Reports.as_view(), name="rc5_1_6"),

    path("create/c5_2_1", CV5_2_1CreateView.as_view(), name="cc5_2_1"),
    path("edit/c5_2_1/<int:pk>", CV5_2_1UpdateView.as_view(), name="uc5_2_1"),
    path("adv-reports/c5_2_1/", C5_2_1Reports.as_view(), name="rc5_2_1"),

    path("create/c5_2_2", CV5_2_2CreateView.as_view(), name="cc5_2_2"),
    path("edit/c5_2_2/<int:pk>", CV5_2_2UpdateView.as_view(), name="uc5_2_2"),
    path("adv-reports/c5_2_2/", C5_2_2Reports.as_view(), name="rc5_2_2"),

    path("create/c5_2_3", CV5_2_3CreateView.as_view(), name="cc5_2_3"),
    path("edit/c5_2_3/<int:pk>", CV5_2_3UpdateView.as_view(), name="uc5_2_3"),
    path("adv-reports/c5_2_3/", C5_2_3Reports.as_view(), name="rc5_2_3"),

    path("create/c5_3_1", CV5_3_1CreateView.as_view(), name="cc5_3_1"),
    path("edit/c5_3_1/<int:pk>", CV5_3_1UpdateView.as_view(), name="uc5_3_1"),
    path("adv-reports/c5_3_1/", C5_3_1Reports.as_view(), name="rc5_3_1"),

    path("create/c5_3_2A", CV5_3_2ACreateView.as_view(), name="cc5_3_2A"),
    path("edit/c5_3_2A/<int:pk>", CV5_3_2AUpdateView.as_view(), name="uc5_3_2A"),
    path("adv-reports/c5_3_2A/", C5_3_2AReports.as_view(), name="rc5_3_2A"),

    path("create/c5_3_2B", CV5_3_2BCreateView.as_view(), name="cc5_3_2B"),
    path("edit/c5_3_2B/<int:pk>", CV5_3_2BUpdateView.as_view(), name="uc5_3_2B"),
    path("adv-reports/c5_3_2B/", C5_3_2BReports.as_view(), name="rc5_3_2B"),

    path("create/c5_3_3", CV5_3_3CreateView.as_view(), name="cc5_3_3"),
    path("edit/c5_3_3/<int:pk>", CV5_3_3UpdateView.as_view(), name="uc5_3_3"),
    path("adv-reports/c5_3_3/", C5_3_3Reports.as_view(), name="rc5_3_3"),

    path("create/c5_4_1A", CV5_4_1ACreateView.as_view(), name="cc5_4_1A"),
    path("edit/c5_4_1A/<int:pk>", CV5_4_1AUpdateView.as_view(), name="uc5_4_1A"),
    path("adv-reports/c5_4_1A/", C5_4_1AReports.as_view(), name="rc5_4_1A"),

    path("create/c5_4_1B", CV5_4_1BCreateView.as_view(), name="cc5_4_1B"),
    path("edit/c5_4_1B/<int:pk>", CV5_4_1BUpdateView.as_view(), name="uc5_4_1B"),
    path("adv-reports/c5_4_1B/", C5_4_1BReports.as_view(), name="rc5_4_1B"),

    path("create/c5_4_2", CV5_4_2CreateView.as_view(), name="cc5_4_2"),
    path("edit/c5_4_2/<int:pk>", CV5_4_2UpdateView.as_view(), name="uc5_4_2"),
    path("adv-reports/c5_4_2/", C5_4_2Reports.as_view(), name="rc5_4_2"),

    path("create/c6_1_1", CV6_1_1CreateView.as_view(), name="cc6_1_1"),
    path("edit/c6_1_1/<int:pk>", CV6_1_1UpdateView.as_view(), name="uc6_1_1"),
    path("adv-reports/c6_1_1/", C6_1_1Reports.as_view(), name="rc6_1_1"),

    path("create/c6_1_2", CV6_1_2CreateView.as_view(), name="cc6_1_2"),
    path("edit/c6_1_2/<int:pk>", CV6_1_2UpdateView.as_view(), name="uc6_1_2"),
    path("adv-reports/c6_1_2/", C6_1_2Reports.as_view(), name="rc6_1_2"),

    path("create/c6_2_1", CV6_2_1CreateView.as_view(), name="cc6_2_1"),
    path("edit/c6_2_1/<int:pk>", CV6_2_1UpdateView.as_view(), name="uc6_2_1"),
    path("adv-reports/c6_2_1/", C6_2_1Reports.as_view(), name="rc6_2_1"),

    path("create/c6_2_2", CV6_2_2CreateView.as_view(), name="cc6_2_2"),
    path("edit/c6_2_2/<int:pk>", CV6_2_2UpdateView.as_view(), name="uc6_2_2"),
    path("adv-reports/c6_2_2/", C6_2_2Reports.as_view(), name="rc6_2_2"),

    path("create/c6_2_3", CV6_2_3CreateView.as_view(), name="cc6_2_3"),
    path("edit/c6_2_3/<int:pk>", CV6_2_3UpdateView.as_view(), name="uc6_2_3"),
    path("adv-reports/c6_2_3/", C6_2_3Reports.as_view(), name="rc6_2_3"),

    path("create/c6_2_4", CV6_2_4CreateView.as_view(), name="cc6_2_4"),
    path("edit/c6_2_4/<int:pk>", CV6_2_4UpdateView.as_view(), name="uc6_2_4"),
    path("adv-reports/c6_2_4/", C6_2_4Reports.as_view(), name="rc6_2_4"),

    path("create/c6_3_1", CV6_3_1CreateView.as_view(), name="cc6_3_1"),
    path("edit/c6_3_1/<int:pk>", CV6_3_1UpdateView.as_view(), name="uc6_3_1"),
    path("adv-reports/c6_3_1/", C6_3_1Reports.as_view(), name="rc6_3_1"),

    path("create/c6_3_2", CV6_3_2CreateView.as_view(), name="cc6_3_2"),
    path("edit/c6_3_2/<int:pk>", CV6_3_2UpdateView.as_view(), name="uc6_3_2"),
    path("adv-reports/c6_3_2/", C6_3_2Reports.as_view(), name="rc6_3_2"),

    path("create/c6_3_3", CV6_3_3CreateView.as_view(), name="cc6_3_3"),
    path("edit/c6_3_3/<int:pk>", CV6_3_3UpdateView.as_view(), name="uc6_3_3"),
    path("adv-reports/c6_3_3/", C6_3_3Reports.as_view(), name="rc6_3_3"),

    path("create/c6_3_4", CV6_3_4CreateView.as_view(), name="cc6_3_4"),
    path("edit/c6_3_4/<int:pk>", CV6_3_4UpdateView.as_view(), name="uc6_3_4"),
    path("adv-reports/c6_3_4/", C6_3_4Reports.as_view(), name="rc6_3_4"),

    path("create/c6_3_5", CV6_3_5CreateView.as_view(), name="cc6_3_5"),
    path("edit/c6_3_5/<int:pk>", CV6_3_5UpdateView.as_view(), name="uc6_3_5"),
    path("adv-reports/c6_3_5/", C6_3_5Reports.as_view(), name="rc6_3_5"),

    path("create/c6_4_1", CV6_4_1CreateView.as_view(), name="cc6_4_1"),
    path("edit/c6_4_1/<int:pk>", CV6_4_1UpdateView.as_view(), name="uc6_4_1"),
    path("adv-reports/c6_4_1/", C6_4_1Reports.as_view(), name="rc6_4_1"),

    path("create/c6_4_2", CV6_4_2CreateView.as_view(), name="cc6_4_2"),
    path("edit/c6_4_2/<int:pk>", CV6_4_2UpdateView.as_view(), name="uc6_4_2"),
    path("adv-reports/c6_4_2/", C6_4_2Reports.as_view(), name="rc6_4_2"),

    path("create/c6_4_3", CV6_4_3CreateView.as_view(), name="cc6_4_3"),
    path("edit/c6_4_3/<int:pk>", CV6_4_3UpdateView.as_view(), name="uc6_4_3"),
    path("adv-reports/c6_4_3/", C6_4_3Reports.as_view(), name="rc6_4_3"),

    path("create/c6_5_1", CV6_5_1CreateView.as_view(), name="cc6_5_1"),
    path("edit/c6_5_1/<int:pk>", CV6_5_1UpdateView.as_view(), name="uc6_5_1"),
    path("adv-reports/c6_5_1/", C6_5_1Reports.as_view(), name="rc6_5_1"),

    path("create/c6_5_2", CV6_5_2CreateView.as_view(), name="cc6_5_2"),
    path("edit/c6_5_2/<int:pk>", CV6_5_2UpdateView.as_view(), name="uc6_5_2"),
    path("adv-reports/c6_5_2/", C6_5_2Reports.as_view(), name="rc6_5_2"),

    path("create/c6_5_3", CV6_5_3CreateView.as_view(), name="cc6_5_3"),
    path("edit/c6_5_3/<int:pk>", CV6_5_3UpdateView.as_view(), name="uc6_5_3"),
    path("adv-reports/c6_5_3/", C6_5_3Reports.as_view(), name="rc6_5_3"),

    path("create/c6_5_4", CV6_5_4CreateView.as_view(), name="cc6_5_4"),
    path("edit/c6_5_4/<int:pk>", CV6_5_4UpdateView.as_view(), name="uc6_5_4"),
    path("adv-reports/c6_5_4/", C6_5_4Reports.as_view(), name="rc6_5_4"),

    path("create/c6_5_5", CV6_5_5CreateView.as_view(), name="cc6_5_5"),
    path("edit/c6_5_5/<int:pk>", CV6_5_5UpdateView.as_view(), name="uc6_5_5"),
    path("adv-reports/c6_5_5/", C6_5_5Reports.as_view(), name="rc6_5_5"),

    path("create/c7_1_1", CV7_1_1CreateView.as_view(), name="cc7_1_1"),
    path("edit/c7_1_1/<int:pk>", CV7_1_1UpdateView.as_view(), name="uc7_1_1"),
    path("adv-reports/c7_1_1/", C7_1_1Reports.as_view(), name="rc7_1_1"),

    path("create/c7_1_2A", CV7_1_2ACreateView.as_view(), name="cc7_1_2A"),
    path("edit/c7_1_2A/<int:pk>", CV7_1_2AUpdateView.as_view(), name="uc7_1_2A"),
    path("adv-reports/c7_1_2A/", C7_1_2AReports.as_view(), name="rc7_1_2A"),

    path("create/c7_1_2B", CV7_1_2BCreateView.as_view(), name="cc7_1_2B"),
    path("edit/c7_1_2B/<int:pk>", CV7_1_2BUpdateView.as_view(), name="uc7_1_2B"),
    path("adv-reports/c7_1_2B/", C7_1_2BReports.as_view(), name="rc7_1_2B"),

    path("create/c7_1_2C", CV7_1_2CCreateView.as_view(), name="cc7_1_2C"),
    path("edit/c7_1_2C/<int:pk>", CV7_1_2CUpdateView.as_view(), name="uc7_1_2C"),
    path("adv-reports/c7_1_2C/", C7_1_2CReports.as_view(), name="rc7_1_2C"),

    path("create/c7_1_3", CV7_1_3CreateView.as_view(), name="cc7_1_3"),
    path("edit/c7_1_3/<int:pk>", CV7_1_3UpdateView.as_view(), name="uc7_1_3"),
    path("adv-reports/c7_1_3/", C7_1_3Reports.as_view(), name="rc7_1_3"),

    path("create/c7_1_4", CV7_1_4CreateView.as_view(), name="cc7_1_4"),
    path("edit/c7_1_4/<int:pk>", CV7_1_4UpdateView.as_view(), name="uc7_1_4"),
    path("adv-reports/c7_1_4/", C7_1_4Reports.as_view(), name="rc7_1_4"),

    path("create/c7_1_5", CV7_1_5CreateView.as_view(), name="cc7_1_5"),
    path("edit/c7_1_5/<int:pk>", CV7_1_5UpdateView.as_view(), name="uc7_1_5"),
    path("adv-reports/c7_1_5/", C7_1_5Reports.as_view(), name="rc7_1_5"),

    path("create/c7_1_6", CV7_1_6CreateView.as_view(), name="cc7_1_6"),
    path("edit/c7_1_6/<int:pk>", CV7_1_6UpdateView.as_view(), name="uc7_1_6"),
    path("adv-reports/c7_1_6/", C7_1_6Reports.as_view(), name="rc7_1_6"),

    path("create/c7_1_7A", CV7_1_7ACreateView.as_view(), name="cc7_1_7A"),
    path("edit/c7_1_7A/<int:pk>", CV7_1_7AUpdateView.as_view(), name="uc7_1_7A"),
    path("adv-reports/c7_1_7A/", C7_1_7AReports.as_view(), name="rc7_1_7A"),

    path("create/c7_1_7B", CV7_1_7BCreateView.as_view(), name="cc7_1_7B"),
    path("edit/c7_1_7B/<int:pk>", CV7_1_7BUpdateView.as_view(), name="uc7_1_7B"),
    path("adv-reports/c7_1_7B/", C7_1_7BReports.as_view(), name="rc7_1_7B"),

    path("create/c7_1_7C", CV7_1_7CCreateView.as_view(), name="cc7_1_7C"),
    path("edit/c7_1_7C/<int:pk>", CV7_1_7CUpdateView.as_view(), name="uc7_1_7C"),
    path("adv-reports/c7_1_7C/", C7_1_7CReports.as_view(), name="rc7_1_7C"),

    path("create/c7_1_7D", CV7_1_7DCreateView.as_view(), name="cc7_1_7D"),
    path("edit/c7_1_7D/<int:pk>", CV7_1_7DUpdateView.as_view(), name="uc7_1_7D"),
    path("adv-reports/c7_1_7D/", C7_1_7DReports.as_view(), name="rc7_1_7D"),

    path("create/c7_1_8", CV7_1_8CreateView.as_view(), name="cc7_1_8"),
    path("edit/c7_1_8/<int:pk>", CV7_1_8UpdateView.as_view(), name="uc7_1_8"),
    path("adv-reports/c7_1_8/", C7_1_8Reports.as_view(), name="rc7_1_8"),

    path("create/c7_1_9", CV7_1_9CreateView.as_view(), name="cc7_1_9"),
    path("edit/c7_1_9/<int:pk>", CV7_1_9UpdateView.as_view(), name="uc7_1_9"),
    path("adv-reports/c7_1_9/", C7_1_9Reports.as_view(), name="rc7_1_9"),

    path("create/c7_1_10", CV7_1_10CreateView.as_view(), name="cc7_1_10"),
    path("edit/c7_1_10/<int:pk>", CV7_1_10UpdateView.as_view(), name="uc7_1_10"),
    path("adv-reports/c7_1_10/", C7_1_10Reports.as_view(), name="rc7_1_10"),

    path("create/c7_1_11", CV7_1_11CreateView.as_view(), name="cc7_1_11"),
    path("edit/c7_1_11/<int:pk>", CV7_1_11UpdateView.as_view(), name="uc7_1_11"),
    path("adv-reports/c7_1_11/", C7_1_11Reports.as_view(), name="rc7_1_11"),

    path("create/c7_1_12", CV7_1_12CreateView.as_view(), name="cc7_1_12"),
    path("edit/c7_1_12/<int:pk>", CV7_1_12UpdateView.as_view(), name="uc7_1_12"),
    path("adv-reports/c7_1_12/", C7_1_12Reports.as_view(), name="rc7_1_12"),

    path("create/c7_1_13", CV7_1_13CreateView.as_view(), name="cc7_1_13"),
    path("edit/c7_1_13/<int:pk>", CV7_1_13UpdateView.as_view(), name="uc7_1_13"),
    path("adv-reports/c7_1_13/", C7_1_13Reports.as_view(), name="rc7_1_13"),

    path("create/c7_1_14", CV7_1_14CreateView.as_view(), name="cc7_1_14"),
    path("edit/c7_1_14/<int:pk>", CV7_1_14UpdateView.as_view(), name="uc7_1_14"),
    path("adv-reports/c7_1_14/", C7_1_14Reports.as_view(), name="rc7_1_14"),

    path("create/c7_1_15", CV7_1_15CreateView.as_view(), name="cc7_1_15"),
    path("edit/c7_1_15/<int:pk>", CV7_1_15UpdateView.as_view(), name="uc7_1_15"),
    path("adv-reports/c7_1_15/", C7_1_15Reports.as_view(), name="rc7_1_15"),

    path("create/c7_1_16", CV7_1_16CreateView.as_view(), name="cc7_1_16"),
    path("edit/c7_1_16/<int:pk>", CV7_1_16UpdateView.as_view(), name="uc7_1_16"),
    path("adv-reports/c7_1_16/", C7_1_16Reports.as_view(), name="rc7_1_16"),

    path("create/c7_1_17", CV7_1_17CreateView.as_view(), name="cc7_1_17"),
    path("edit/c7_1_17/<int:pk>", CV7_1_17UpdateView.as_view(), name="uc7_1_17"),
    path("adv-reports/c7_1_17/", C7_1_17Reports.as_view(), name="rc7_1_17"),

    path("create/c7_1_18", CV7_1_18CreateView.as_view(), name="cc7_1_18"),
    path("edit/c7_1_18/<int:pk>", CV7_1_18UpdateView.as_view(), name="uc7_1_18"),
    path("adv-reports/c7_1_18/", C7_1_18Reports.as_view(), name="rc7_1_18"),

    path("create/c7_1_19", CV7_1_19CreateView.as_view(), name="cc7_1_19"),
    path("edit/c7_1_19/<int:pk>", CV7_1_19UpdateView.as_view(), name="uc7_1_19"),
    path("adv-reports/c7_1_19/", C7_1_19Reports.as_view(), name="rc7_1_19"),

    path("create/c7_2_1", CV7_2_1CreateView.as_view(), name="cc7_2_1"),
    path("edit/c7_2_1/<int:pk>", CV7_2_1UpdateView.as_view(), name="uc7_2_1"),
    path("adv-reports/c7_2_1/", C7_2_1Reports.as_view(), name="rc7_2_1"),

    path("create/c7_3_1", CV7_3_1CreateView.as_view(), name="cc7_3_1"),
    path("edit/c7_3_1/<int:pk>", CV7_3_1UpdateView.as_view(), name="uc7_3_1"),
    path("adv-reports/c7_3_1/", C7_3_1Reports.as_view(), name="rc7_3_1"),

]
