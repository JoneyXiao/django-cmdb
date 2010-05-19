import logging
logging.basicConfig(level=logging.DEBUG)


def get_parent_paths(path):
    split_path = path.split('/')
    try:
        split_path.remove('') # Remove the empty item that is left as the first item in the list
    except ValueError:
        # Someone has entered a path with no / in it... 
        raise ValidationError(u'Invalid Path')
    paths = [] # Create an empty list to hold the paths
    while len(split_path) > 0:
        # For each item in the CIs path
        new_path = '' # Create an empty string to hold this path
        for part in split_path:
            new_path = '''%s/%s''' % ( new_path, part)       # Generate the path
        paths.append(new_path) # Append this path to the list
        part_to_delete = split_path[-1]
        # As we iterate through the path we need to delete the last part of
        # the path.. find it now
        split_path.remove(part_to_delete)
        # Delete the part and do it all again....
    # Insert a single slash at the beginning of the list
    paths.append('/')
    return paths

def get_options_for_combo(string):
    ret = []
    from cmdb.models import ConfigurationItem
    try:
        for ci in ConfigurationItem.objects.filter(active=True,
            path__startswith=string):
            short_path = ci.path[ len(string): ]
            if not short_path:
                pass
            else:
                ret.append( (ci.pk, short_path[1:] ) )
        return ret
    except:
        pass

def get_correct_class(*args, **kwargs):
    if not kwargs.has_key('ci'):
        ci = ConfigurationItem.objects.get(path=kwargs['ci_path'])
    else:
        ci = kwargs['ci']

    from cmdb.models import *
    for part in get_parent_paths(ci.path):
        try:
            s = Schema.objects.get(path=part)
            return eval('''%s.objects.get(path='%s')''' % ( s.class_name, ci.path))
        except Schema.DoesNotExist:
            pass
    return False

def get_schema_for_ci(*args, **kwargs):
    from cmdb.models import ConfigurationItem, Schema
    if not kwargs.has_key('ci_path'):
        ci_path = kwargs['ci'].path
    else:
        ci_path = kwargs['ci_path']

    for part in get_parent_paths(ci_path):
        try:
            s = Schema.objects.get(path=part)
            return s
        except Schema.DoesNotExist:
            pass
    return False
        
def prefix_slash(s):
    return '''/%s''' % s


def collect_all_attributes_for_schema(schema):
    from cmdb.models import *
    parent_classes = get_parent_paths(schema.path)
    fields = []
    for path in parent_classes:
        _schema = Schema.objects.get(path=path)
        instance = eval('''%s()''' % _schema.class_name)
        instance_fields = [ f.name for f in instance._meta.fields ] + \
            [ f[0].name for f in instance._meta.get_m2m_with_model() ]
        for f in instance_fields:
            if f not in fields:
                fields.append(f)
    return fields

def serialize_object(ci):
    import simplejson as json
    fields = collect_all_attributes_for_schema(get_schema_for_ci(ci=ci))
    ret = {}
    for f in fields:
        if f[-4:] == '_ptr':
            pass
        else:
            ret[f] = eval('''ci.%s''' % f)
            logging.debug("Serializing field %s, value %s" % ( f, ret[f] ))
    return json.dumps(ret)


        
