from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from .generator.create import generate_tables, generate_reports, all_criterion


# Create your views here.
def index(request):
    return HttpResponse("Welcome to AutoUpdate app Home..!")


class PasswordValidator(View):
    def get(self, request):
        return render(request, "criterions/staff_password_entry.html")

    def post(self, request):
        try:
            password = request.POST['password']
            option = request.POST['option']
            if str(password) == "vassgps@2021" and str(option) == "1":
                generate_tables()
                messages.add_message(request, messages.SUCCESS, 'Tables Updated Successfully')
            elif str(password) == "vassgps@2021" and str(option) == "2":
                generate_reports()
                messages.add_message(request, messages.SUCCESS, 'Reports Updated Successfully')
            else:
                messages.add_message(request, messages.WARNING, 'Incorrect ID or Password')
        except Exception as e:
            print("Error :", e)
            messages.add_message(request, messages.ERROR, 'Something went wrong..!')
        return render(request, "criterions/staff_password_entry.html")


# Display list of Tuples and Dictionary of all field names
def show_field_names(request):
    kstring = ""
    vstring = ""
    for obj in all_criterion:
        ks = f""" "{obj}": f{obj}[:-2], """
        vs = f""" "{obj}": d{obj}, """
        kstring = kstring + ks
        vstring = vstring + vs

    print(kstring)
    print(vstring)
