from django.shortcuts import render

# Create your views here.
def first_html(request):
    return render(request,'h1.html')