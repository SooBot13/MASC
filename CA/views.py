from django.shortcuts import render, HttpResponse 

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is homepage")  

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page") 

def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("This is contact page")

def test(request):
    return render(request,'testpage.html')     