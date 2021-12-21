from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from accounts_app.models import OrganisationProfile
from requests_app.forms import NewRequestForm
from requests_app.models import Request


class CreateRequestView(LoginRequiredMixin, View):
    def get(self, request):
        form = NewRequestForm()
        return render(request, 'create_request.html', {'form': form})

    def post(self, request):
        form = NewRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.account = OrganisationProfile.objects.get(representative=request.user)
            new_request.save()

            return redirect('chat_request', pk=new_request.pk)

        else:
            return render(request, 'create_request.html', {'form': form})


class ListRequestsView(LoginRequiredMixin, View):
    def get(self, request):
        account = OrganisationProfile.objects.get(representative=request.user)
        requests = Request.objects.filter(account=account).order_by('date_creation').filter(
            Q(status__icontains='На рассмотрении') | Q(status__icontains='В работе')
        )
        return render(request, 'list_requests.html', {'requests': requests})


