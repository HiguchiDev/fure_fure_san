from django.views.generic import TemplateView

# Create your views here.

class TermsView(TemplateView):
    template_name: str = "terms.html"
    