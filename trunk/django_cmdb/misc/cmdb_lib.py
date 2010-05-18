
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
    for ci in ConfigurationItem.objects.filter(active=True,
            path__startswith=string):
        short_path = ci.path[ len(string): ]
        if not short_path:
            pass
        else:
            ret.append( (ci.pk, short_path[1:] ) )
    return ret
