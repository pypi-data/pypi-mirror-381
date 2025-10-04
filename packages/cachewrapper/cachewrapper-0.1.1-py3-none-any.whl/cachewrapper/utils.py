
def dict_converter_factory(source_class: type, target_class: type):
    assert issubclass(source_class, dict)
    assert issubclass(target_class, dict)

    def convert_dict_subclasses(obj):
        if isinstance(obj, dict):
            if isinstance(obj, source_class):
                new_dict = target_class()
                for key, value in obj.items():
                    new_dict[key] = convert_dict_subclasses(value)
                return new_dict
            else:
                return {key: convert_dict_subclasses(value) for key, value in obj.items()}
        elif isinstance(obj, (list, tuple, set)):
            return type(obj)(convert_dict_subclasses(item) for item in obj)
        else:
            return obj

    return convert_dict_subclasses
