from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomeUserCreationForm

# Create your views here.
class DashboardView(View):
    def get(self,request):
        return render(request, "users/dashboard.html")

class RegisterView(View):
    def get(self, request):
        return render(request, "users/register.html", {"form":CustomeUserCreationForm})

    def post(self, request):
        form = CustomeUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
