from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View

from .forms import ExtendedAccountCreationForm, OrganisationProfileForm


class RegisterView(View):

    def get(self, request):
        form = ExtendedAccountCreationForm()
        profile_form = OrganisationProfileForm()
        return render(request, 'registration.html', {'form': form, 'profile_form': profile_form})

    def post(self, request):

        form = ExtendedAccountCreationForm(request.POST)
        profile_form = OrganisationProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            account = form.save()

            profile = profile_form.save(commit=False)
            profile.representative = account

            profile.save()

            return redirect('login')
        else:
            return render(request, 'registration.html', {'form': form, 'profile_form': profile_form})


class LoginAccountView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'


class HomepageView(View):
    def get(self, request):
        return render(request, 'home.html')
