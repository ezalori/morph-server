
import pkgutil


def load_module_recursively(module) -> None:
    for _, name, ispkg in pkgutil.iter_modules(module.__path__):
        module_name = '%s.%s' % (module.__name__, name)
        print('loading view: %s' % module_name)
        _module = __import__(module_name, fromlist=[''])

        if ispkg:
            load_module_recursively(_module)
