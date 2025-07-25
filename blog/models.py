from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse
from django.utils.timezone import now
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.utils.functional import cached_property
from django.dispatch import receiver

#Blog Model
        
class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200, blank=False, null=False, unique=True)
    slug = models.SlugField(unique=True)
    content = CKEditor5Field('Content', config_name='default')
    image = models.ImageField(upload_to='images', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-published_at']
        
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)

@receiver(pre_save, sender=Post)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        base_slug = slugify(f"{instance.author.username}-{instance.title}")
        slug = base_slug
        num = 1
        while Post.objects.filter(slug=slug).exclude(pk=instance.pk).exists():
            slug = f"{base_slug}-{num}"
            num += 1
        instance.slug = slug
        
    # Auto-set published_at when status is changed to published
    if instance.status == 'published' and not instance.published_at:
        instance.published_at = now()
        
    #Auto-uncheck is_featured if status is draft
    if instance.status == 'draft':
        instance.is_featured = False