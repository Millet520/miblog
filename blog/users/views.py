from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from libs.captcha.captcha import captcha
from django_redis import get_redis_connection


# Create your views here.
class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')


class ImageCodeView(View):

    def get(self, request):
        uuid = request.GET.get('uuid')
        if uuid is None:
            return HttpResponseBadRequest('have not hand')
        text, image = captcha.generate_captcha()

        redis_conn = get_redis_connection('default')
        redis_conn.setex('img: %s' % uuid, 300, text)
        return HttpResponse(image, content_type='image/jpeg')
