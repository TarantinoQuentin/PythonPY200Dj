from django.shortcuts import render
from django.views import View
from .forms import IndexForm
from django.http import JsonResponse


class IndexView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):
        received_data = request.POST
        form = IndexForm(received_data)
        if form.is_valid():
            my_text = form.cleaned_data.get("my_text")
            my_email = form.cleaned_data.get("my_email")
            my_another_text = form.cleaned_data.get("my_another_text")
            my_text_area = form.cleaned_data.get("my_text_area")
            result_dict = form.cleaned_data

            # Заголовок HTTP_X_FORWARDED_FOR используется для идентификации исходного IP-адреса клиента,
            # который подключается к веб-серверу через HTTP-прокси или балансировщик нагрузки.
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')
            result_dict['ip'] = ip
            result_dict['user_agent'] = user_agent
            return JsonResponse(result_dict, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        return render(request, 'landing/index.html', context={"form": form})
