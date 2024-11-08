import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    obj_module = getattr(obj, '__module__', None)

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
    }
    return info


number_info = introspection_info("ddd")
print(number_info)
