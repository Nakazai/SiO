# file:features/steps/step_edit_member.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('a overview of members')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/member_overview/')


@when('i click on update')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/member_edit/')


@when('i edit in "foo","bar","sa@gmail.com","1990-02-01","2017-01-01","2017-06-03"')
def step_impl(context):
    br = context.browser
    br.get(context.get_url('/member_signup/'))
    br.find_element_by_name('first_name').send_keys('foo')
    br.find_element_by_name('last_name').send_keys('bar')
    br.find_element_by_name('email').send_keys('sa@gmail.com')
    br.find_element_by_name('date_of_birth').send_keys('1990-02-01')
    br.find_element_by_name('reg_date').send_keys('2017-01-01')
    br.find_element_by_name('end_date').send_keys('2017-06-03')


@when('update the form')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit').click()


@when('i fill in "2017-01-01"')
def step_impl(context):
    br = context.browser
    br.get(context.get_url('/member_signup/'))
    br.find_element_by_name('reg_date').send_keys('2017-01-01')


@when('cancel the form')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('cancel').click()


@then('i will see the new member added with correct email')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/member_overview/')





