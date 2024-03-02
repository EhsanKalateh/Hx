from django.views.generic import TemplateView

class  MainPageView(TemplateView):
    template_name = "case_list.html"

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"