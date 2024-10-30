from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Replace with your actual template name
