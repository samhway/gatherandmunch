from django.urls import path
from .views import indexPageView, aboutPageView, portfolioView, displayPageView, contactPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about/', aboutPageView, name='about'),
    path('portfolio/', portfolioView, name='portfolio'),
    path('display/<str:portItem>', displayPageView, name='display'),
    path('contact/', contactPageView, name='contact'),
]
