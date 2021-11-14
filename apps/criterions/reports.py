# Criterions/ reports.py
from contextlib import suppress

from django.shortcuts import render
from django.views import View
from django.db import models as dmodels
from .forms import *
from ..adminapp.models import FinalCriteria
from .models import CriterionMaster
from .fields.generate_report import *


def apply_filter(post_data, criteria):
    fdate = post_data['fdate']
    tdate = post_data['tdate']
    status = post_data['status']
    try:
        department_id = post_data['department']
    except:
        department_id = None
    try:
        program_id = post_data['program']

    except:
        program_id = None

    try:
        paper_id = post_data['paper'] #batch
    except:
        paper_id = None
    try:
        batch_id = post_data['batch']  # batch
    except:
        batch_id = None

    filters = dmodels.Q(criterion=criteria) if criteria else dmodels.Q()
    filters &= dmodels.Q(department=department_id) if department_id else dmodels.Q()
    filters &= dmodels.Q(program=program_id) if program_id else dmodels.Q()
    filters &= dmodels.Q(paper=paper_id) if paper_id else dmodels.Q()
    filters &= dmodels.Q(batch=batch_id) if paper_id else dmodels.Q()
    filters &= dmodels.Q(status=status) if status else dmodels.Q()
    start_date = fdate if fdate else "2001-01-01"  # If no from date applied start from 2001
    end_date = tdate if tdate else "3021-12-31"  # If no End date applied Search up to 3021
    filters &= dmodels.Q(date__range=[start_date, end_date])
    return filters


class C1_1_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c1_1_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c1_1_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data':cr_data}
            return render(request, "criteria/reports/c1_1_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c1_1_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c1_1_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c1_1_1", "filters": filters})
        return data

    def get(self, request):
        form = C1_1_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c1_1_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


class C1_1_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c1_1_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list}
            return render(request, "criteria/reports/c1_1_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c1_1_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c1_1_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c1_1_2", "filters": filters})
        return data

    def get(self, request):
        form = C1_1_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c1_1_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


class C1_1_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c1_1_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list}
            return render(request, "criteria/reports/c1_1_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c1_1_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c1_1_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c1_1_3", "filters": filters})
        return data

    def get(self, request):
        form = C1_1_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c1_1_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


class C1_2_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c1_2_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list}
            return render(request, "criteria/reports/c1_2_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c1_2_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c1_2_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c1_2_1", "filters": filters})
        return data

    def get(self, request):
        form = C1_2_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c1_2_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


class C1_2_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c1_2_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list}
            return render(request, "criteria/reports/c1_2_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c1_2_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c1_2_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c1_2_2", "filters": filters})
        return data

    def get(self, request):
        form = C1_2_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c1_2_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


class C1_3_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c1_3_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list}
            return render(request, "criteria/reports/c1_3_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c1_3_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c1_3_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c1_3_1", "filters": filters})
        return data

    def get(self, request):
        form = C1_3_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c1_3_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


class C1_3_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c1_3_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list}
            return render(request, "criteria/reports/c1_3_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c1_3_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c1_3_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c1_3_2", "filters": filters})
        return data

    def get(self, request):
        form = C1_3_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c1_3_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


class C1_3_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c1_3_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list}
            return render(request, "criteria/reports/c1_3_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c1_3_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c1_3_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c1_3_3", "filters": filters})
        return data

    def get(self, request):
        form = C1_3_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c1_3_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


class C1_3_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c1_3_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list}
            return render(request, "criteria/reports/c1_3_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c1_3_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c1_3_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c1_3_4", "filters": filters})
        return data

    def get(self, request):
        form = C1_3_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c1_3_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


class C1_4_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c1_4_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list}
            return render(request, "criteria/reports/c1_4_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c1_4_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c1_4_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c1_4_1", "filters": filters})
        return data

    def get(self, request):
        form = C1_4_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c1_4_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


class C1_4_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c1_4_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list}
            return render(request, "criteria/reports/c1_4_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c1_4_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c1_4_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c1_4_2", "filters": filters})
        return data

    def get(self, request):
        form = C1_4_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c1_4_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_1_1 *  ----------------------------- #
class C2_1_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_1_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_1_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_1_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_1_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_1_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_1_1", "filters": filters})
        return data

    def get(self, request):
        form = C2_1_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_1_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_1_2 *  ----------------------------- #
class C2_1_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_1_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_1_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_1_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_1_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_1_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_1_2", "filters": filters})
        return data

    def get(self, request):
        form = C2_1_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_1_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_1_3 *  ----------------------------- #
class C2_1_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_1_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_1_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_1_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_1_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_1_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_1_3", "filters": filters})
        return data

    def get(self, request):
        form = C2_1_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_1_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_2_1 *  ----------------------------- #
class C2_2_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_2_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_2_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_2_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_2_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_2_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_2_1", "filters": filters})
        return data

    def get(self, request):
        form = C2_2_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_2_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_2_2 *  ----------------------------- #
class C2_2_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_2_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_2_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_2_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_2_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_2_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_2_2", "filters": filters})
        return data

    def get(self, request):
        form = C2_2_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_2_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_2_3 *  ----------------------------- #
class C2_2_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_2_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_2_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_2_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_2_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_2_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_2_3", "filters": filters})
        return data

    def get(self, request):
        form = C2_2_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_2_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_3_1 *  ----------------------------- #
class C2_3_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_3_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_3_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_3_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_3_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_3_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_3_1", "filters": filters})
        return data

    def get(self, request):
        form = C2_3_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_3_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_3_2 *  ----------------------------- #
class C2_3_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_3_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_3_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_3_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_3_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_3_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_3_2", "filters": filters})
        return data

    def get(self, request):
        form = C2_3_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_3_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_3_3 *  ----------------------------- #
class C2_3_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_3_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_3_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_3_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_3_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_3_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_3_3", "filters": filters})
        return data

    def get(self, request):
        form = C2_3_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_3_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_3_4 *  ----------------------------- #
class C2_3_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_3_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_3_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_3_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_3_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_3_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_3_4", "filters": filters})
        return data

    def get(self, request):
        form = C2_3_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_3_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_4_1 *  ----------------------------- #
class C2_4_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_4_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_4_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_4_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_4_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_4_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_4_1", "filters": filters})
        return data

    def get(self, request):
        form = C2_4_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_4_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_4_2 *  ----------------------------- #
class C2_4_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_4_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_4_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_4_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_4_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_4_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_4_2", "filters": filters})
        return data

    def get(self, request):
        form = C2_4_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_4_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_4_3 *  ----------------------------- #
class C2_4_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_4_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_4_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_4_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_4_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_4_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_4_3", "filters": filters})
        return data

    def get(self, request):
        form = C2_4_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_4_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_4_4 *  ----------------------------- #
class C2_4_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_4_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_4_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_4_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_4_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_4_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_4_4", "filters": filters})
        return data

    def get(self, request):
        form = C2_4_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_4_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_4_5 *  ----------------------------- #
class C2_4_5Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_4_5")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_4_5")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_4_5.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_4_5", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_4_5", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_4_5", "filters": filters})
        return data

    def get(self, request):
        form = C2_4_5SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_4_5")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_5_1 *  ----------------------------- #
class C2_5_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_5_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_5_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_5_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_5_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_5_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_5_1", "filters": filters})
        return data

    def get(self, request):
        form = C2_5_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_5_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_5_2 *  ----------------------------- #
class C2_5_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_5_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_5_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_5_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_5_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_5_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_5_2", "filters": filters})
        return data

    def get(self, request):
        form = C2_5_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_5_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_5_3 *  ----------------------------- #
class C2_5_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_5_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_5_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_5_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_5_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_5_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_5_3", "filters": filters})
        return data

    def get(self, request):
        form = C2_5_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_5_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_5_4 *  ----------------------------- #
class C2_5_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_5_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_5_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_5_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_5_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_5_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_5_4", "filters": filters})
        return data

    def get(self, request):
        form = C2_5_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_5_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_5_5 *  ----------------------------- #
class C2_5_5Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_5_5")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_5_5")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_5_5.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_5_5", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_5_5", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_5_5", "filters": filters})
        return data

    def get(self, request):
        form = C2_5_5SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_5_5")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_6_1 *  ----------------------------- #
class C2_6_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_6_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_6_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_6_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_6_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_6_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_6_1", "filters": filters})
        return data

    def get(self, request):
        form = C2_6_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_6_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_6_2 *  ----------------------------- #
class C2_6_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_6_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_6_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_6_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_6_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_6_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_6_2", "filters": filters})
        return data

    def get(self, request):
        form = C2_6_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_6_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_6_3 *  ----------------------------- #
class C2_6_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_6_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_6_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_6_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_6_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_6_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_6_3", "filters": filters})
        return data

    def get(self, request):
        form = C2_6_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_6_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 2_7_1 *  ----------------------------- #
class C2_7_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c2_7_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c2_7_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c2_7_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c2_7_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c2_7_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c2_7_1", "filters": filters})
        return data

    def get(self, request):
        form = C2_7_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c2_7_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_1_1 *  ----------------------------- #
class C3_1_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_1_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_1_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_1_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_1_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_1_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_1_1", "filters": filters})
        return data

    def get(self, request):
        form = C3_1_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_1_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_1_2 *  ----------------------------- #
class C3_1_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_1_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_1_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_1_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_1_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_1_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_1_2", "filters": filters})
        return data

    def get(self, request):
        form = C3_1_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_1_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_1_3 *  ----------------------------- #
class C3_1_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_1_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_1_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_1_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_1_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_1_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_1_3", "filters": filters})
        return data

    def get(self, request):
        form = C3_1_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_1_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_1_4 *  ----------------------------- #
class C3_1_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_1_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_1_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_1_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_1_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_1_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_1_4", "filters": filters})
        return data

    def get(self, request):
        form = C3_1_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_1_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_2_1 *  ----------------------------- #
class C3_2_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_2_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_2_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_2_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_2_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_2_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_2_1", "filters": filters})
        return data

    def get(self, request):
        form = C3_2_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_2_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_2_2 *  ----------------------------- #
class C3_2_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_2_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_2_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_2_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_2_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_2_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_2_2", "filters": filters})
        return data

    def get(self, request):
        form = C3_2_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_2_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_2_3 *  ----------------------------- #
class C3_2_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_2_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_2_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_2_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_2_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_2_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_2_3", "filters": filters})
        return data

    def get(self, request):
        form = C3_2_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_2_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_2_4 *  ----------------------------- #
class C3_2_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_2_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_2_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_2_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_2_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_2_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_2_4", "filters": filters})
        return data

    def get(self, request):
        form = C3_2_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_2_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_3_1 *  ----------------------------- #
class C3_3_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_3_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_3_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_3_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_3_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_3_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_3_1", "filters": filters})
        return data

    def get(self, request):
        form = C3_3_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_3_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_3_2 *  ----------------------------- #
class C3_3_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_3_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_3_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_3_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_3_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_3_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_3_2", "filters": filters})
        return data

    def get(self, request):
        form = C3_3_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_3_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_3_3 *  ----------------------------- #
class C3_3_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_3_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_3_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_3_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_3_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_3_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_3_3", "filters": filters})
        return data

    def get(self, request):
        form = C3_3_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_3_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_4_1 *  ----------------------------- #
class C3_4_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_4_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_4_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_4_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_4_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_4_1", "filters": filters})
        return data

    def get(self, request):
        form = C3_4_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_4_2 *  ----------------------------- #
class C3_4_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_4_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_4_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_4_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_4_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_4_2", "filters": filters})
        return data

    def get(self, request):
        form = C3_4_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_4_3 *  ----------------------------- #
class C3_4_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_4_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_4_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_4_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_4_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_4_3", "filters": filters})
        return data

    def get(self, request):
        form = C3_4_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_4_4 *  ----------------------------- #
class C3_4_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_4_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_4_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_4_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_4_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_4_4", "filters": filters})
        return data

    def get(self, request):
        form = C3_4_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_4_5 *  ----------------------------- #
class C3_4_5Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_4_5")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_5")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_4_5.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_4_5", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_4_5", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_4_5", "filters": filters})
        return data

    def get(self, request):
        form = C3_4_5SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_5")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_4_6 *  ----------------------------- #
class C3_4_6Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_4_6")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_6")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_4_6.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_4_6", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_4_6", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_4_6", "filters": filters})
        return data

    def get(self, request):
        form = C3_4_6SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_6")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_4_7 *  ----------------------------- #
class C3_4_7Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_4_7")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_7")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_4_7.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_4_7", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_4_7", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_4_7", "filters": filters})
        return data

    def get(self, request):
        form = C3_4_7SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_7")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_4_8 *  ----------------------------- #
class C3_4_8Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_4_8")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_8")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_4_8.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_4_8", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_4_8", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_4_8", "filters": filters})
        return data

    def get(self, request):
        form = C3_4_8SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_4_8")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_5_1 *  ----------------------------- #
class C3_5_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_5_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_5_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_5_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_5_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_5_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_5_1", "filters": filters})
        return data

    def get(self, request):
        form = C3_5_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_5_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_5_2 *  ----------------------------- #
class C3_5_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_5_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_5_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_5_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_5_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_5_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_5_2", "filters": filters})
        return data

    def get(self, request):
        form = C3_5_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_5_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_5_3 *  ----------------------------- #
class C3_5_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_5_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_5_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_5_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_5_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_5_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_5_3", "filters": filters})
        return data

    def get(self, request):
        form = C3_5_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_5_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_6_1 *  ----------------------------- #
class C3_6_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_6_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_6_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_6_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_6_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_6_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_6_1", "filters": filters})
        return data

    def get(self, request):
        form = C3_6_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_6_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_6_2 *  ----------------------------- #
class C3_6_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_6_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_6_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_6_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_6_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_6_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_6_2", "filters": filters})
        return data

    def get(self, request):
        form = C3_6_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_6_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_6_3 *  ----------------------------- #
class C3_6_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_6_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_6_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_6_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_6_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_6_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_6_3", "filters": filters})
        return data

    def get(self, request):
        form = C3_6_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_6_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_6_4 *  ----------------------------- #
class C3_6_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_6_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_6_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_6_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_6_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_6_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_6_4", "filters": filters})
        return data

    def get(self, request):
        form = C3_6_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_6_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_7_1 *  ----------------------------- #
class C3_7_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_7_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_7_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_7_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_7_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_7_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_7_1", "filters": filters})
        return data

    def get(self, request):
        form = C3_7_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_7_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_7_2 *  ----------------------------- #
class C3_7_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_7_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_7_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_7_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_7_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_7_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_7_2", "filters": filters})
        return data

    def get(self, request):
        form = C3_7_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_7_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 3_7_3 *  ----------------------------- #
class C3_7_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c3_7_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c3_7_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c3_7_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c3_7_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c3_7_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c3_7_3", "filters": filters})
        return data

    def get(self, request):
        form = C3_7_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c3_7_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_1_1 *  ----------------------------- #
class C4_1_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_1_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_1_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_1_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_1_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_1_1", "filters": filters})
        return data

    def get(self, request):
        form = C4_1_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_1_2 *  ----------------------------- #
class C4_1_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_1_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_1_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_1_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_1_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_1_2", "filters": filters})
        return data

    def get(self, request):
        form = C4_1_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_1_2A *  ----------------------------- #
class C4_1_2AReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_1_2A")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2A")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_1_2A.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_1_2A", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_1_2A", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_1_2A", "filters": filters})
        return data

    def get(self, request):
        form = C4_1_2ASearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2A")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_1_2B *  ----------------------------- #
class C4_1_2BReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_1_2B")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2B")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_1_2B.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_1_2B", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_1_2B", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_1_2B", "filters": filters})
        return data

    def get(self, request):
        form = C4_1_2BSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2B")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_1_2C *  ----------------------------- #
class C4_1_2CReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_1_2C")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2C")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_1_2C.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_1_2C", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_1_2C", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_1_2C", "filters": filters})
        return data

    def get(self, request):
        form = C4_1_2CSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2C")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_1_2D *  ----------------------------- #
class C4_1_2DReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_1_2D")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2D")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_1_2D.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_1_2D", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_1_2D", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_1_2D", "filters": filters})
        return data

    def get(self, request):
        form = C4_1_2DSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2D")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_1_2E *  ----------------------------- #
class C4_1_2EReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_1_2E")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2E")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_1_2E.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_1_2E", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_1_2E", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_1_2E", "filters": filters})
        return data

    def get(self, request):
        form = C4_1_2ESearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_2E")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_1_3 *  ----------------------------- #
class C4_1_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_1_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_1_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_1_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_1_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_1_3", "filters": filters})
        return data

    def get(self, request):
        form = C4_1_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_1_4 *  ----------------------------- #
class C4_1_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_1_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_1_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_1_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_1_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_1_4", "filters": filters})
        return data

    def get(self, request):
        form = C4_1_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_1_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_2_1 *  ----------------------------- #
class C4_2_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_2_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_2_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_2_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_2_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_2_1", "filters": filters})
        return data

    def get(self, request):
        form = C4_2_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_2_2 *  ----------------------------- #
class C4_2_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_2_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_2_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_2_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_2_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_2_2", "filters": filters})
        return data

    def get(self, request):
        form = C4_2_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_2_3 *  ----------------------------- #
class C4_2_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_2_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_2_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_2_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_2_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_2_3", "filters": filters})
        return data

    def get(self, request):
        form = C4_2_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_2_4 *  ----------------------------- #
class C4_2_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_2_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_2_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_2_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_2_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_2_4", "filters": filters})
        return data

    def get(self, request):
        form = C4_2_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_2_5 *  ----------------------------- #
class C4_2_5Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_2_5")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_5")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_2_5.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_2_5", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_2_5", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_2_5", "filters": filters})
        return data

    def get(self, request):
        form = C4_2_5SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_5")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_2_6 *  ----------------------------- #
class C4_2_6Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_2_6")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_6")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_2_6.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_2_6", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_2_6", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_2_6", "filters": filters})
        return data

    def get(self, request):
        form = C4_2_6SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_2_6")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_3_1 *  ----------------------------- #
class C4_3_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_3_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_3_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_3_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_3_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_3_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_3_1", "filters": filters})
        return data

    def get(self, request):
        form = C4_3_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_3_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_3_2 *  ----------------------------- #
class C4_3_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_3_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_3_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_3_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_3_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_3_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_3_2", "filters": filters})
        return data

    def get(self, request):
        form = C4_3_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_3_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_3_3 *  ----------------------------- #
class C4_3_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_3_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_3_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_3_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_3_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_3_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_3_3", "filters": filters})
        return data

    def get(self, request):
        form = C4_3_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_3_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_3_4 *  ----------------------------- #
class C4_3_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_3_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_3_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_3_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_3_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_3_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_3_4", "filters": filters})
        return data

    def get(self, request):
        form = C4_3_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_3_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_4_1 *  ----------------------------- #
class C4_4_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_4_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_4_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_4_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_4_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_4_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_4_1", "filters": filters})
        return data

    def get(self, request):
        form = C4_4_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_4_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 4_4_2 *  ----------------------------- #
class C4_4_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c4_4_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c4_4_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c4_4_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c4_4_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c4_4_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c4_4_2", "filters": filters})
        return data

    def get(self, request):
        form = C4_4_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c4_4_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_1 *  ----------------------------- #
class C5_1_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_1", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_2 *  ----------------------------- #
class C5_1_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_2", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_3 *  ----------------------------- #
class C5_1_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_3", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_3A *  ----------------------------- #
class C5_1_3AReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_3A")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3A")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_3A.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_3A", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_3A", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_3A", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_3ASearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3A")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_3B *  ----------------------------- #
class C5_1_3BReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_3B")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3B")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_3B.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_3B", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_3B", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_3B", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_3BSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3B")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_3C *  ----------------------------- #
class C5_1_3CReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_3C")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3C")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_3C.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_3C", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_3C", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_3C", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_3CSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3C")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_3D *  ----------------------------- #
class C5_1_3DReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_3D")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3D")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_3D.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_3D", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_3D", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_3D", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_3DSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3D")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_3E *  ----------------------------- #
class C5_1_3EReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_3E")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3E")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_3E.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_3E", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_3E", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_3E", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_3ESearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3E")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_3F *  ----------------------------- #
class C5_1_3FReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_3F")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3F")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_3F.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_3F", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_3F", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_3F", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_3FSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3F")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_3G *  ----------------------------- #
class C5_1_3GReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_3G")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3G")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_3G.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_3G", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_3G", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_3G", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_3GSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3G")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_3H *  ----------------------------- #
class C5_1_3HReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_3H")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3H")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_3H.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_3H", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_3H", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_3H", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_3HSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_3H")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_4 *  ----------------------------- #
class C5_1_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_4", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_5 *  ----------------------------- #
class C5_1_5Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_5")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_5")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_5.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_5", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_5", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_5", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_5SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_5")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_1_6 *  ----------------------------- #
class C5_1_6Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_1_6")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_6")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_1_6.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_1_6", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_1_6", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_1_6", "filters": filters})
        return data

    def get(self, request):
        form = C5_1_6SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_1_6")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_2_1 *  ----------------------------- #
class C5_2_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_2_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_2_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_2_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_2_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_2_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_2_1", "filters": filters})
        return data

    def get(self, request):
        form = C5_2_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_2_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_2_2 *  ----------------------------- #
class C5_2_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_2_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_2_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_2_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_2_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_2_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_2_2", "filters": filters})
        return data

    def get(self, request):
        form = C5_2_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_2_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_2_3 *  ----------------------------- #
class C5_2_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_2_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_2_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_2_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_2_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_2_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_2_3", "filters": filters})
        return data

    def get(self, request):
        form = C5_2_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_2_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_3_1 *  ----------------------------- #
class C5_3_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_3_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_3_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_3_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_3_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_3_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_3_1", "filters": filters})
        return data

    def get(self, request):
        form = C5_3_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_3_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_3_2 *  ----------------------------- #
class C5_3_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_3_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_3_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_3_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_3_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_3_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_3_2", "filters": filters})
        return data

    def get(self, request):
        form = C5_3_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_3_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_3_2A *  ----------------------------- #
class C5_3_2AReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_3_2A")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_3_2A")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_3_2A.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_3_2A", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_3_2A", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_3_2A", "filters": filters})
        return data

    def get(self, request):
        form = C5_3_2ASearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_3_2A")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_3_2B *  ----------------------------- #
class C5_3_2BReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_3_2B")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_3_2B")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_3_2B.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_3_2B", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_3_2B", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_3_2B", "filters": filters})
        return data

    def get(self, request):
        form = C5_3_2BSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_3_2B")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_3_3 *  ----------------------------- #
class C5_3_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_3_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_3_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_3_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_3_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_3_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_3_3", "filters": filters})
        return data

    def get(self, request):
        form = C5_3_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_3_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_4_1A *  ----------------------------- #
class C5_4_1AReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_4_1A")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_4_1A")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_4_1A.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_4_1A", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_4_1A", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_4_1A", "filters": filters})
        return data

    def get(self, request):
        form = C5_4_1ASearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_4_1A")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_4_1B *  ----------------------------- #
class C5_4_1BReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_4_1B")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_4_1B")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_4_1B.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_4_1B", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_4_1B", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_4_1B", "filters": filters})
        return data

    def get(self, request):
        form = C5_4_1BSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_4_1B")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 5_4_2 *  ----------------------------- #
class C5_4_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c5_4_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c5_4_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c5_4_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c5_4_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c5_4_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c5_4_2", "filters": filters})
        return data

    def get(self, request):
        form = C5_4_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c5_4_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_1_1 *  ----------------------------- #
class C6_1_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_1_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_1_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_1_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_1_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_1_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_1_1", "filters": filters})
        return data

    def get(self, request):
        form = C6_1_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_1_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_1_2 *  ----------------------------- #
class C6_1_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_1_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_1_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_1_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_1_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_1_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_1_2", "filters": filters})
        return data

    def get(self, request):
        form = C6_1_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_1_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_2_1 *  ----------------------------- #
class C6_2_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_2_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_2_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_2_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_2_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_2_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_2_1", "filters": filters})
        return data

    def get(self, request):
        form = C6_2_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_2_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_2_2 *  ----------------------------- #
class C6_2_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_2_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_2_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_2_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_2_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_2_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_2_2", "filters": filters})
        return data

    def get(self, request):
        form = C6_2_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_2_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_2_3 *  ----------------------------- #
class C6_2_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_2_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_2_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_2_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_2_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_2_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_2_3", "filters": filters})
        return data

    def get(self, request):
        form = C6_2_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_2_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_2_4 *  ----------------------------- #
class C6_2_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_2_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_2_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_2_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_2_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_2_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_2_4", "filters": filters})
        return data

    def get(self, request):
        form = C6_2_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_2_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_3_1 *  ----------------------------- #
class C6_3_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_3_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_3_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_3_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_3_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_3_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_3_1", "filters": filters})
        return data

    def get(self, request):
        form = C6_3_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_3_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_3_2 *  ----------------------------- #
class C6_3_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_3_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_3_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_3_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_3_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_3_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_3_2", "filters": filters})
        return data

    def get(self, request):
        form = C6_3_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_3_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_3_3 *  ----------------------------- #
class C6_3_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_3_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_3_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_3_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_3_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_3_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_3_3", "filters": filters})
        return data

    def get(self, request):
        form = C6_3_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_3_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_3_4 *  ----------------------------- #
class C6_3_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_3_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_3_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_3_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_3_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_3_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_3_4", "filters": filters})
        return data

    def get(self, request):
        form = C6_3_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_3_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_3_5 *  ----------------------------- #
class C6_3_5Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_3_5")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_3_5")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_3_5.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_3_5", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_3_5", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_3_5", "filters": filters})
        return data

    def get(self, request):
        form = C6_3_5SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_3_5")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_4_1 *  ----------------------------- #
class C6_4_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_4_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_4_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_4_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_4_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_4_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_4_1", "filters": filters})
        return data

    def get(self, request):
        form = C6_4_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_4_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_4_2 *  ----------------------------- #
class C6_4_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_4_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_4_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_4_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_4_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_4_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_4_2", "filters": filters})
        return data

    def get(self, request):
        form = C6_4_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_4_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_4_3 *  ----------------------------- #
class C6_4_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_4_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_4_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_4_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_4_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_4_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_4_3", "filters": filters})
        return data

    def get(self, request):
        form = C6_4_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_4_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_5_1 *  ----------------------------- #
class C6_5_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_5_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_5_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_5_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_5_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_5_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_5_1", "filters": filters})
        return data

    def get(self, request):
        form = C6_5_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_5_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_5_2 *  ----------------------------- #
class C6_5_2Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_5_2")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_5_2")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_5_2.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_5_2", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_5_2", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_5_2", "filters": filters})
        return data

    def get(self, request):
        form = C6_5_2SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_5_2")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_5_3 *  ----------------------------- #
class C6_5_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_5_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_5_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_5_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_5_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_5_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_5_3", "filters": filters})
        return data

    def get(self, request):
        form = C6_5_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_5_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_5_4 *  ----------------------------- #
class C6_5_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_5_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_5_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_5_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_5_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_5_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_5_4", "filters": filters})
        return data

    def get(self, request):
        form = C6_5_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_5_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 6_5_5 *  ----------------------------- #
class C6_5_5Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c6_5_5")
        cr_data = FinalCriteria.objects.get(criteria_id="c6_5_5")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c6_5_5.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c6_5_5", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c6_5_5", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c6_5_5", "filters": filters})
        return data

    def get(self, request):
        form = C6_5_5SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c6_5_5")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_1 *  ----------------------------- #
class C7_1_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_1", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_2A *  ----------------------------- #
class C7_1_2AReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_2A")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_2A")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_2A.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_2A", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_2A", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_2A", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_2ASearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_2A")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_2B *  ----------------------------- #
class C7_1_2BReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_2B")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_2B")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_2B.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_2B", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_2B", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_2B", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_2BSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_2B")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_2C *  ----------------------------- #
class C7_1_2CReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_2C")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_2C")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_2C.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_2C", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_2C", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_2C", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_2CSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_2C")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_3 *  ----------------------------- #
class C7_1_3Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_3")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_3")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_3.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_3", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_3", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_3", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_3SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_3")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_4 *  ----------------------------- #
class C7_1_4Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_4")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_4")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_4.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_4", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_4", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_4", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_4SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_4")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_5 *  ----------------------------- #
class C7_1_5Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_5")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_5")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_5.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_5", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_5", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_5", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_5SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_5")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_6 *  ----------------------------- #
class C7_1_6Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_6")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_6")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_6.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_6", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_6", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_6", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_6SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_6")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_7A *  ----------------------------- #
class C7_1_7AReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_7A")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_7A")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_7A.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_7A", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_7A", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_7A", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_7ASearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_7A")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_7B *  ----------------------------- #
class C7_1_7BReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_7B")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_7B")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_7B.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_7B", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_7B", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_7B", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_7BSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_7B")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_7C *  ----------------------------- #
class C7_1_7CReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_7C")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_7C")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_7C.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_7C", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_7C", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_7C", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_7CSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_7C")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_7D *  ----------------------------- #
class C7_1_7DReports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_7D")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_7D")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_7D.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_7D", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_7D", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_7D", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_7DSearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_7D")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_8 *  ----------------------------- #
class C7_1_8Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_8")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_8")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_8.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_8", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_8", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_8", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_8SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_8")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_9 *  ----------------------------- #
class C7_1_9Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_9")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_9")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_9.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_9", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_9", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_9", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_9SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_9")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_10 *  ----------------------------- #
class C7_1_10Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_10")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_10")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_10.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_10", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_10", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_10", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_10SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_10")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_11 *  ----------------------------- #
class C7_1_11Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_11")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_11")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_11.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_11", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_11", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_11", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_11SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_11")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_12 *  ----------------------------- #
class C7_1_12Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_12")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_12")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_12.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_12", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_12", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_12", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_12SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_12")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_13 *  ----------------------------- #
class C7_1_13Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_13")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_13")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_13.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_13", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_13", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_13", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_13SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_13")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_14 *  ----------------------------- #
class C7_1_14Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_14")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_14")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_14.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_14", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_14", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_14", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_14SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_14")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_15 *  ----------------------------- #
class C7_1_15Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_15")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_15")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_15.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_15", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_15", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_15", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_15SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_15")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_16 *  ----------------------------- #
class C7_1_16Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_16")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_16")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_16.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_16", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_16", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_16", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_16SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_16")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_17 *  ----------------------------- #
class C7_1_17Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_17")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_17")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_17.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_17", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_17", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_17", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_17SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_17")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_18 *  ----------------------------- #
class C7_1_18Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_18")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_18")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_18.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_18", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_18", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_18", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_18SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_18")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_1_19 *  ----------------------------- #
class C7_1_19Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_1_19")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_19")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_1_19.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_1_19", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_1_19", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_1_19", "filters": filters})
        return data

    def get(self, request):
        form = C7_1_19SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_1_19")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_2_1 *  ----------------------------- #
class C7_2_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_2_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_2_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_2_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_2_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_2_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_2_1", "filters": filters})
        return data

    def get(self, request):
        form = C7_2_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_2_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)


# ------------------------- * Report Logic for 7_3_1 *  ----------------------------- #
class C7_3_1Reports(View):
    def post(self, request):
        # Check for applied filters in the HTML form and apply
        filters = apply_filter(request.POST, "c7_3_1")
        cr_data = FinalCriteria.objects.get(criteria_id="c7_3_1")
        type = request.POST['type']
        # Check report type and call appropriate Function
        if str(type) in ["msx", "csv", "pdf"]:
            obj_list = CriterionMaster.objects.filter(filters)
            context = {'objects': obj_list, 'cr_data': cr_data}
            return render(request, "criteria/reports/c7_3_1.html", context)

        elif type == "txtmedia":
            data = generatePdfMedia(request, **{"text": True, "criterion": "c7_3_1", "filters": filters})
        elif type == "notxt":
            data = generatePdfMedia(request, **{"text": False, "criterion": "c7_3_1", "filters": filters})
        elif type == "spdf":
            data = mergePdf(request, **{"criterion": "c7_3_1", "filters": filters})
        return data

    def get(self, request):
        form = C7_3_1SearchForm
        cr_data = FinalCriteria.objects.get(criteria_id="c7_3_1")
        context = {'form': form, 'cr_data': cr_data}
        return render(request, 'criteria/advanced_reports.html', context)
