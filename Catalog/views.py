from django.shortcuts import render

def main(request):
    return render (request, 'Catalog/main.html')

def resume(request):
    return render (request, 'Catalog/resume.html')
