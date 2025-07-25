from agency.models import SEOSettings

def get_seo_context(page_slug):
    seo = SEOSettings.objects.filter(page=page_slug).first()
    if not seo:
        return {}
    return {
        'meta_title': seo.title,
        'meta_description': seo.description,
        'meta_keywords': seo.keywords,
        'og_image': seo.og_image,
        'twitter_card_type': seo.twitter_card_type,
    }
