from django.views.generic import TemplateView

# Create your views here.

class PolicyPageView(TemplateView):
    template_name: str = "policy.html"
    