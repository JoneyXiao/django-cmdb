from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import ConfigurationItemHandler
from api.emitters import *

ci_resource = Resource(ConfigurationItemHandler)

urlpatterns = patterns('',
        url(r'^(?P<path>[-\w\./\s]+)$', ci_resource),
        url(r'^$', ci_resource),
)
