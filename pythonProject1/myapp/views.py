from django.shortcuts import render
from django.http import HttpResponse
import json

def index_view(request):
    if request.method == 'POST':
        try:
            # Предполагается, что данные из формы отправляются в формате JSON
            data = json.loads(request.body.decode('utf-8'))  # Раскодирование JSON из тела запроса
            theme = data.get('theme')
            lang = data.get('lang')

            response = HttpResponse("Настройки сохранены!")  # Создание ответа

            # Установка cookies
            if theme:
                response.set_cookie('theme', theme, max_age=31536000)  # Куки темы, срок действия - 1 год
            if lang:
                response.set_cookie('lang', lang, max_age=31536000)  # Куки языка, срок действия - 1 год

            return response

        except json.JSONDecodeError:  # Обработка ошибки
            return HttpResponse("Неверные данные", status=400)

    else:
        # Получение куки для применения настроек.
        theme_cookie = request.COOKIES.get('theme')
        lang_cookie = request.COOKIES.get('lang')
        context = {'theme': theme_cookie, 'lang': lang_cookie}
        return render(request, 'myapp/index.html', context)