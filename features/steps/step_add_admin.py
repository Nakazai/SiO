# file:features/steps/step_add_admin.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('a admin form')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/InnsideSignUp/')


@when('i fill in "sara","bara","fb@gmail.com","leader","sara"')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/InnsideSignUp/')
    br.find_element_by_name('first_name').send_keys('sara')
    br.find_element_by_name('last_name').send_keys('bara')
    br.find_element_by_name('email').send_keys('fb@gmail.com')
    br.find_element_by_name('union_position').send_keys('leader')
    br.find_element_by_name('username').send_keys('sara')


@when('register the admin form')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit').click()


@when('cancel the admin form')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('cancel').click()


@then('i will see the new admin added')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/admin_overview/')


@then('i will be redirected to overview of all admins')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/admin_overview/')

