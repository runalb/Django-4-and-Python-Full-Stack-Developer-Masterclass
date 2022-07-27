from django.urls import path
from . import views

urlpatterns = [
    path("sv/",views.simple_view),

    # ---- Dynamic urls: ----
    
    # /123 intiger urls
    path("<int:value>",views.int_view),
    # /sting_value urls
    path("<str:value>",views.string_view),
    # /urls-with-dashes
    path("<slug:value>",views.slug_view),



]
