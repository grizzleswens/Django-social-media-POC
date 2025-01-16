from django.shortcuts import render
from django.views import View

class Index(View):
    
    # generic view class allows us to put different methods on our class, for each http method that we will handle
    # if you want just a get request for a web page, make a def get():
    # same for the other methods
    
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')