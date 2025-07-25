from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout,login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *

# Create your views here.

#Account Views
class AccountListView(ListView):
    template_name='account/account_list.html'
    model=Account
    context_object_name='accounts'
    
class AccountDetailView(LoginRequiredMixin, DetailView):
    model=Account
    template_name='account/account_detail.html'
    
    def get_object(self, queryset=None):
        return self.request.user
    
    
class AccountCreateView(CreateView):
    template_name="account/account_create.html"
    model=Account
    form_class=AccountCreationForm
    success_url = reverse_lazy ("account_detail" )
    
    def form_valid(self, form):
        response= super().form_valid(form)
        login(self.request, self.object)  # optional: auto-login after signup
        messages.success(self.request, "Account added successfully.")
        return response
    
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model=Account
    form_class=AccountChangeForm
    template_name="account/account_edit.html"
    success_url=reverse_lazy("account_detail")
    
    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Account updated successfully.")
        return response
    
class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    template_name = "account/account_delete.html"
    success_url= reverse_lazy("accounts")
    
    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        # Log out the user before deleting their account
        logout(request)
        messages.success(request, "Your account has been deleted.")
        return super().delete(request, *args, **kwargs)