from django.shortcuts import render, redirect
from .forms import TopBackForm
from django.views.generic import View



class TopBackView(View):
    def post(self, request):
        form = TopBackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect("/")






