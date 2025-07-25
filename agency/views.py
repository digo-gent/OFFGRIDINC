from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .utils import get_seo_context
from blog.models import Post
from agency.forms import *

class HomeView(TemplateView):
    template_name = "agency/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_seo_context('home'))
        context['popular_posts'] = Post.objects.filter(status='published', is_featured=True)[:3]
        context['testimonials'] = Testimonial.objects.all().order_by('-created_at')
        context['services'] = Service.objects.all()
        context['clientlogos'] = ClientLogo.objects.all()
        
        return context
    
#Services Views
class ServiceListView(FormMixin, ListView):
    template_name='agency/service_list.html'
    model=Service
    context_object_name='services'
    form_class = ServiceInquiryForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientlogos'] = ClientLogo.objects.all()
        context.update(get_seo_context('service'))
    
        if self.request.method == 'POST':
            context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            form.save()
            messages.success(request, "Your inquiry was submitted successfully.")
            return redirect(request.path)
        else:
            messages.error(request, "There was an error submitting your inquiry.")
            return self.get(request, *args, **kwargs)
        
class ServiceDetailView(FormMixin, DetailView):
    model = Service
    template_name = 'agency/service_detail.html'
    context_object_name = 'service'
    form_class = ServiceInquiryForm

    def get_success_url(self):
        return reverse('service_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.object
        
        context['file_url'] = service.get_file_url() if service.get_file_url() else None
        # Just pass related packages
        context['packages'] = self.object.packages.all()
        context['testimonials'] = Testimonial.objects.all()
        context['clientlogos'] = ClientLogo.objects.all()
        context['form'] = self.form_class(initial={'service': service})
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Inquiry submitted successfully.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "There was an error submitting your inquiry. Please try again.")
        return super().form_invalid(form)
    
class ServiceCreateView(LoginRequiredMixin, CreateView):
    template_name="agency/service_create.html"
    model=Service
    form_class=ServiceForm
    success_url = reverse_lazy ("services" )
    
    def form_valid(self, form):
        response= super().form_valid(form)
        messages.success(self.request, "Service added successfully.")
        return response
    
class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model=Service
    template_name="agency/service_edit.html"
    form_class=ServiceForm
    success_url=reverse_lazy("services")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Service updated successfully.")
        return response
    
class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    template_name = "agency/service_delete.html"
    success_url= reverse_lazy("services")


#Testimonials views
class TestimonialListView(ListView):
    template_name='agency/testimonial_list.html'
    model=Testimonial
    context_object_name='testimonials'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_seo_context('testimonial'))
        return context
    
class TestimonialDetailView(DetailView):
    model=Testimonial
    template_name='agency/testimonial_detail.html'
    
class TestimonialCreateView(CreateView):
    template_name="agency/testimonial_create.html"
    model=Testimonial
    form_class=TestimonialForm
    success_url = reverse_lazy ("testimonials" )
    
    def form_valid(self, form):
        response= super().form_valid(form)
        messages.success(self.request, "Testimonial added successfully.")
        return response
    
class TestimonialUpdateView(LoginRequiredMixin, UpdateView):
    model=Testimonial
    form_class=TestimonialForm
    template_name="agency/testimonial_edit.html"
    success_url=reverse_lazy("testimonials")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Testimonial updated successfully.")
        return response
    
class TestimonialDeleteView(LoginRequiredMixin, DeleteView):
    model = Testimonial
    template_name = "agency/Testimonial_delete.html"
    success_url= reverse_lazy("testimonials")
    

#Logo views
class LogoListView(ListView):
    template_name='agency/logo_list.html'
    model=ClientLogo
    context_object_name='logos'
    
class LogoDetailView(DetailView):
    model=ClientLogo
    template_name='agency/logo_detail.html'
    
class LogoCreateView(LoginRequiredMixin, CreateView):
    template_name="agency/logo_create.html"
    model=ClientLogo
    form_class = ClientLogoForm
    success_url = reverse_lazy ("home" )
    
    def form_valid(self, form):
        response= super().form_valid(form)
        messages.success(self.request, "Logo added successfully.")
        return response
    
class LogoUpdateView(LoginRequiredMixin, UpdateView):
    model=ClientLogo
    form_class = ClientLogoForm
    template_name="agency/logo_edit.html"
    success_url=reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Logo updated successfully.")
        return response
    
class LogoDeleteView(LoginRequiredMixin, DeleteView):
    model = ClientLogo
    template_name = "agency/logo_delete.html"
    success_url= reverse_lazy("home")

    
#Contact views
class ContactView(FormView):
    template_name = 'agency/contact_us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy ('contact_us' ) # or redirect to same page

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Message sent successfully.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_us'] = Contact.objects.all()
        context.update(get_seo_context('contact'))
        return context
    

    
class PackageDetailView(DetailView):
    model=Package
    template_name='agency/package_detail.html'
    context_object_name="package"
    
class PackageCreateView(LoginRequiredMixin, CreateView):
    template_name="agency/package_create.html"
    model=Package
    form_class = PackageForm
    success_url = reverse_lazy ("services" )
    
    def form_valid(self, form):
        response= super().form_valid(form)
        messages.success(self.request, "Package added successfully.")
        return response
    
class PackageUpdateView(LoginRequiredMixin, UpdateView):
    model=Package
    form_class = PackageForm
    template_name="agency/package_edit.html"
    success_url=reverse_lazy("services")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Package updated successfully.")
        return response
    
class PackageDeleteView(LoginRequiredMixin, DeleteView):
    model = Package
    template_name = "agency/package_delete.html"
    success_url= reverse_lazy("services")


def newsletter_subscribe(request):
    if request.method == 'POST' and request.POST.get('form_type') == 'newsletter':
        form = NewsLetterForm(request.POST, prefix='newsletter')  # use the same prefix here
        if form.is_valid():
            form.save()
            messages.success(request, "Subscribed successfully!")
        else:
            messages.error(request, "Please enter a valid email.")
    return redirect(request.META.get('HTTP_REFERER', '/'))

    

