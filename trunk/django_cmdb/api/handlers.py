from piston.handler import BaseHandler
from cmdb.models import *
from misc.cmdb_lib import prefix_slash, get_correct_class, get_schema_for_ci
import logging
import urllib

class ConfigurationItemHandler(BaseHandler):

    model = ConfigurationItem

    def read(self, request, path=None):

        if not path:
            return ConfigurationItem.objects.filter(is_active=True)

        # As the path might contain %20 instead of ' ' dequote it
        # and also add in the original slash
        path = prefix_slash(urllib.unquote(path))
        logging.debug('In API module, path=%s' % path)
        s = get_schema_for_ci(ci_path=path)
        ci = eval('''%s.objects.filter(path__startswith='%s')''' % ( s.class_name, path ))
        logging.debug('ci = %s' % ci)
        return ci

