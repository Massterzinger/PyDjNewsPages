from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from mainpg import forms
from django.http import HttpResponse
from news.models import NewsPost

# Create your views here.

def facepage(request):
    obs = NewsPost.objects.all()[:3]
    for i in obs:
        i.body = i.body[:86]+'...'
    return HttpResponse(render(request, "face.html", {'posts':obs} ))

class UserFormView(generic.View):
    form_class = forms.UserForm
    template_name = 'registerform.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user != None:
                if user.is_active:
                    login(request, user)
                    return redirect('/news')
                
        return render(request, self.template_name, {'form':form})

class UserLogInFormView(generic.View):
    form_class = forms.UserLogInForm
    template_name = 'registerform.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        #print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/news')
                
        return render(request, self.template_name, {'form':form})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return redirect('/news')