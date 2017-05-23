# file:features/steps/step_login.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('a user')
def step_impl(context):
    from django.contrib.auth.models import User
    u = User(username='foo')
    u.set_password('bar')


@when('i log in as "foo" with "bar"')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')
    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('bar')
    br.find_element_by_name('submit').click()


@then('i can see my home site')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/dashboard/')


@when('i log in with invalid "anonymous" and "none"')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')
    br.find_element_by_name('username').send_keys('anonymous')
    br.find_element_by_name('password').send_keys('none')
    br.find_element_by_name('submit').click()


@then('i will see error message')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('error')



