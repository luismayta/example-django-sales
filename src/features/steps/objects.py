from test.factories.registry import Apps
from test.tools import del_key_by_value, normalize_data

from behave import given
from core.utils import get_model_app
from hamcrest import assert_that, not_none


@given(u'the "{var}" update with')
def the_var_update_with(context, var):
    model = get_model_app(var)

    for row in context.table:
        row = normalize_data(del_key_by_value(row.as_dict()))
        args_search = dict()
        args_search = {'id': row.get('id')}
        args_search['defaults'] = row
        obj, created = model.objects.update_or_create(**args_search)
        assert_that(obj, not_none)


@given(u'the "{var}" with')
def the_var_with(context, var):
    factory_class = Apps.get_factory(var)

    for row in context.table:
        factory_object = None
        row = normalize_data(del_key_by_value(row.as_dict()))
        factory_object = factory_class.create(**row)
        assert_that(factory_object, not_none)
