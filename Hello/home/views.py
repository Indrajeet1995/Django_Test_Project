from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # context = {
    #     "variable":"Variable passed successfully"
    # }
    # return HttpResponse("Home Page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is page is About Us")

def services(request):
    return HttpResponse("These are our services") 

def contact(request):
    return HttpResponse("This is our Contact Page") 
    
          