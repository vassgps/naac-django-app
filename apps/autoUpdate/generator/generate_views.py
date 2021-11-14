cr_now = ["3_1_1", "3_1_2", "3_1_3", "3_1_4", "3_2_1", "3_2_2",
          "3_2_3", "3_2_4", "3_3_1", "3_3_2", "3_3_3", "3_4_1", "3_4_2", "3_4_3", "3_4_4", "3_4_5",
          "3_4_6", "3_4_7", "3_4_8", "3_5_1", "3_5_2", "3_5_3", "3_6_1", "3_6_2", "3_6_3", "3_6_4",
          "3_7_1", "3_7_2", "3_7_3", "4_1_1", "4_1_2A", "4_1_2B", "4_1_2C", "4_1_2D",
          "4_1_2E",
          "4_1_3", "4_1_4", "4_2_1", "4_2_2", "4_2_3", "4_2_4", "4_2_5", "4_2_6", "4_3_1", "4_3_2",
          "4_3_3", "4_3_4", "4_4_1", "4_4_2", "5_1_1", "5_1_2",  "5_1_3A", "5_1_3B", "5_1_3C",
          "5_1_3D", "5_1_3E", "5_1_3F", "5_1_3G", "5_1_3H", "5_1_4", "5_1_5", "5_1_6", "5_2_1",
          "5_2_2",
          "5_2_3", "5_3_1", "5_3_2A", "5_3_2B", "5_3_3", "5_4_1A", "5_4_1B", "5_4_2", "6_1_1",
          "6_1_2", "6_2_1", "6_2_2", "6_2_3", "6_2_4", "6_3_1", "6_3_2", "6_3_3", "6_3_4", "6_3_5",
          "6_4_1", "6_4_2", "6_4_3", "6_5_1", "6_5_2", "6_5_3", "6_5_4", "6_5_5", "7_1_1",
          "7_1_2A", "7_1_2B", "7_1_2C", "7_1_3", "7_1_4", "7_1_5", "7_1_6", "7_1_7A", "7_1_7B",
          "7_1_7C",
          "7_1_7D", "7_1_8", "7_1_9", "7_1_10", "7_1_11", "7_1_12", "7_1_13", "7_1_14", "7_1_15",
          "7_1_16", "7_1_17", "7_1_18", "7_1_19", "7_2_1", "7_3_1"]

# Generate Logic for Create and Update
for obj_id in cr_now:
    form_data = f"""
# ------------------------- * Data Add and Edit Logic for  {obj_id} *  ----------------------------- #
# Create Criteria {obj_id}
class CV{obj_id}CreateView(LoginRequiredMixin, CreateView):
    template_name = "criteria/create.html"
    success_message = "Successfully Created"
    form_class = C{obj_id}CreateForm
    criteria_id = "c{obj_id}"
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
        kwargs = super(CV{obj_id}CreateView, self).get_form_kwargs(*args, **kwargs)
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
        super(CV{obj_id}CreateView, self).__init__(*args, **kwargs)


# Update Criteria {obj_id}
class CV{obj_id}UpdateView(LoginRequiredMixin, UpdateView):
    model = CriterionMaster
    form_class = C{obj_id}UpdateForm
    template_name = "criteria/update.html"
    criteria_id = "c{obj_id}"
    success_url = '/criteria/show/' + criteria_id

    def get_success_url(self):
        return '{{}}#criterions'.format(reverse('criterions:show-criteria', kwargs={{'slug': 'c{obj_id}'}}))

    def form_valid(self, form):
        instance = form.save(commit=False)
        if (instance.user == self.request.user) and (instance.status in ("PENDING", "REVERTED")):
            messages.add_message(self.request, messages.SUCCESS, "Updated Page")
            return super(CV{obj_id}UpdateView, self).form_valid(form)

        elif str(self.request.user.user_scope) in ("ADMIN", "NAAC_COD"):
            messages.add_message(self.request, messages.INFO, "Updated Data by Admin is done!")
            return super(CV{obj_id}UpdateView, self).form_valid(form)

        messages.add_message(self.request, messages.ERROR, "Edit Permission Error.!")
        return redirect(self.success_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CV{obj_id}UpdateView, self).get_form_kwargs(*args, **kwargs)
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
        super(CV{obj_id}UpdateView, self).__init__(*args, **kwargs)

    """
    filename = "view_data.txt"
    fx = open(filename, "a")
    fx.write(form_data)
    fx.close()
print("Success fully Completed..!")
