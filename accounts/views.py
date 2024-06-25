from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth.models import User, Group
from .models import UserInfo
from .forms import CreateUserForm


class UserCreateView(CreateView):
    model = User
    form_class = CreateUserForm
    success_url = "/login"
    template_name = "accounts/create.html"

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.email = form.cleaned_data["email"]
        new_user.save()
        form.save_m2m()

        interests = form.cleaned_data["interests"]

        points_dict = {
            "roupas": 0,
            "fitness": 0,
            "beleza": 0,
            "eletronicos": 0,
            "outros": 0,
        }

        for value in interests:
            points_dict[value] = 100

        user_info = UserInfo(
            user=new_user,
            name=form.cleaned_data["name"],
            gender=form.cleaned_data["gender"],
            birthday=form.cleaned_data["birthday"],
            
            size=form.cleaned_data["size"],
            style=form.cleaned_data["style"],
            roupas=points_dict["roupas"],
            fitness=points_dict["fitness"],
            beleza=points_dict["beleza"],
            eletronicos=points_dict["eletronicos"],
            outros=points_dict["outros"]
        )

        user_info.save()
        

        return HttpResponseRedirect(reverse("login"))
