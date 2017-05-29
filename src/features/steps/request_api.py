import json
from test.tools import del_key_by_value, normalize_data

from behave import then
from hamcrest import assert_that, not_none


def factory_method_request(context, method, items, resource):

    methods_available = {
        'post': request_method_post,
        'patch': request_method_patch,
        'delete': request_method_delete,
    }
    method_function = methods_available.get(method, None)
    if not method_function:
        raise ValueError('{0} not available'.format(method))

    return method_function(
        context=context,
        method=method,
        items=items,
        resource=resource
    )


def response_to_dict(response):
    data = dict()
    if isinstance(response.content, bytes):
        data = response.content.decode('utf-8')
        if data:
            data = json.loads(data)
        else:
            data = dict()
            data['content'] = None
    data['status_code'] = response.status_code
    return normalize_data(data)


def request_method_post(context, method, items, resource):
    extra = dict()
    extra['format'] = 'json'
    response_list = list()
    for item in items:
        item = del_key_by_value(item)
        response = context.client.post(
            resource,
            data=item,
            **extra
        )
        assert_that(response, not_none)
        response_list.append(response_to_dict(response))

    return response_list


def request_method_patch(context, method, items, resource):
    extra = dict()
    extra['format'] = 'json'
    response_list = list()
    for item in items:
        pk_order = item.get('id')
        url = '{0}/{1}'.format(
            resource,
            pk_order,
        )
        item.pop('id')
        item = del_key_by_value(item)
        response = context.client.patch(
            url,
            data=item,
            **extra
        )

        assert_that(response, not_none)
        response_list.append(response_to_dict(response))

    return response_list


def request_method_delete(context, method, items, resource):
    extra = dict()
    extra['format'] = 'json'
    response_list = list()
    for item in items:
        pk_order = item.get('id')
        url = '{0}/{1}'.format(
            resource,
            pk_order,
        )
        item.pop('id')
        item = del_key_by_value(item)
        response = context.client.delete(
            url,
            data=item,
            **extra
        )

        assert_that(response, not_none)
        response_list.append(response_to_dict(response))

    return response_list


@then(u'"{method}" the "{var}" to the resource "{resource}":')
def method_the_var_with_resource(context, method, var, resource):
    items = list()
    extra = dict()
    response_list = list()
    if hasattr(context, var):
        items = getattr(context, var)

    extra['format'] = 'json'

    if not isinstance(items, (list, tuple)):
        items = [items, ]

    response_list = factory_method_request(
        context=context,
        method=method,
        items=items,
        resource=resource)

    context.response = dict()
    context.response[var] = response_list
