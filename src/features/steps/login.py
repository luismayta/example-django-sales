from test.drf import APIClient
from test.factories.user import UserFactory

from behave import given
from django.test import Client
from hamcrest import assert_that, not_none


@given(u'The user with "{email}" and password "{password}"')
def the_user_with_and_password(context, email, password):
    user = UserFactory(email=email)
    user.set_password(password)
    user.save()
    assert_that(user, not_none)
    context.user = user
    response = APIClient.login(
        username=email,
        password=password
    )

    assert_that(response, not_none)


@given(u'Login with "{email}" and "{password}"')
def login_with_email_password(context, email, password):
    client = APIClient()
    response = client.login(
        username=email,
        password=password
    )
    assert_that(response, not_none)

    context.client = client


@given(u'make token with "{email}" and "{password}"')
def make_token_with_and(context, email, password):
    client = Client()
    data = {
        'username': email,
        'password': password
    }
    response = client.post(
        '/api-token-auth/',
        data,
    )
    assert_that(response, not_none)
    assert_that(response.data.get('token', None), not_none)
    context.token = response.data.get('token')
