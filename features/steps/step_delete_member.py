# file:features/steps/step_delete_member.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@when('i click delete on a member')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/member_delete/')


@when('i get redirect to a confirmation message that tells me if i am sure to delete the member')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/member_delete/')


@when('i see "foo","bar","sa@gmail.com","female","1990-02-01","2017-01-01","2017-06-03"')
def step_impl(context):
    br = context.browser
    br.get(context.get_url('/member_signup/'))
    br.find_element_by_name('first_name').send_keys('foo')
    br.find_element_by_name('last_name').send_keys('bar')
    br.find_element_by_name('email').send_keys('sa@gmail.com')
    br.find_element_by_name('gender').send_keys('female')
    br.find_element_by_name('date_of_birth').send_keys('1990-02-01')
    br.find_element_by_name('reg_date').send_keys('2017-01-01')
    br.find_element_by_name('end_date').send_keys('2017-06-03')


@when('i confirm delete')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit').click()


@when('i cancel the action')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit').click()


@then('i will see member does not exist anymore')
def step_impl(context):
    br = context.browser
    br.get(context.get_url('/member_overview/'))


@then('i will still see member exist')
def step_impl(context):
    br = context.browser
    br.get(context.get_url('/member_overview/'))




