# file:features/steps/step_add_member.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('a member form')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/member_signup/')


@when('i fill in "foo","bar","fb@gmail.com","female","1990-02-01","2017-01-01","2017-06-03"')
def step_impl(context):

    br = context.browser
    br.get(context.base_url + '/member_signup/')
    br.find_element_by_name('first_name').send_keys('foo')
    br.find_element_by_name('last_name').send_keys('bar')
    br.find_element_by_name('email').send_keys('fb@gmail.com')
    br.find_element_by_name('gender').send_keys('female')
    br.find_element_by_name('date_of_birth').send_keys('1990-02-01')
    br.find_element_by_name('reg_date').send_keys('2017-01-01')
    br.find_element_by_name('end_date').send_keys('2017-06-03')


@when('register the member form')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit').click()


@when('cancel the member form')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('cancel').click()


@then('i will see the new member added')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/member_overview/')


@then('i will be redirected to overview of all members')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/member_overview/')




