# file:features/steps/step_delete_admin.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


# @given('a overview of members')
# def step_impl(context):
#     br = context.browser
#     br.get(context.base_url + '/member_overview/')


@when('i click delete on a admin')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/admin_delete/')
    # br.find_element_by_name('submit').click()


@when('i get redirect to a confirmation message that tells me if i am sure to delete the admin')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/admin_delete/')
    # br.find_element_by_name('submit').click()


# @when('i edit "2017-06-03"')
# @when('i see "foo","bar","sa@gmail.com","female","1990-02-01","2017-01-01","2017-06-03" to confirm delete')
@when('i see "sara","bara","sa@gmail.com","leader","sara"')
# @when('i fill in and register the form')
def step_impl(context):
    br = context.browser
    # br.get(context.base_url + '/member_edit/')
    # br(context.get_url('member_edit'))
    br.get(context.get_url('/InnsideSignUp/'))

    # Checks for Cross-Site Request Forgery protection input
    # assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('first_name').send_keys('sara')
    br.find_element_by_name('last_name').send_keys('bara')
    br.find_element_by_name('email').send_keys('sa@gmail.com')
    br.find_element_by_name('union_position').send_keys('leader')
    br.find_element_by_name('username').send_keys('sara')


# @when('i confirm delete')
# def step_impl(context):
#     br = context.browser
#     br.find_element_by_name('submit').click()


# @when('i cancel the action')
# def step_impl(context):
#     br = context.browser
#     br.find_element_by_name('submit').click()


@then('i will see admin does not exist anymore')
def step_impl(context):
    br = context.browser
    br.get(context.get_url('/admin_overview/'))
    # br.find_element_by_name('reg_date').send_keys('2017-01-01')


@then('i will still see admin exist')
def step_impl(context):
    br = context.browser
    br.get(context.get_url('/admin_overview/'))
    # br.find_element_by_name('reg_date').send_keys('2017-01-01')

