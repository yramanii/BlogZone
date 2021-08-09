from django.shortcuts import render
from .forms import contactForm, signupForm
from django.views.generic.edit import FormView
from django.views.generic import ListView, TemplateView
from .models import createBlog
from .forms import blogForm
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse


# Function Based Views

# def contact(request):

#     form = contactForm()

#     if request.method == 'POST':
#         print(request.POST)
#         form = contactForm(request.POST)


#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/contact')
    
#     context = {'form': form}

#     return render (request, 'contact.html', context)


class contact(FormView):
    template_name = 'contact.html'
    form_class = contactForm

    def form_valid(self, form):
        form.send_email()
        
        # return HttpResponse("Thanks for the review!")
        return HttpResponseRedirect('/contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class
        context = {'form':form}
        return context

    # First, we are saving our contact form data into DB but now we don't save the data although we sent the mail of data to the user.
    # def post(self, request):
    #     form = blogForm(request.POST, request.FILES or None)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/createblog')


# class based views

from django.urls import reverse_lazy

class HomePageView(ListView):
    template_name = "index.html"
    model = createBlog
    ordering = ['-id']

    # def get_context_data(self):

    #     show_data = viewBlog.objects.all()

    #     context = {'data':show_data}
    #     return context

class signupView(FormView):
    
    template_name = "registration/signup.html"
    form_class = signupForm
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class
        context = {'form3':form}
        return context

    def post(self, request):
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
        # return redirect('accounts/login/')
        return HttpResponseRedirect('/accounts/login')
    success_url = reverse_lazy('login')


class LoginView(TemplateView):
    template_name = "login.html"



# @login_required
# class loginview():

#     template_name = "login.html"
#     form_class = loginForm

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         form = self.form_class
#         context = {'form2':form}
#         return context

#     def post(self, request):
#         form = loginForm(request.POST, request.FILES or None)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect('/')



class createBlog(FormView):
    
    template_name = 'createblog.html'
    form_class = blogForm
    success_url = '/createblog/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class
        context = {'form1':form}
        return context

    def post(self, request):
        form = blogForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createblog')


    
    # def get(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)

    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form

    #     return self.render_to_response(context)

    
    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)

    #     if form.is_valid():
    #         return self.form_valid(form, **kwargs)
    #     else:
    #         return self.form_invalid(form, **kwargs)
    
    # def form_invalid(self, form, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    

    # def form_valid(self, form):
    #     # context = self.get_context_data(**kwargs)
    #     # context['form'] = form
    #     return super().form_valid(form)

    # def get(self, request):
    #     form = blogForm()
        
    #     if request.method == 'POST':
    #         form = blogForm(request.POST)

    #         if form.is_valid():
    #             form.save()

    #     return render(request, self.template_name, {'form':form})


# class blogCreateView(CreateView):

#     model = createBlog
#     fields = '__all__'
#     template_name = 'createblog.html'

# class blogUpdateView(UpdateView):

#     model = createBlog
#     fields = '__all__'
#     template_name = 'createblog.html'

# class blogDeleteView(DeleteView):

#     model = createBlog
#     success_url = reverse_lazy('createblog.html')
