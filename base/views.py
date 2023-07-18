from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class TestView(TemplateView):
    template_name = "base/test.html"

class Pagina2View(TemplateView):
    template_name = "base/test2.html"
