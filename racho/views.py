from django.shortcuts import render, redirect
from .forms import FeedBackForm
# from .forms import TopBackForm
from django.views.generic import View



def index(request):
    return render(request, 'index.html')

def top(request):
    return render(request, 'top.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def ustav(request):
    return render(request, 'ustav.html')

def contests(request):
    return render(request, 'contests.html')



class FeedBackView(View):
      def post(self, request):
          form = FeedBackForm(request.POST)
          if form.is_valid():
              form.save()

          return redirect("/")
