from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

#Testimonial Model   
class Testimonial(models.Model):
        testimony=models.TextField()
        client=models.CharField(max_length=50)
        owner=models.CharField(max_length=50)
        created_at=models.DateTimeField(auto_now=True)
        
        class Meta:
            ordering=['-created_at']
        
        def __str__(self):
            return self.client
        
#ClientLogo Model       
class ClientLogo(models.Model):
        client=models.CharField(max_length=50, unique=True)
        owner=models.TextField(max_length=50, unique=True)
        logo=models.FileField(upload_to='logos/')
        created_at=models.DateTimeField(auto_now=True)
        
        class Meta:
            ordering=['-created_at']
        
        def __str__(self):
            return self.client
        

#Service Model
class Service(models.Model):
    SERVICE_CHOICES=[
            ('Social media management','Social Media Management'),
            ('google & meta ads','Google & Meta Ads'),
            ('email marketing','Email Marketing'),
            ('influencer marketing','Influencer Marketing'),
            ('branding and media buying','Branding & Media Buying'),
            ('photography and videography','Photography & Videography'),
        ]
    
    service =models.CharField(max_length=50, choices=SERVICE_CHOICES, unique=True, blank=True)
    overview=models.TextField(max_length=150, blank=True)
    description=CKEditor5Field('Content',null=True, config_name='default')
    image=models.ImageField(upload_to='services/', blank=True, null=True)
    case_study=models.FileField(upload_to='case_studies/', null=True, blank=True)
    
    def get_file_url(self):
        if self.case_study:
            return self.case_study.url
        return None
    
    @property
    def display_service(self):
        return self.get_service_display()
    
    def __str__(self):
        return self.display_service
    
#Package model
class Package(models.Model):
    PACKAGE_CHOICES = [
        ('standard', 'Standard'),
        ('premium', 'Premium'),
        ('enterprise', 'Enterprise'),
    ]

    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=False, blank=False, related_name='packages')
    package = models.CharField(max_length=50, choices=PACKAGE_CHOICES, null=True)
    package_details = CKEditor5Field('Content', config_name='default')

    @property
    def display_package(self):
        return self.get_package_display()

    @property
    def display_service(self):
        return self.service.service if self.service else "No Service"
    
    def __str__(self):
        return f"{self.display_package} {self.display_service}"



#Contact Model
class Contact(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    company_name=models.CharField(max_length=100)
    subject=models.CharField(max_length=50)
    industry=models.CharField(max_length=100,null=True, blank=True)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message=models.TextField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Newsletter   
class NewsLetter(models.Model):
    email=models.EmailField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.email

#Service Inquiry
class ServiceInquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    service = models.CharField(max_length=50, choices=Service.SERVICE_CHOICES)
    package = models.CharField(max_length=50, choices=Package.PACKAGE_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

class SEOSettings(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home Page'),
        ('about', 'About Page'),
        ('services', 'Services Page'),
        ('blog', 'Blog Page'),
        ('contact', 'Contact Page'),
        ('testimonial', 'Testimonial Page'),
        # Add more as needed
    ]

    page = models.CharField(max_length=50, choices=PAGE_CHOICES, unique=True)
    title = models.CharField(max_length=255, help_text="Meta Title for SEO and Social Media")
    description = models.TextField(help_text="Meta Description for SEO")
    keywords = models.TextField(help_text="Comma-separated keywords")

    # Optional Open Graph
    og_image = models.ImageField(upload_to="seo/", null=True, blank=True, help_text="Recommended size: 1200x630")
    twitter_card_type = models.CharField(
        max_length=20,
        choices=[('summary', 'Summary'), ('summary_large_image', 'Summary Large Image')],
        default='summary_large_image'
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SEO: {self.get_page_display()}"
