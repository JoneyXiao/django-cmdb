from piston.authentication import HttpBasicAuthentication
from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import ConfigurationItemHandler, ContainerHandler
from api.emitters import *

auth = HttpBasicAuthentication(realm="My Realm")
ad = { 'authentication': auth }

ci_resource = Resource(ConfigurationItemHandler, **ad)
container_resource = Resource(ContainerHandler, **ad)

urlpatterns = patterns('',
        url(r'Containers$', container_resource),
        url(r'^(?P<path>[-\w\./\s]+)$', ci_resource),
        url(r'^$', ci_resource),
)
