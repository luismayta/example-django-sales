from importlib import import_module

from django.conf import settings
from django.template import Context, Template

try:
    from django.apps import apps, AppConfig
    get_model = apps.get_model
except ImportError:
    from django.db.models.loading import get_model
    AppConfig = None


def get_name_object(instance):
    return '{}.{}'.format(
        instance.__class__.__module__.split('.')[0],
        instance.__class__.__name__,
    )


def get_model_app(model):
    return get_model(*model.split('.'))


def get_credential_model():
    return get_model(*settings.CREDENTIAL_MODEL.split('.'))


def get_client_model():
    return get_model(*settings.CLIENT_MODEL.split('.'))


def get_user_model():
    return get_model(*settings.USER_MODEL.split('.'))


def get_instance_model(*args, **kwargs):
    model = get_model_app(kwargs.get('model'))
    args = kwargs.get('args')
    return model.objects.get(**args)


def get_class(name):
    name = name.split('.')
    class_name = name.pop(-1)
    module = import_module('.'.join(name))
    return getattr(module, class_name)


def render(text, params):
    template = Template(text)
    return template.render(Context(params))


def getattr_args(var, args=str):
    items = args.split('.')
    for item in items:
        if not hasattr(var, item):
            raise ValueError('Not Exist {0}'.format(args))
        var = getattr(var, item)
    return var
