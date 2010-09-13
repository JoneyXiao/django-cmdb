from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import ConfigurationItemHandler, ContainerHandler
from api.emitters import *

ci_resource = Resource(ConfigurationItemHandler)
container_resource = Resource(ContainerHandler)

urlpatterns = patterns('',
        url(r'Containers$', container_resource),
        url(r'^(?P<path>[-\w\./\s]+)$', ci_resource),
        url(r'^$', ci_resource),
)
