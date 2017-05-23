# file:features/steps/step_delete_admin.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@when('i click delete on a admin')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/admin_delete/')


@when('i get redirect to a confirmation message that tells me if i am sure to delete the admin')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/admin_delete/')


@when('i see "sara","bara","sa@gmail.com","leader","sara"')
def step_impl(context):
    br = context.browser
    br.get(context.get_url('/InnsideSignUp/'))

    br.find_element_by_name('first_name').send_keys('sara')
    br.find_element_by_name('last_name').send_keys('bara')
    br.find_element_by_name('email').send_keys('sa@gmail.com')
    br.find_element_by_name('union_position').send_keys('leader')
    br.find_element_by_name('username').send_keys('sara')


@then('i will see admin does not exist anymore')
def step_impl(context):
    br = context.browser
    br.get(context.get_url('/admin_overview/'))


@then('i will still see admin exist')
def step_impl(context):
    br = context.browser
    br.get(context.get_url('/admin_overview/'))




