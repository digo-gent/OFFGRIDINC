from .models import Service
from .forms import NewsLetterForm
from agency.models import SEOSettings

def services_navbar(request):
    return {
        "services": Service.objects.all()
    }

def global_footer_data(request):
    return {
        'newsletter_form': NewsLetterForm(prefix='newsletter')
    }


def seo_context(request):
    path = request.path.strip('/')
    page_slug = path.split('/')[0] if path else 'home'

    # Optional: manually map known slugs if URLs don't directly match SEOSettings
    page_map = {
        '': 'home',
        'about': 'about',
        'services': 'services',
        'contact': 'contact',
        'blog': 'blog',
        'testimonials': 'testimonial',
    }
    page_slug = page_map.get(page_slug, page_slug)

    seo = SEOSettings.objects.filter(page=page_slug).first()
    return {
        'meta_title': seo.title if seo else '',
        'meta_description': seo.description if seo else '',
        'meta_keywords': seo.keywords if seo else '',
        'og_image': seo.og_image if seo else None,
        'twitter_card_type': seo.twitter_card_type if seo else 'summary_large_image',
    }
