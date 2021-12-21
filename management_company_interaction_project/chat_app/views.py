from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from chat_app.constants import CLOSE_STATUS_MESSAGE, WORK_STATUS_MESSAGE
from chat_app.models import RequestMessage
from requests_app.models import Request

from rolepermissions.checkers import has_permission


class ChatRequestView(LoginRequiredMixin, View):
    def get(self, request, pk):
        selected_request = Request.objects.get(pk=pk)

        is_manager = has_permission(request.user, 'create_medical_record')

        if selected_request.account.representative != request.user and not is_manager:
            return redirect('list_requests')

        messages = RequestMessage.objects.filter(request=selected_request)
        return render(request, 'chat_request.html', {'selected': selected_request,
                                                     'messages': messages,
                                                     'is_manager': is_manager})

    def post(self, request, pk):
        response_data = {}
        try:
            selected_request = Request.objects.get(pk=pk)

            content = request.POST.get('content')

            new_message = RequestMessage.objects.create(
                request=selected_request,
                status='отправлено',
                content=content
            )
            response_data['status'] = 'OK'
            response_data['user'] = request.user.username
            response_data['content'] = content
            response_data['date'] = new_message.date.strftime("%d %B %Y г. %H:%M")

            return JsonResponse(response_data)

        except Exception as e:
            print(e)
            response_data['status'] = 'BAD'
            return JsonResponse(response_data)


class SetWorkStatusView(View):
    def post(self, request, pk):
        response_data = {}
        try:
            response_data = get_response_data(pk, 'В работе', request, WORK_STATUS_MESSAGE)
            return JsonResponse(response_data)

        except Exception as e:
            print(e)
            response_data['status'] = 'BAD'
            return JsonResponse(response_data)


class SetCloseStatusView(View):
    def post(self, request, pk):
        response_data = {}
        try:
            response_data = get_response_data(pk, 'Закрыта', request, CLOSE_STATUS_MESSAGE)
            return JsonResponse(response_data)

        except Exception as e:
            print(e)
            response_data['status'] = 'BAD'
            return JsonResponse(response_data)


def get_response_data(id, status, request, content_msg):
    data = {}
    selected_request = Request.objects.get(pk=id)
    selected_request.status = status
    selected_request.save()

    new_message = RequestMessage.objects.create(
        request=selected_request,
        status='отправлено',
        content=content_msg,
        is_system=True
    )
    data['status'] = 'OK'
    data['user'] = request.user.username
    data['content'] = content_msg
    data['date'] = new_message.date.strftime("%d %B %Y г. %H:%M")

    return data
