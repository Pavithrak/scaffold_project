def extract_file_name_from_template_name(name):
    arr = name.split('.')
    arr.remove('j2')
    return '.'.join(arr)
