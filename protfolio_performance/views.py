from django.views import generic


class LandingPageView(generic.TemplateView):
	template_name = 'landing_page.html'