from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, is successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(selfself, request, user):
        return '/activities/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ic_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^activities/', include('activities.urls')),
    url(r'^prob/', include('prob.urls')),
    url(r'^artigos/', include('artigos.urls')),
    
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
