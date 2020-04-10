from django.urls import path

from . import views
from django.views.generic import TemplateView
app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name="main/main.html"), name="homepage"),
    path('choice', TemplateView.as_view(template_name="main/choicePage.html"))
]