from test.drf import APIClient
from test.factories.user import UserFactory

from behave import given
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
