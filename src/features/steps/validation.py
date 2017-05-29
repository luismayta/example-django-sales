import json
from test.tools import normalize_data

from behave import then
from django.apps import apps
from hamcrest import assert_that, has_entries, has_item, not_none


@then(u'the resource "{resource}" with "{field}" "{value}" should have')
def the_resource_with_field_value_should_have(context, resource, field, value):
    data = dict()
    url = '{0}/{1}'.format(resource, value)
    response = context.client.get(url)
    for row in context.table:
        data = normalize_data(row.as_dict())

    response_data = json.loads(response.content.decode('utf-8'))
    assert_that(response_data, has_entries(data))


@then(u'the resource "{resource}" should have')
def the_resource_should_have(context, resource):
    response = context.client.get(resource)
    response_data = json.loads(response.content.decode('utf-8'))
    items = response_data.get('results')
    assert_that(items, not_none)
    items = [normalize_data(item) for item in items]
    for row in context.table:
        row = normalize_data(row.as_dict())
        assert_that(items, has_item(has_entries(row)))


@then(u'the response of "{var}" must be')
def the_response_of_var_must_be(context, var):
    items = context.response.get(var)
    for row in context.table:
        row = normalize_data(row.as_dict())
        assert_that(items, has_item(has_entries(row)))


@then(u'the apps "{application}" model "{model}" should have')
def the_apps_model_should_have(context, application, model):
    app_model = apps.get_model(application, model)
    headings = context.table.headings
    items = list()
    values = app_model.objects.values(*headings)
    for value in values:
        data = dict()
        for head in headings:
            try:
                data[head] = value.get(head)
            except AttributeError:
                data[head] = None
        items.append(normalize_data(data))

    for row in context.table:
        row = normalize_data(row.as_dict())
        assert_that(items, has_item(has_entries(row)))
