from agency.models import *
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_ckeditor_5.widgets import CKEditor5Widget


#testimonial form
class TestimonialForm(ModelForm):
    
    class Meta:
        model = Testimonial
        fields = ("testimony","client","owner")
        widgets= {
            "testimony": forms.Textarea(attrs={"placeholder": "Testimony", "class": "form-control", "rows": 3}),
            "client": forms.TextInput(attrs={"placeholder": "Client", "class": "form-control"}),
            "owner": forms.TextInput(attrs={"placeholder": "Owner", "class": "form-control"}),
        }


#ClientLogo form
class ClientLogoForm(ModelForm):
    
    class Meta:
        model = ClientLogo
        fields = ("client","owner","logo")
        widgets= {
            "client": forms.TextInput(attrs={"placeholder": "Client" ,"class": "form-control"}),
            "owner": forms.Textarea(attrs={"placeholder": "Owner", "class": "form-control"}),
            "logo": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


#Contact Us form
class ContactUsForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "company_name", "email", "phone", "subject", "message")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send'))


#Service Inquiry Form
class ServiceInquiryForm(forms.ModelForm):
    class Meta:
        model = ServiceInquiry
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}),
            'last_name': forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}),
            'company_name': forms.TextInput(attrs={"placeholder": "Company Name", "class": "form-control"}),
            'industry': forms.TextInput(attrs={"placeholder": "Industry", "class": "form-control"}),
            'email': forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}),
            'phone': forms.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}),
            'message': forms.Textarea(attrs={"placeholder": "Your Message", "class": "form-control", "rows": 5}),
            'service': forms.Select(attrs={"class": "form-control"}),
            'package': forms.Select(attrs={"class": "form-control"}),
        }


        
#Service Form
class ServiceForm(ModelForm):
    class Meta:
        model= Service
        fields=("service", "overview","description","image","case_study")

#package Form
class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = ['service', 'package', 'package_details']
        
class NewsLetterForm(ModelForm):
    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "Enter your email",
            "class": "form-control"
        })
    )

    class Meta:
        model = NewsLetter
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if NewsLetter.objects.filter(email=email).exists():
            raise forms.ValidationError("You're already subscribed.")
        return email
