# Criterions/data_management.py
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from ..models import CriterionMaster
from ...adminapp.models import FinalCriteria
from ..forms import *


# ------------------------- * Data Add and Edit Logic for  1.1.1 *  ----------------------------- #
# Create Criteria 1.1.1
class CV1_1_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C1_1_1CreateForm
    criteria_id = "c1_1_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_1_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_1_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 1.1.1
class CV1_1_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C1_1_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c1_1_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c1_1_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV1_1_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV1_1_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_1_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_1_1UpdateView, self).__init__(*args, **kwargs)


# --------------------------------------- * C 1.1.2 * -----------------------------------------------------------#
# Create Criteria 1.1.2
class CV1_1_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C1_1_2CreateForm
    criteria_id = "c1_1_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_1_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_1_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 1.1.2
class CV1_1_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C1_1_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c1_1_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c1_1_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV1_1_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV1_1_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_1_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_1_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  1.1.3 *  ----------------------------- #
# Create Criteria
class CV1_1_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C1_1_3CreateForm
    criteria_id = "c1_1_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_1_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_1_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria
class CV1_1_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C1_1_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c1_1_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c1_1_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV1_1_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV1_1_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_1_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_1_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  1.2.1 *  ----------------------------- #
# Create Criteria
class CV1_2_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C1_2_1CreateForm
    criteria_id = "c1_2_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_2_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_2_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria
class CV1_2_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C1_2_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c1_2_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c1_2_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV1_2_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV1_2_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_2_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_2_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  1.2.2 *  ----------------------------- #
# Create Criteria
class CV1_2_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C1_2_2CreateForm
    criteria_id = "c1_2_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_2_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_2_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria
class CV1_2_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C1_2_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c1_2_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c1_2_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV1_2_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV1_2_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_2_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_2_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  1.3.1 *  ----------------------------- #
# Create Criteria
class CV1_3_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C1_3_1CreateForm
    criteria_id = "c1_3_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_3_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_3_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria
class CV1_3_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C1_3_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c1_3_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c1_3_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV1_3_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV1_3_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_3_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_3_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  1.3.2 *  ----------------------------- #
# Create Criteria
class CV1_3_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C1_3_2CreateForm
    criteria_id = "c1_3_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_3_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_3_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria
class CV1_3_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C1_3_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c1_3_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c1_3_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV1_3_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV1_3_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_3_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_3_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  1.3.3 *  ----------------------------- #
# Create Criteria
class CV1_3_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C1_3_3CreateForm
    criteria_id = "c1_3_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_3_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_3_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria
class CV1_3_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C1_3_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c1_3_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c1_3_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV1_3_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV1_3_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_3_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_3_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  1.3.4 *  ----------------------------- #
# Create Criteria
class CV1_3_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C1_3_4CreateForm
    criteria_id = "c1_3_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_3_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_3_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria
class CV1_3_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C1_3_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c1_3_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c1_3_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV1_3_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV1_3_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_3_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_3_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  1.4.1 *  ----------------------------- #
# Create Criteria
class CV1_4_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C1_4_1CreateForm
    criteria_id = "c1_4_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_4_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_4_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria
class CV1_4_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C1_4_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c1_4_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c1_4_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV1_4_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV1_4_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_4_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_4_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  1.4.2 *  ----------------------------- #
# Create Criteria
class CV1_4_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C1_4_2CreateForm
    criteria_id = "c1_4_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_4_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_4_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria
class CV1_4_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C1_4_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c1_4_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c1_4_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV1_4_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV1_4_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV1_4_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV1_4_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_1_1 *  ----------------------------- #
# Create Criteria 2_1_1
class CV2_1_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_1_1CreateForm
    criteria_id = "c2_1_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_1_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_1_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_1_1
class CV2_1_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_1_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_1_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_1_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_1_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_1_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_1_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_1_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_1_2 *  ----------------------------- #
# Create Criteria 2_1_2
class CV2_1_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_1_2CreateForm
    criteria_id = "c2_1_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_1_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_1_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_1_2
class CV2_1_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_1_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_1_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_1_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_1_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_1_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_1_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_1_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_1_3 *  ----------------------------- #
# Create Criteria 2_1_3
# class CV2_1_3CreateView(LoginRequiredMixin, CreateView):
#     template_name = "criteria/create.html"
#     success_message = "Successfully Created"
#     form_class = C2_1_3CreateForm
#     criteria_id = "c2_1_3"
#     create_form_url = 'criterions:c' + criteria_id
#     success_url = '/criteria/show/' + criteria_id
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.criterion = self.criteria_id
#         self.object.cr_index = self.criteria_id[1]
#         try:
#             self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
#         except:
#             pass
#         self.object.save()
#         messages.add_message(self.request, messages.SUCCESS, self.success_message)
#         if "add-next" in self.request.POST:
#             return HttpResponseRedirect(reverse(self.create_form_url))
#         return HttpResponseRedirect(self.success_url)
#
#     def get_form_kwargs(self, *args, **kwargs):
#         kwargs = super(CV2_1_3CreateView, self).get_form_kwargs(*args, **kwargs)
#         kwargs['user'] = self.request.user
#         return kwargs
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["cr_data"] = self.final_criteria_id
#         return context
#
#     def __init__(self, *args, **kwargs):
#         try:
#             self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
#         except:
#             self.final_criteria_id = None
#         super(CV2_1_3CreateView, self).__init__(*args, **kwargs)

class CV2_1_3CreateView(View):
    def get(self, request):
        return render(request, "criteria/table_form_c213.html", self.context)

    def post(self, request):
        try:
            messages.add_message(request, messages.SUCCESS, 'Criterion Added Successfully')
            date = request.POST['date']
            sc_r1 = request.POST['r1']
            st_r1 = request.POST['r2']
            cm_r1 = request.POST['r3']
            ge_r1 = request.POST['r4']
            ph_r1 = request.POST['r5']
            sp_r1 = request.POST['r6']
            mg_r1 = request.POST['r7']
            ot_r1 = request.POST['r8']
            sc_a1 = request.POST['a1']
            st_a1 = request.POST['a2']
            cm_a1 = request.POST['a3']
            ge_a1 = request.POST['a4']
            ph_a1 = request.POST['a5']
            sp_a1 = request.POST['a6']
            mg_a1 = request.POST['a7']
            ot_a1 = request.POST['a8']
            # UN-Aided
            sc_r2 = request.POST['r11']
            st_r2 = request.POST['r12']
            cm_r2 = request.POST['r13']
            ge_r2 = request.POST['r14']
            ph_r2 = request.POST['r15']
            sp_r2 = request.POST['r16']
            mg_r2 = request.POST['r17']
            muslim_r2 = request.POST['r19']
            et_r2 = request.POST['r18']
            lc_r2 = request.POST['r20']
            obx_r2 = request.POST['r21']
            obh_r2 = request.POST['r22']
            ot_r2 = request.POST['r23']
            sc_a2 = request.POST['a11']
            st_a2 = request.POST['a12']
            cm_a2 = request.POST['a13']
            ge_a2 = request.POST['a14']
            ph_a2 = request.POST['a15']
            sp_a2 = request.POST['a16']
            mg_a2 = request.POST['a17']
            muslim_a2 = request.POST['a19']
            et_a2 = request.POST['a18']
            lc_a2 = request.POST['a20']
            obx_a2 = request.POST['a21']
            obh_a2 = request.POST['a22']
            ot_a2 = request.POST['a23']

            text2 = f"""
                    Reserved for SC - {sc_r1}
                    Reserved for ST - {st_r1}
                    Reserved for Community - {cm_r1}
                    Reserved for General - {ge_r1}
                    Reserved for PH - {ph_r1}
                    Reserved for Sports - {sp_r1}
                    Reserved for Management - {mg_r1}
                    Reserved for Others - {ot_r1}
                    """
            text3 = f"""
                    Admitted from SC - {sc_a1}
                    Admitted from ST - {st_a1}
                    Admitted from Community - {cm_a1}
                    Admitted from General - {ge_a1}
                    Admitted from PH - {ph_a1}
                    Admitted from Sports - {sp_a1}
                    Admitted from Management - {mg_a1}
                    Admitted from Others - {ot_a1}
                    """
            text4 = f"""
                   Reserved for SC - {sc_r2}
                   Reserved for ST - {st_r2}
                   Reserved for Community - {cm_r2}
                   Reserved for General - {ge_r2}
                   Reserved for PH - {ph_r2}
                   Reserved for Sports - {sp_r2}
                   Reserved for Management - {mg_r2}
                   Reserved for ET - {et_r2}
                   Reserved for LC - {lc_r2}
                   Reserved for OBX - {obx_r2}
                   Reserved for OBH - {obh_r2}
                   Reserved for Muslim - {muslim_r2}
                   Reserved for Others - {ot_r2}
                   """
            text5 = f"""
                    Admitted from SC - {sc_a2}
                    Admitted from ST - {st_a2}
                    Admitted from Community - {cm_a2}
                    Admitted from General - {ge_a2}
                    Admitted from PH - {ph_a2}
                    Admitted from Sports - {sp_a2}
                    Admitted from Management - {mg_a2}
                    Admitted from ET - {et_a2}
                    Admitted from LC - {lc_a2}
                    Admitted from OBX - {obx_a2}
                    Admitted from OBH - {obh_a2}
                    Admitted from Muslim - {muslim_a2}
                    Admitted from Others - {ot_a2}
                    """
            user_data = request.user
            date_time = datetime.datetime.now()
            obj = CriterionMaster.objects.create(date=date, cr_index="2", criterion="c2_1_3", text2=text2,
                                                 text3=text3, text4=text4, text5=text5, user=user_data)
        except Exception as exp:
            messages.add_message(request, messages.ERROR, 'Something went wrong..!')
            print(exp)
        return render(request, "criteria/table_form_c213.html", self.context)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cr_data = FinalCriteria.objects.get(criteria_id="c2_1_3")
        self.context = {'cr_data': cr_data}


# Update Criteria 2_1_3
class CV2_1_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_1_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_1_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_1_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_1_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_1_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_1_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_1_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_2_1 *  ----------------------------- #
# Create Criteria 2_2_1
class CV2_2_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_2_1CreateForm
    criteria_id = "c2_2_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_2_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_2_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_2_1
class CV2_2_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_2_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_2_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_2_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_2_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_2_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_2_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_2_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_2_2 *  ----------------------------- #
# Create Criteria 2_2_2
class CV2_2_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_2_2CreateForm
    criteria_id = "c2_2_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_2_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_2_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_2_2
class CV2_2_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_2_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_2_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_2_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_2_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_2_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_2_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_2_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_2_3 *  ----------------------------- #
# Create Criteria 2_2_3
class CV2_2_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_2_3CreateForm
    criteria_id = "c2_2_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_2_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_2_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_2_3
class CV2_2_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_2_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_2_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_2_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_2_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_2_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_2_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_2_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_3_1 *  ----------------------------- #
# Create Criteria 2_3_1
class CV2_3_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_3_1CreateForm
    criteria_id = "c2_3_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_3_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_3_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_3_1
class CV2_3_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_3_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_3_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_3_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_3_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_3_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_3_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_3_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_3_2 *  ----------------------------- #
# Create Criteria 2_3_2
class CV2_3_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_3_2CreateForm
    criteria_id = "c2_3_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_3_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_3_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_3_2
class CV2_3_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_3_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_3_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_3_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_3_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_3_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_3_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_3_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_3_3 *  ----------------------------- #
# Create Criteria 2_3_3
class CV2_3_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_3_3CreateForm
    criteria_id = "c2_3_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_3_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_3_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_3_3
class CV2_3_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_3_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_3_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_3_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_3_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_3_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_3_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_3_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_3_4 *  ----------------------------- #
# Create Criteria 2_3_4
class CV2_3_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_3_4CreateForm
    criteria_id = "c2_3_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_3_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_3_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_3_4
class CV2_3_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_3_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_3_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_3_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_3_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_3_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_3_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_3_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_4_1 *  ----------------------------- #
# Create Criteria 2_4_1
class CV2_4_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_4_1CreateForm
    criteria_id = "c2_4_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_4_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_4_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_4_1
class CV2_4_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_4_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_4_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_4_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_4_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_4_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_4_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_4_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_4_2 *  ----------------------------- #
# Create Criteria 2_4_2
class CV2_4_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_4_2CreateForm
    criteria_id = "c2_4_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_4_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_4_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_4_2
class CV2_4_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_4_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_4_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_4_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_4_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_4_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_4_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_4_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_4_3 *  ----------------------------- #
# Create Criteria 2_4_3
class CV2_4_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_4_3CreateForm
    criteria_id = "c2_4_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_4_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_4_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_4_3
class CV2_4_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_4_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_4_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_4_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_4_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_4_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_4_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_4_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_4_4 *  ----------------------------- #
# Create Criteria 2_4_4
class CV2_4_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_4_4CreateForm
    criteria_id = "c2_4_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_4_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_4_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_4_4
class CV2_4_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_4_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_4_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_4_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_4_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_4_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_4_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_4_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_4_5 *  ----------------------------- #
# Create Criteria 2_4_5
class CV2_4_5CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_4_5CreateForm
    criteria_id = "c2_4_5"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_4_5CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_4_5CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_4_5
class CV2_4_5UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_4_5UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_4_5"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_4_5'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_4_5UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_4_5UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_4_5UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_4_5UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_5_1 *  ----------------------------- #
# Create Criteria 2_5_1
class CV2_5_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_5_1CreateForm
    criteria_id = "c2_5_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_5_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_5_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_5_1
class CV2_5_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_5_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_5_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_5_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_5_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_5_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_5_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_5_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_5_2 *  ----------------------------- #
# Create Criteria 2_5_2
class CV2_5_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_5_2CreateForm
    criteria_id = "c2_5_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_5_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_5_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_5_2
class CV2_5_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_5_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_5_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_5_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_5_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_5_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_5_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_5_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_5_3 *  ----------------------------- #
# Create Criteria 2_5_3
class CV2_5_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_5_3CreateForm
    criteria_id = "c2_5_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_5_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_5_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_5_3
class CV2_5_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_5_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_5_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_5_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_5_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_5_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_5_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_5_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_5_4 *  ----------------------------- #
# Create Criteria 2_5_4
class CV2_5_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_5_4CreateForm
    criteria_id = "c2_5_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_5_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_5_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_5_4
class CV2_5_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_5_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_5_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_5_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_5_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_5_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_5_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_5_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_5_5 *  ----------------------------- #
# Create Criteria 2_5_5
class CV2_5_5CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_5_5CreateForm
    criteria_id = "c2_5_5"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_5_5CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_5_5CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_5_5
class CV2_5_5UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_5_5UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_5_5"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_5_5'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_5_5UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_5_5UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_5_5UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_5_5UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_6_1 *  ----------------------------- #
# Create Criteria 2_6_1
class CV2_6_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_6_1CreateForm
    criteria_id = "c2_6_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_6_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_6_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_6_1
class CV2_6_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_6_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_6_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_6_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_6_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_6_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_6_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_6_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_6_2 *  ----------------------------- #
# Create Criteria 2_6_2
class CV2_6_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_6_2CreateForm
    criteria_id = "c2_6_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_6_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_6_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_6_2
class CV2_6_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_6_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_6_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_6_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_6_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_6_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_6_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_6_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_6_3 *  ----------------------------- #
# Create Criteria 2_6_3
class CV2_6_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_6_3CreateForm
    criteria_id = "c2_6_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_6_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_6_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_6_3
class CV2_6_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_6_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_6_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_6_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_6_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_6_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_6_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_6_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  2_7_1 *  ----------------------------- #
# Create Criteria 2_7_1
class CV2_7_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C2_7_1CreateForm
    criteria_id = "c2_7_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_7_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_7_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 2_7_1
class CV2_7_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C2_7_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c2_7_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c2_7_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV2_7_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV2_7_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV2_7_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV2_7_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------* Forms for Criteria 1_1_1 * -------------------------------- #
class C1_1_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_1
        labels = dc1_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_1_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_1_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_1_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_1_1


# Update Form
class C1_1_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_1
        labels = dc1_1_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_1_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_1_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_1_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_1_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1_1_2 * -------------------------------- #
class C1_1_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_2
        labels = dc1_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_1_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_1_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_1_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_1_2


# Update Form
class C1_1_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_2
        labels = dc1_1_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_1_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_1_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_1_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_1_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1_1_3 * -------------------------------- #
class C1_1_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_3
        labels = dc1_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_1_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_1_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_1_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                    initial['final_criteria'] = cid
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_1_3


# Update Form
class C1_1_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_3
        labels = dc1_1_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_1_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_1_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_1_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_1_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1_2_1 * -------------------------------- #
class C1_2_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_2_1
        labels = dc1_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_2_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_2_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_2_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_2_1


# Update Form
class C1_2_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_2_1
        labels = dc1_2_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_2_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_2_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_2_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_2_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1_2_2 * -------------------------------- #
class C1_2_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_2_2
        labels = dc1_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_2_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_2_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_2_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_2_2


# Update Form
class C1_2_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_2_2
        labels = dc1_2_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_2_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_2_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_2_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_2_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1_3_1 * -------------------------------- #
class C1_3_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_1
        labels = dc1_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_3_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_3_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_3_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_3_1


# Update Form
class C1_3_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_1
        labels = dc1_3_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_3_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_3_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_3_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_3_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1_3_2 * -------------------------------- #
class C1_3_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_2
        labels = dc1_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_3_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_3_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_3_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_3_2


# Update Form
class C1_3_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_2
        labels = dc1_3_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_3_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_3_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_3_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_3_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1_3_3 * -------------------------------- #
class C1_3_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_3
        labels = dc1_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_3_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_3_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_3_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_3_3


# Update Form
class C1_3_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_3
        labels = dc1_3_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_3_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_3_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_3_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_3_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1_3_4 * -------------------------------- #
class C1_3_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_4
        labels = dc1_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_3_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_3_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_3_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_3_4


# Update Form
class C1_3_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_4
        labels = dc1_3_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_3_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_3_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_3_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_3_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1_4_1 * -------------------------------- #
class C1_4_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_4_1
        labels = dc1_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_4_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_4_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_4_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_4_1


# Update Form
class C1_4_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_4_1
        labels = dc1_4_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_4_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_4_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_4_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_4_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1_4_2 * -------------------------------- #
class C1_4_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_4_2
        labels = dc1_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_4_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_4_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_4_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_4_2


# Update Form
class C1_4_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_4_2
        labels = dc1_4_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_4_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_4_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_4_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_4_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_1_1 * -------------------------------- #
class C2_1_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_1
        labels = dc2_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_1_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_1_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_1_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_1_1


# Update Form
class C2_1_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_1
        labels = dc2_1_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_1_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_1_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_1_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_1_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_1_2 * -------------------------------- #
class C2_1_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_2
        labels = dc2_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_1_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_1_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_1_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_1_2


# Update Form
class C2_1_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_2
        labels = dc2_1_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_1_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_1_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_1_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_1_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_1_3 * -------------------------------- #
class C2_1_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_3
        labels = dc2_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_1_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_1_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_1_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_1_3


# Update Form
class C2_1_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_3
        labels = dc2_1_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_1_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_1_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_1_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_1_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_2_1 * -------------------------------- #
class C2_2_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_1
        labels = dc2_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_2_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_2_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_2_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_2_1


# Update Form
class C2_2_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_1
        labels = dc2_2_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_2_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_2_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_2_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_2_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_2_2 * -------------------------------- #
class C2_2_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_2
        labels = dc2_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_2_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_2_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_2_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_2_2


# Update Form
class C2_2_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_2
        labels = dc2_2_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_2_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_2_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_2_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_2_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_2_3 * -------------------------------- #
class C2_2_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_3
        labels = dc2_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_2_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_2_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_2_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_2_3


# Update Form
class C2_2_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_3
        labels = dc2_2_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_2_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_2_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_2_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_2_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_3_1 * -------------------------------- #
class C2_3_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_1
        labels = dc2_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_3_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_3_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_3_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_3_1


# Update Form
class C2_3_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_1
        labels = dc2_3_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_3_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_3_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_3_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_3_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_3_2 * -------------------------------- #
class C2_3_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_2
        labels = dc2_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_3_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_3_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_3_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_3_2


# Update Form
class C2_3_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_2
        labels = dc2_3_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_3_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_3_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_3_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_3_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_3_3 * -------------------------------- #
class C2_3_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_3
        labels = dc2_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_3_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_3_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_3_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_3_3


# Update Form
class C2_3_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_3
        labels = dc2_3_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_3_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_3_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_3_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_3_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_3_4 * -------------------------------- #
class C2_3_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_4
        labels = dc2_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_3_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_3_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_3_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_3_4


# Update Form
class C2_3_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_4
        labels = dc2_3_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_3_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_3_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_3_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_3_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_4_1 * -------------------------------- #
class C2_4_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_1
        labels = dc2_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_4_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_4_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_4_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_4_1


# Update Form
class C2_4_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_1
        labels = dc2_4_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_4_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_4_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_4_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_4_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_4_2 * -------------------------------- #
class C2_4_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_2
        labels = dc2_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_4_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_4_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_4_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_4_2


# Update Form
class C2_4_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_2
        labels = dc2_4_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_4_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_4_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_4_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_4_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_4_3 * -------------------------------- #
class C2_4_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_3
        labels = dc2_4_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_4_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_4_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_4_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_4_3


# Update Form
class C2_4_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_3
        labels = dc2_4_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_4_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_4_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_4_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_4_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_4_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_4_4 * -------------------------------- #
class C2_4_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_4
        labels = dc2_4_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_4_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_4_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_4_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_4_4


# Update Form
class C2_4_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_4
        labels = dc2_4_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_4_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_4_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_4_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_4_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_4_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_4_5 * -------------------------------- #
class C2_4_5CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_5
        labels = dc2_4_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_4_5')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_4_5'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_4_5CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_4_5


# Update Form
class C2_4_5UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_5
        labels = dc2_4_5
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_4_5UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_4_5UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_4_5SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_4_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_4_5SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_5_1 * -------------------------------- #
class C2_5_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_1
        labels = dc2_5_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_5_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_5_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_5_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_5_1


# Update Form
class C2_5_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_1
        labels = dc2_5_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_5_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_5_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_5_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_5_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_5_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_5_2 * -------------------------------- #
class C2_5_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_2
        labels = dc2_5_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_5_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_5_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_5_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_5_2


# Update Form
class C2_5_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_2
        labels = dc2_5_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_5_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_5_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_5_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_5_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_5_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_5_3 * -------------------------------- #
class C2_5_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_3
        labels = dc2_5_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_5_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_5_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_5_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_5_3


# Update Form
class C2_5_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_3
        labels = dc2_5_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_5_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_5_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_5_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_5_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_5_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_5_4 * -------------------------------- #
class C2_5_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_4
        labels = dc2_5_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_5_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_5_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_5_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_5_4


# Update Form
class C2_5_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_4
        labels = dc2_5_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_5_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_5_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_5_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_5_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_5_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_5_5 * -------------------------------- #
class C2_5_5CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_5
        labels = dc2_5_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_5_5')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_5_5'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_5_5CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_5_5


# Update Form
class C2_5_5UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_5
        labels = dc2_5_5
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_5_5UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_5_5UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_5_5SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_5_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_5_5SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_6_1 * -------------------------------- #
class C2_6_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_1
        labels = dc2_6_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_6_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_6_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_6_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_6_1


# Update Form
class C2_6_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_1
        labels = dc2_6_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_6_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_6_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_6_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_6_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_6_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_6_2 * -------------------------------- #
class C2_6_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_2
        labels = dc2_6_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_6_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_6_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_6_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_6_2


# Update Form
class C2_6_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_2
        labels = dc2_6_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_6_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_6_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_6_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_6_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_6_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_6_3 * -------------------------------- #
class C2_6_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_3
        labels = dc2_6_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_6_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_6_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_6_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_6_3


# Update Form
class C2_6_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_3
        labels = dc2_6_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_6_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_6_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_6_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_6_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_6_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_7_1 * -------------------------------- #
class C2_7_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_7_1
        labels = dc2_7_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_7_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_7_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_7_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_7_1


# Update Form
class C2_7_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_7_1
        labels = dc2_7_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_7_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_7_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_7_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_7_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_7_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------- * Data Add and Edit Logic for  3_1_1 *  ----------------------------- #
# Create Criteria 3_1_1
class CV3_1_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_1_1CreateForm
    criteria_id = "c3_1_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_1_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_1_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_1_1
class CV3_1_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_1_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_1_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_1_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_1_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_1_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_1_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_1_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_1_2 *  ----------------------------- #
# Create Criteria 3_1_2
class CV3_1_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_1_2CreateForm
    criteria_id = "c3_1_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_1_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_1_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_1_2
class CV3_1_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_1_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_1_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_1_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_1_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_1_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_1_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_1_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_1_3 *  ----------------------------- #
# Create Criteria 3_1_3
class CV3_1_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_1_3CreateForm
    criteria_id = "c3_1_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_1_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_1_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_1_3
class CV3_1_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_1_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_1_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_1_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_1_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_1_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_1_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_1_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_1_4 *  ----------------------------- #
# Create Criteria 3_1_4
class CV3_1_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_1_4CreateForm
    criteria_id = "c3_1_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_1_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_1_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_1_4
class CV3_1_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_1_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_1_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_1_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_1_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_1_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_1_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_1_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_2_1 *  ----------------------------- #
# Create Criteria 3_2_1
class CV3_2_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_2_1CreateForm
    criteria_id = "c3_2_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_2_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_2_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_2_1
class CV3_2_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_2_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_2_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_2_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_2_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_2_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_2_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_2_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_2_2 *  ----------------------------- #
# Create Criteria 3_2_2
class CV3_2_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_2_2CreateForm
    criteria_id = "c3_2_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_2_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_2_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_2_2
class CV3_2_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_2_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_2_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_2_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_2_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_2_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_2_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_2_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_2_3 *  ----------------------------- #
# Create Criteria 3_2_3
class CV3_2_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_2_3CreateForm
    criteria_id = "c3_2_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_2_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_2_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_2_3
class CV3_2_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_2_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_2_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_2_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_2_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_2_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_2_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_2_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_2_4 *  ----------------------------- #
# Create Criteria 3_2_4
class CV3_2_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_2_4CreateForm
    criteria_id = "c3_2_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_2_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_2_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_2_4
class CV3_2_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_2_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_2_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_2_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_2_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_2_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_2_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_2_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_3_1 *  ----------------------------- #
# Create Criteria 3_3_1
class CV3_3_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_3_1CreateForm
    criteria_id = "c3_3_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_3_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_3_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_3_1
class CV3_3_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_3_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_3_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_3_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_3_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_3_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_3_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_3_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_3_2 *  ----------------------------- #
# Create Criteria 3_3_2
class CV3_3_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_3_2CreateForm
    criteria_id = "c3_3_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_3_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_3_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_3_2
class CV3_3_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_3_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_3_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_3_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_3_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_3_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_3_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_3_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_3_3 *  ----------------------------- #
# Create Criteria 3_3_3
class CV3_3_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_3_3CreateForm
    criteria_id = "c3_3_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_3_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_3_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_3_3
class CV3_3_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_3_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_3_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_3_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_3_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_3_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_3_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_3_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_4_1 *  ----------------------------- #
# Create Criteria 3_4_1
class CV3_4_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_4_1CreateForm
    criteria_id = "c3_4_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_4_1
class CV3_4_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_4_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_4_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_4_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_4_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_4_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_4_2 *  ----------------------------- #
# Create Criteria 3_4_2
class CV3_4_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_4_2CreateForm
    criteria_id = "c3_4_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_4_2
class CV3_4_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_4_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_4_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_4_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_4_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_4_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_4_3 *  ----------------------------- #
# Create Criteria 3_4_3
class CV3_4_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_4_3CreateForm
    criteria_id = "c3_4_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_4_3
class CV3_4_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_4_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_4_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_4_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_4_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_4_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_4_4 *  ----------------------------- #
# Create Criteria 3_4_4
class CV3_4_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_4_4CreateForm
    criteria_id = "c3_4_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_4_4
class CV3_4_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_4_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_4_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_4_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_4_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_4_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_4_5 *  ----------------------------- #
# Create Criteria 3_4_5
class CV3_4_5CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_4_5CreateForm
    criteria_id = "c3_4_5"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_5CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_5CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_4_5
class CV3_4_5UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_4_5UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_4_5"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_4_5'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_4_5UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_4_5UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_5UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_5UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_4_6 *  ----------------------------- #
# Create Criteria 3_4_6
class CV3_4_6CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_4_6CreateForm
    criteria_id = "c3_4_6"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_6CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_6CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_4_6
class CV3_4_6UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_4_6UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_4_6"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_4_6'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_4_6UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_4_6UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_6UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_6UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_4_7 *  ----------------------------- #
# Create Criteria 3_4_7
class CV3_4_7CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_4_7CreateForm
    criteria_id = "c3_4_7"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_7CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_7CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_4_7
class CV3_4_7UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_4_7UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_4_7"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_4_7'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_4_7UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_4_7UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_7UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_7UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_4_8 *  ----------------------------- #
# Create Criteria 3_4_8
class CV3_4_8CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_4_8CreateForm
    criteria_id = "c3_4_8"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_8CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_8CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_4_8
class CV3_4_8UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_4_8UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_4_8"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_4_8'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_4_8UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_4_8UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_4_8UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_4_8UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_5_1 *  ----------------------------- #
# Create Criteria 3_5_1
class CV3_5_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_5_1CreateForm
    criteria_id = "c3_5_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_5_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_5_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_5_1
class CV3_5_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_5_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_5_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_5_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_5_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_5_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_5_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_5_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_5_2 *  ----------------------------- #
# Create Criteria 3_5_2
class CV3_5_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_5_2CreateForm
    criteria_id = "c3_5_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_5_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_5_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_5_2
class CV3_5_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_5_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_5_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_5_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_5_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_5_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_5_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_5_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_5_3 *  ----------------------------- #
# Create Criteria 3_5_3
class CV3_5_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_5_3CreateForm
    criteria_id = "c3_5_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_5_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_5_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_5_3
class CV3_5_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_5_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_5_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_5_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_5_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_5_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_5_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_5_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_6_1 *  ----------------------------- #
# Create Criteria 3_6_1
class CV3_6_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_6_1CreateForm
    criteria_id = "c3_6_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_6_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_6_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_6_1
class CV3_6_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_6_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_6_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_6_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_6_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_6_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_6_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_6_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_6_2 *  ----------------------------- #
# Create Criteria 3_6_2
class CV3_6_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_6_2CreateForm
    criteria_id = "c3_6_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_6_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_6_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_6_2
class CV3_6_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_6_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_6_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_6_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_6_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_6_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_6_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_6_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_6_3 *  ----------------------------- #
# Create Criteria 3_6_3
class CV3_6_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_6_3CreateForm
    criteria_id = "c3_6_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_6_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_6_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_6_3
class CV3_6_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_6_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_6_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_6_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_6_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_6_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_6_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_6_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_6_4 *  ----------------------------- #
# Create Criteria 3_6_4
class CV3_6_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_6_4CreateForm
    criteria_id = "c3_6_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_6_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_6_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_6_4
class CV3_6_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_6_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_6_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_6_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_6_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_6_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_6_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_6_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_7_1 *  ----------------------------- #
# Create Criteria 3_7_1
class CV3_7_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_7_1CreateForm
    criteria_id = "c3_7_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_7_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_7_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_7_1
class CV3_7_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_7_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_7_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_7_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_7_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_7_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_7_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_7_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_7_2 *  ----------------------------- #
# Create Criteria 3_7_2
class CV3_7_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_7_2CreateForm
    criteria_id = "c3_7_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_7_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_7_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_7_2
class CV3_7_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_7_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_7_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_7_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_7_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_7_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_7_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_7_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  3_7_3 *  ----------------------------- #
# Create Criteria 3_7_3
class CV3_7_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C3_7_3CreateForm
    criteria_id = "c3_7_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_7_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_7_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 3_7_3
class CV3_7_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C3_7_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c3_7_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c3_7_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV3_7_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV3_7_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV3_7_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV3_7_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_1_1 *  ----------------------------- #
# Create Criteria 4_1_1
class CV4_1_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_1_1CreateForm
    criteria_id = "c4_1_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_1_1
class CV4_1_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_1_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_1_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_1_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_1_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_1_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_1_2A *  ----------------------------- #
# Create Criteria 4_1_2A
class CV4_1_2ACreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_1_2ACreateForm
    criteria_id = "c4_1_2A"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_2ACreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_2ACreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_1_2A
class CV4_1_2AUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_1_2AUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_1_2A"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_1_2A'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_1_2AUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_1_2AUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_2AUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_2AUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_1_2B *  ----------------------------- #
# Create Criteria 4_1_2B
class CV4_1_2BCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_1_2BCreateForm
    criteria_id = "c4_1_2B"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_2BCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_2BCreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_1_2B
class CV4_1_2BUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_1_2BUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_1_2B"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_1_2B'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_1_2BUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_1_2BUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_2BUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_2BUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_1_2C *  ----------------------------- #
# Create Criteria 4_1_2C
class CV4_1_2CCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_1_2CCreateForm
    criteria_id = "c4_1_2C"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_2CCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_2CCreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_1_2C
class CV4_1_2CUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_1_2CUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_1_2C"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_1_2C'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_1_2CUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_1_2CUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_2CUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_2CUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_1_2D *  ----------------------------- #
# Create Criteria 4_1_2D
class CV4_1_2DCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_1_2DCreateForm
    criteria_id = "c4_1_2D"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_2DCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_2DCreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_1_2D
class CV4_1_2DUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_1_2DUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_1_2D"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_1_2D'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_1_2DUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_1_2DUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_2DUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_2DUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_1_2E *  ----------------------------- #
# Create Criteria 4_1_2E
class CV4_1_2ECreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_1_2ECreateForm
    criteria_id = "c4_1_2E"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_2ECreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_2ECreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_1_2E
class CV4_1_2EUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_1_2EUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_1_2E"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_1_2E'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_1_2EUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_1_2EUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_2EUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_2EUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_1_3 *  ----------------------------- #
# Create Criteria 4_1_3
class CV4_1_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_1_3CreateForm
    criteria_id = "c4_1_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_1_3
class CV4_1_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_1_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_1_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_1_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_1_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_1_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_1_4 *  ----------------------------- #
# Create Criteria 4_1_4
class CV4_1_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_1_4CreateForm
    criteria_id = "c4_1_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_1_4
class CV4_1_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_1_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_1_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_1_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_1_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_1_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_1_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_1_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_2_1 *  ----------------------------- #
# Create Criteria 4_2_1
class CV4_2_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_2_1CreateForm
    criteria_id = "c4_2_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_2_1
class CV4_2_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_2_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_2_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_2_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_2_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_2_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_2_2 *  ----------------------------- #
# Create Criteria 4_2_2
class CV4_2_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_2_2CreateForm
    criteria_id = "c4_2_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_2_2
class CV4_2_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_2_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_2_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_2_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_2_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_2_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_2_3 *  ----------------------------- #
# Create Criteria 4_2_3
class CV4_2_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_2_3CreateForm
    criteria_id = "c4_2_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_2_3
class CV4_2_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_2_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_2_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_2_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_2_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_2_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_2_4 *  ----------------------------- #
# Create Criteria 4_2_4
class CV4_2_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_2_4CreateForm
    criteria_id = "c4_2_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_2_4
class CV4_2_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_2_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_2_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_2_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_2_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_2_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_2_5 *  ----------------------------- #
# Create Criteria 4_2_5
class CV4_2_5CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_2_5CreateForm
    criteria_id = "c4_2_5"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_5CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_5CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_2_5
class CV4_2_5UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_2_5UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_2_5"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_2_5'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_2_5UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_2_5UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_5UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_5UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_2_6 *  ----------------------------- #
# Create Criteria 4_2_6
class CV4_2_6CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_2_6CreateForm
    criteria_id = "c4_2_6"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_6CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_6CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_2_6
class CV4_2_6UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_2_6UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_2_6"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_2_6'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_2_6UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_2_6UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_2_6UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_2_6UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_3_1 *  ----------------------------- #
# Create Criteria 4_3_1
class CV4_3_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_3_1CreateForm
    criteria_id = "c4_3_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_3_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_3_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_3_1
class CV4_3_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_3_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_3_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_3_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_3_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_3_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_3_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_3_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_3_2 *  ----------------------------- #
# Create Criteria 4_3_2
class CV4_3_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_3_2CreateForm
    criteria_id = "c4_3_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_3_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_3_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_3_2
class CV4_3_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_3_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_3_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_3_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_3_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_3_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_3_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_3_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_3_3 *  ----------------------------- #
# Create Criteria 4_3_3
class CV4_3_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_3_3CreateForm
    criteria_id = "c4_3_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_3_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_3_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_3_3
class CV4_3_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_3_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_3_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_3_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_3_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_3_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_3_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_3_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_3_4 *  ----------------------------- #
# Create Criteria 4_3_4
class CV4_3_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_3_4CreateForm
    criteria_id = "c4_3_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_3_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_3_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_3_4
class CV4_3_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_3_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_3_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_3_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_3_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_3_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_3_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_3_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_4_1 *  ----------------------------- #
# Create Criteria 4_4_1
class CV4_4_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_4_1CreateForm
    criteria_id = "c4_4_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_4_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_4_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_4_1
class CV4_4_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_4_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_4_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_4_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_4_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_4_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_4_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_4_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  4_4_2 *  ----------------------------- #
# Create Criteria 4_4_2
class CV4_4_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C4_4_2CreateForm
    criteria_id = "c4_4_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_4_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_4_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 4_4_2
class CV4_4_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C4_4_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c4_4_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c4_4_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV4_4_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV4_4_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV4_4_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV4_4_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_1 *  ----------------------------- #
# Create Criteria 5_1_1
class CV5_1_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_1CreateForm
    criteria_id = "c5_1_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_1
class CV5_1_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_2 *  ----------------------------- #
# Create Criteria 5_1_2
class CV5_1_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_2CreateForm
    criteria_id = "c5_1_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_2
class CV5_1_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_3A *  ----------------------------- #
# Create Criteria 5_1_3A
class CV5_1_3ACreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_3ACreateForm
    criteria_id = "c5_1_3A"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3ACreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3ACreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_3A
class CV5_1_3AUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_3AUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_3A"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_3A'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_3AUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_3AUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3AUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3AUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_3B *  ----------------------------- #
# Create Criteria 5_1_3B
class CV5_1_3BCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_3BCreateForm
    criteria_id = "c5_1_3B"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3BCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3BCreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_3B
class CV5_1_3BUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_3BUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_3B"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_3B'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_3BUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_3BUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3BUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3BUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_3C *  ----------------------------- #
# Create Criteria 5_1_3C
class CV5_1_3CCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_3CCreateForm
    criteria_id = "c5_1_3C"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3CCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3CCreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_3C
class CV5_1_3CUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_3CUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_3C"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_3C'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_3CUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_3CUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3CUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3CUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_3D *  ----------------------------- #
# Create Criteria 5_1_3D
class CV5_1_3DCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_3DCreateForm
    criteria_id = "c5_1_3D"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3DCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3DCreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_3D
class CV5_1_3DUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_3DUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_3D"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_3D'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_3DUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_3DUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3DUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3DUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_3E *  ----------------------------- #
# Create Criteria 5_1_3E
class CV5_1_3ECreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_3ECreateForm
    criteria_id = "c5_1_3E"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3ECreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3ECreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_3E
class CV5_1_3EUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_3EUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_3E"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_3E'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_3EUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_3EUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3EUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3EUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_3F *  ----------------------------- #
# Create Criteria 5_1_3F
class CV5_1_3FCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_3FCreateForm
    criteria_id = "c5_1_3F"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3FCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3FCreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_3F
class CV5_1_3FUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_3FUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_3F"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_3F'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_3FUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_3FUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3FUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3FUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_3G *  ----------------------------- #
# Create Criteria 5_1_3G
class CV5_1_3GCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_3GCreateForm
    criteria_id = "c5_1_3G"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3GCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3GCreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_3G
class CV5_1_3GUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_3GUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_3G"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_3G'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_3GUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_3GUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3GUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3GUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_3H *  ----------------------------- #
# Create Criteria 5_1_3H
class CV5_1_3HCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_3HCreateForm
    criteria_id = "c5_1_3H"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3HCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3HCreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_3H
class CV5_1_3HUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_3HUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_3H"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_3H'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_3HUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_3HUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_3HUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_3HUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_4 *  ----------------------------- #
# Create Criteria 5_1_4
class CV5_1_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_4CreateForm
    criteria_id = "c5_1_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_4
class CV5_1_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_5 *  ----------------------------- #
# Create Criteria 5_1_5
class CV5_1_5CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_5CreateForm
    criteria_id = "c5_1_5"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_5CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_5CreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_5
class CV5_1_5UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_5UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_5"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_5'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_5UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_5UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_5UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_5UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_1_6 *  ----------------------------- #
# Create Criteria 5_1_6
class CV5_1_6CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_1_6CreateForm
    criteria_id = "c5_1_6"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_6CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_6CreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_1_6
class CV5_1_6UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_1_6UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_1_6"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_1_6'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_1_6UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_1_6UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_1_6UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_1_6UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_2_1 *  ----------------------------- #
# Create Criteria 5_2_1
class CV5_2_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_2_1CreateForm
    criteria_id = "c5_2_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_2_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_2_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_2_1
class CV5_2_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_2_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_2_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_2_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_2_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_2_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_2_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_2_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_2_2 *  ----------------------------- #
# Create Criteria 5_2_2
class CV5_2_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_2_2CreateForm
    criteria_id = "c5_2_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_2_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_2_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_2_2
class CV5_2_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_2_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_2_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_2_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_2_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_2_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_2_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_2_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_2_3 *  ----------------------------- #
# Create Criteria 5_2_3
class CV5_2_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_2_3CreateForm
    criteria_id = "c5_2_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_2_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_2_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_2_3
class CV5_2_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_2_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_2_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_2_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_2_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_2_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_2_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_2_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_3_1 *  ----------------------------- #
# Create Criteria 5_3_1
class CV5_3_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_3_1CreateForm
    criteria_id = "c5_3_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_3_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_3_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_3_1
class CV5_3_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_3_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_3_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_3_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_3_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_3_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_3_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_3_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_3_2A *  ----------------------------- #
# Create Criteria 5_3_2A
class CV5_3_2ACreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_3_2ACreateForm
    criteria_id = "c5_3_2A"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_3_2ACreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_3_2ACreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_3_2A
class CV5_3_2AUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_3_2AUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_3_2A"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_3_2A'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_3_2AUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_3_2AUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_3_2AUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_3_2AUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_3_2B *  ----------------------------- #
# Create Criteria 5_3_2B
class CV5_3_2BCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_3_2BCreateForm
    criteria_id = "c5_3_2B"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_3_2BCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_3_2BCreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_3_2B
class CV5_3_2BUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_3_2BUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_3_2B"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_3_2B'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_3_2BUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_3_2BUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_3_2BUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_3_2BUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_3_3 *  ----------------------------- #
# Create Criteria 5_3_3
class CV5_3_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_3_3CreateForm
    criteria_id = "c5_3_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_3_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_3_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_3_3
class CV5_3_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_3_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_3_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_3_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_3_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_3_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_3_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_3_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_4_1A *  ----------------------------- #
# Create Criteria 5_4_1A
class CV5_4_1ACreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_4_1ACreateForm
    criteria_id = "c5_4_1A"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_4_1ACreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_4_1ACreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_4_1A
class CV5_4_1AUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_4_1AUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_4_1A"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_4_1A'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_4_1AUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_4_1AUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_4_1AUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_4_1AUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_4_1B *  ----------------------------- #
# Create Criteria 5_4_1B
class CV5_4_1BCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_4_1BCreateForm
    criteria_id = "c5_4_1B"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_4_1BCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_4_1BCreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_4_1B
class CV5_4_1BUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_4_1BUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_4_1B"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_4_1B'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_4_1BUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_4_1BUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_4_1BUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_4_1BUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  5_4_2 *  ----------------------------- #
# Create Criteria 5_4_2
class CV5_4_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C5_4_2CreateForm
    criteria_id = "c5_4_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_4_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_4_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 5_4_2
class CV5_4_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C5_4_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c5_4_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c5_4_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV5_4_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV5_4_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV5_4_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV5_4_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_1_1 *  ----------------------------- #
# Create Criteria 6_1_1
class CV6_1_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_1_1CreateForm
    criteria_id = "c6_1_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_1_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_1_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_1_1
class CV6_1_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_1_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_1_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_1_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_1_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_1_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_1_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_1_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_1_2 *  ----------------------------- #
# Create Criteria 6_1_2
class CV6_1_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_1_2CreateForm
    criteria_id = "c6_1_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_1_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_1_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_1_2
class CV6_1_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_1_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_1_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_1_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_1_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_1_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_1_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_1_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_2_1 *  ----------------------------- #
# Create Criteria 6_2_1
class CV6_2_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_2_1CreateForm
    criteria_id = "c6_2_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_2_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_2_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_2_1
class CV6_2_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_2_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_2_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_2_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_2_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_2_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_2_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_2_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_2_2 *  ----------------------------- #
# Create Criteria 6_2_2
class CV6_2_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_2_2CreateForm
    criteria_id = "c6_2_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_2_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_2_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_2_2
class CV6_2_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_2_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_2_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_2_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_2_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_2_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_2_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_2_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_2_3 *  ----------------------------- #
# Create Criteria 6_2_3
class CV6_2_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_2_3CreateForm
    criteria_id = "c6_2_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_2_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_2_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_2_3
class CV6_2_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_2_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_2_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_2_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_2_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_2_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_2_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_2_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_2_4 *  ----------------------------- #
# Create Criteria 6_2_4
class CV6_2_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_2_4CreateForm
    criteria_id = "c6_2_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_2_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_2_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_2_4
class CV6_2_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_2_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_2_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_2_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_2_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_2_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_2_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_2_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_3_1 *  ----------------------------- #
# Create Criteria 6_3_1
class CV6_3_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_3_1CreateForm
    criteria_id = "c6_3_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_3_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_3_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_3_1
class CV6_3_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_3_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_3_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_3_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_3_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_3_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_3_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_3_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_3_2 *  ----------------------------- #
# Create Criteria 6_3_2
class CV6_3_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_3_2CreateForm
    criteria_id = "c6_3_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_3_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_3_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_3_2
class CV6_3_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_3_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_3_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_3_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_3_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_3_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_3_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_3_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_3_3 *  ----------------------------- #
# Create Criteria 6_3_3
class CV6_3_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_3_3CreateForm
    criteria_id = "c6_3_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_3_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_3_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_3_3
class CV6_3_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_3_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_3_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_3_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_3_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_3_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_3_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_3_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_3_4 *  ----------------------------- #
# Create Criteria 6_3_4
class CV6_3_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_3_4CreateForm
    criteria_id = "c6_3_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_3_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_3_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_3_4
class CV6_3_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_3_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_3_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_3_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_3_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_3_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_3_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_3_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_3_5 *  ----------------------------- #
# Create Criteria 6_3_5
class CV6_3_5CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_3_5CreateForm
    criteria_id = "c6_3_5"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_3_5CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_3_5CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_3_5
class CV6_3_5UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_3_5UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_3_5"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_3_5'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_3_5UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_3_5UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_3_5UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_3_5UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_4_1 *  ----------------------------- #
# Create Criteria 6_4_1
class CV6_4_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_4_1CreateForm
    criteria_id = "c6_4_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_4_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_4_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_4_1
class CV6_4_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_4_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_4_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_4_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_4_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_4_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_4_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_4_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_4_2 *  ----------------------------- #
# Create Criteria 6_4_2
class CV6_4_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_4_2CreateForm
    criteria_id = "c6_4_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_4_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_4_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_4_2
class CV6_4_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_4_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_4_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_4_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_4_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_4_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_4_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_4_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_4_3 *  ----------------------------- #
# Create Criteria 6_4_3
class CV6_4_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_4_3CreateForm
    criteria_id = "c6_4_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_4_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_4_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_4_3
class CV6_4_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_4_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_4_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_4_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_4_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_4_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_4_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_4_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_5_1 *  ----------------------------- #
# Create Criteria 6_5_1
class CV6_5_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_5_1CreateForm
    criteria_id = "c6_5_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_5_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_5_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_5_1
class CV6_5_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_5_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_5_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_5_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_5_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_5_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_5_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_5_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_5_2 *  ----------------------------- #
# Create Criteria 6_5_2
class CV6_5_2CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_5_2CreateForm
    criteria_id = "c6_5_2"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_5_2CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_5_2CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_5_2
class CV6_5_2UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_5_2UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_5_2"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_5_2'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_5_2UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_5_2UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_5_2UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_5_2UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_5_3 *  ----------------------------- #
# Create Criteria 6_5_3
class CV6_5_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_5_3CreateForm
    criteria_id = "c6_5_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_5_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_5_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_5_3
class CV6_5_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_5_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_5_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_5_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_5_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_5_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_5_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_5_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_5_4 *  ----------------------------- #
# Create Criteria 6_5_4
class CV6_5_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_5_4CreateForm
    criteria_id = "c6_5_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_5_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_5_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_5_4
class CV6_5_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_5_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_5_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_5_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_5_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_5_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_5_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_5_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  6_5_5 *  ----------------------------- #
# Create Criteria 6_5_5
class CV6_5_5CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C6_5_5CreateForm
    criteria_id = "c6_5_5"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_5_5CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_5_5CreateView, self).__init__(*args, **kwargs)


# Update Criteria 6_5_5
class CV6_5_5UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C6_5_5UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c6_5_5"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c6_5_5'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV6_5_5UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV6_5_5UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV6_5_5UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV6_5_5UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_1 *  ----------------------------- #
# Create Criteria 7_1_1
class CV7_1_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_1CreateForm
    criteria_id = "c7_1_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_1
class CV7_1_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_2A *  ----------------------------- #
# Create Criteria 7_1_2A
class CV7_1_2ACreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_2ACreateForm
    criteria_id = "c7_1_2A"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_2ACreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_2ACreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_2A
class CV7_1_2AUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_2AUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_2A"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_2A'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_2AUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_2AUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_2AUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_2AUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_2B *  ----------------------------- #
# Create Criteria 7_1_2B
class CV7_1_2BCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_2BCreateForm
    criteria_id = "c7_1_2B"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_2BCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_2BCreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_2B
class CV7_1_2BUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_2BUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_2B"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_2B'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_2BUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_2BUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_2BUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_2BUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_2C *  ----------------------------- #
# Create Criteria 7_1_2C
class CV7_1_2CCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_2CCreateForm
    criteria_id = "c7_1_2C"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_2CCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_2CCreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_2C
class CV7_1_2CUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_2CUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_2C"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_2C'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_2CUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_2CUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_2CUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_2CUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_3 *  ----------------------------- #
# Create Criteria 7_1_3
class CV7_1_3CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_3CreateForm
    criteria_id = "c7_1_3"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_3CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_3CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_3
class CV7_1_3UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_3UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_3"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_3'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_3UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_3UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_3UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_3UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_4 *  ----------------------------- #
# Create Criteria 7_1_4
class CV7_1_4CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_4CreateForm
    criteria_id = "c7_1_4"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_4CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_4CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_4
class CV7_1_4UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_4UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_4"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_4'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_4UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_4UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_4UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_4UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_5 *  ----------------------------- #
# Create Criteria 7_1_5
class CV7_1_5CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_5CreateForm
    criteria_id = "c7_1_5"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_5CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_5CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_5
class CV7_1_5UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_5UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_5"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_5'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_5UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_5UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_5UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_5UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_6 *  ----------------------------- #
# Create Criteria 7_1_6
class CV7_1_6CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_6CreateForm
    criteria_id = "c7_1_6"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_6CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_6CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_6
class CV7_1_6UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_6UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_6"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_6'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_6UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_6UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_6UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_6UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_7A *  ----------------------------- #
# Create Criteria 7_1_7A
class CV7_1_7ACreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_7ACreateForm
    criteria_id = "c7_1_7A"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_7ACreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_7ACreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_7A
class CV7_1_7AUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_7AUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_7A"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_7A'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_7AUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_7AUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_7AUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_7AUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_7B *  ----------------------------- #
# Create Criteria 7_1_7B
class CV7_1_7BCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_7BCreateForm
    criteria_id = "c7_1_7B"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_7BCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_7BCreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_7B
class CV7_1_7BUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_7BUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_7B"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_7B'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_7BUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_7BUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_7BUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_7BUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_7C *  ----------------------------- #
# Create Criteria 7_1_7C
class CV7_1_7CCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_7CCreateForm
    criteria_id = "c7_1_7C"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_7CCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_7CCreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_7C
class CV7_1_7CUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_7CUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_7C"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_7C'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_7CUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_7CUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_7CUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_7CUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_7D *  ----------------------------- #
# Create Criteria 7_1_7D
class CV7_1_7DCreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_7DCreateForm
    criteria_id = "c7_1_7D"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_7DCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_7DCreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_7D
class CV7_1_7DUpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_7DUpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_7D"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_7D'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_7DUpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_7DUpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_7DUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_7DUpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_8 *  ----------------------------- #
# Create Criteria 7_1_8
class CV7_1_8CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_8CreateForm
    criteria_id = "c7_1_8"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_8CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_8CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_8
class CV7_1_8UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_8UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_8"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_8'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_8UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_8UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_8UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_8UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_9 *  ----------------------------- #
# Create Criteria 7_1_9
class CV7_1_9CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_9CreateForm
    criteria_id = "c7_1_9"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_9CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_9CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_9
class CV7_1_9UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_9UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_9"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_9'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_9UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_9UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_9UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_9UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_10 *  ----------------------------- #
# Create Criteria 7_1_10
class CV7_1_10CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_10CreateForm
    criteria_id = "c7_1_10"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_10CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_10CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_10
class CV7_1_10UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_10UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_10"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_10'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_10UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_10UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_10UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_10UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_11 *  ----------------------------- #
# Create Criteria 7_1_11
class CV7_1_11CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_11CreateForm
    criteria_id = "c7_1_11"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_11CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_11CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_11
class CV7_1_11UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_11UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_11"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_11'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_11UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_11UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_11UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_11UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_12 *  ----------------------------- #
# Create Criteria 7_1_12
class CV7_1_12CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_12CreateForm
    criteria_id = "c7_1_12"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_12CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_12CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_12
class CV7_1_12UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_12UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_12"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_12'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_12UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_12UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_12UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_12UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_13 *  ----------------------------- #
# Create Criteria 7_1_13
class CV7_1_13CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_13CreateForm
    criteria_id = "c7_1_13"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_13CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_13CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_13
class CV7_1_13UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_13UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_13"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_13'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_13UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_13UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_13UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_13UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_14 *  ----------------------------- #
# Create Criteria 7_1_14
class CV7_1_14CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_14CreateForm
    criteria_id = "c7_1_14"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_14CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_14CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_14
class CV7_1_14UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_14UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_14"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_14'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_14UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_14UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_14UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_14UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_15 *  ----------------------------- #
# Create Criteria 7_1_15
class CV7_1_15CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_15CreateForm
    criteria_id = "c7_1_15"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_15CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_15CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_15
class CV7_1_15UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_15UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_15"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_15'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_15UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_15UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_15UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_15UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_16 *  ----------------------------- #
# Create Criteria 7_1_16
class CV7_1_16CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_16CreateForm
    criteria_id = "c7_1_16"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_16CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_16CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_16
class CV7_1_16UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_16UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_16"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_16'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_16UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_16UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_16UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_16UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_17 *  ----------------------------- #
# Create Criteria 7_1_17
class CV7_1_17CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_17CreateForm
    criteria_id = "c7_1_17"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_17CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_17CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_17
class CV7_1_17UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_17UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_17"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_17'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_17UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_17UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_17UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_17UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_18 *  ----------------------------- #
# Create Criteria 7_1_18
class CV7_1_18CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_18CreateForm
    criteria_id = "c7_1_18"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_18CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_18CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_18
class CV7_1_18UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_18UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_18"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_18'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_18UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_18UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_18UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_18UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_1_19 *  ----------------------------- #
# Create Criteria 7_1_19
class CV7_1_19CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_1_19CreateForm
    criteria_id = "c7_1_19"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_19CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_19CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_1_19
class CV7_1_19UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_1_19UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_1_19"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_1_19'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_1_19UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_1_19UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_1_19UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_1_19UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_2_1 *  ----------------------------- #
# Create Criteria 7_2_1
class CV7_2_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_2_1CreateForm
    criteria_id = "c7_2_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_2_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_2_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_2_1
class CV7_2_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_2_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_2_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_2_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_2_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_2_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_2_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_2_1UpdateView, self).__init__(*args, **kwargs)


# ------------------------- * Data Add and Edit Logic for  7_3_1 *  ----------------------------- #
# Create Criteria 7_3_1
class CV7_3_1CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C7_3_1CreateForm
    criteria_id = "c7_3_1"
    create_form_url = 'criterions:c' + criteria_id
    success_url = '/criteria/show/' + criteria_id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.criterion = self.criteria_id
        self.object.cr_index = self.criteria_id[1]
        try:
            self.object.final_criteria = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            pass
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        if "add-next" in self.request.POST:
            return HttpResponseRedirect(reverse(self.create_form_url))
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_3_1CreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_3_1CreateView, self).__init__(*args, **kwargs)


# Update Criteria 7_3_1
class CV7_3_1UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C7_3_1UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c7_3_1"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{}#criterions'.format(reverse('criterions:show-criteria', kwargs={'slug': 'c7_3_1'}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV7_3_1UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV7_3_1UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV7_3_1UpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cr_data"] = self.final_criteria_id
        context["obj_id"] = self.object.id
        return context

    def __init__(self, *args, **kwargs):
        try:
            self.final_criteria_id = FinalCriteria.objects.get(criteria_id=self.criteria_id)
        except:
            self.final_criteria_id = None
        super(CV7_3_1UpdateView, self).__init__(*args, **kwargs)
