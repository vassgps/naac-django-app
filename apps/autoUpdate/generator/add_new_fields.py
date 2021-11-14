# autoUpdate/generator/table_templates.py
from django.shortcuts import render
from django.views import View
from django.contrib import messages, auth
import json


class DataEntryForm(View):

    def get(self, request):
        return render(request, "criterions/data_entry_form.html")

    def post(self, request):
        field_dict = {}  #
        name_list = []
        data_list = {"cid": "ip0", "date": "ip1", "date2": "ip2", "date3": "ip3", "date4":"ip4", "date5":"ip5",
                     "text1":"ip6", "text2":"ip7", "text3":"ip8", "text4":"ip9", "text5":"ip10", "text6":"ip11",
                     "text7":"ip12", "text8":"ip13", "text9":"ip14", "text10":"ip15", "text11":"ip16",
                     "text12":"ip17", "text13":"ip18", "text14":"19", "text15":"ip20", "text16":"ip21"}
        for key, value in data_list.items():
            try:
                if request.POST.get(value) is not None:
                    fdata = request.POST.get(value)
                    if str(fdata) != "":
                        field_dict.update({key: fdata})
                        name_list.append(key)
            except:
                pass  # templates/criteria/
        field_dict.update({"file1": "Additional Information Files", "url1": "Additional Info Link"})
        name_list.append("file1")
        name_list.append("url1")
        print(field_dict, " - ", name_list)
        filename = "templates/criteria/field_names.txt"
        cr_string = f"#--------------------------* {field_dict['cid']} *---------------------------------------"
        fx = open(filename, "a")
        fx.write(cr_string + '\n')
        fx.write(str(name_list) + '\n')
        fx.write(str(field_dict) + '\n')
        fx.close()
        messages.add_message(request, messages.SUCCESS, 'Form fields added')
        return render(request, "criterions/data_entry_form.html")
