
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from rapidsms.views import dashboard
from rtwilio.views import TwilioBackendView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # rapidSMS urls
    url(r'^accounts/', include('rapidsms.urls.login_logout')),
    url(r'^$', dashboard, name='rapidsms-dashboard'),
    #rapidSMS contrib app URLs
    url(r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
    # 3rd party urls
    url(r'^selectable/', include('selectable.urls')),

]

if 'twilio-backed' in settings.INSTALLED_BACKENDS:
    urlpatterns += [
        url(
            r'backend/twilio/$',
            TwilioBackendView.as_view(backend_name='twilio-backend'),
        ),
    ]

if settings.DEBUG:
    urlpatterns += [
        url(r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    ]