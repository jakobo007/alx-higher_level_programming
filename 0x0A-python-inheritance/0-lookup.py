"""Function that returs the list of available atrributes and methods of an object"""
def lookup(obj):
    list = dir(obj)
    return list