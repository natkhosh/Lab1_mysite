from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class SafarioView(View):

    def get(self, request):
        return render(request, '../templates/index.html')


    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</body></html>'
        return HttpResponse(html)


class ContactsView(View):

    def get(self, request):
        return render(request, '../templates/contact/contact.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</body></html>'
        return HttpResponse(html)




