# file:features/steps/step_edit_admin.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('a overview of admins')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/InnsideSignUp/')


@when('i edit in "sara","bara","fb@gmail.com","leader","sara"')
# @when('i fill in and register the form')
def step_impl(context):
    # br = context.browser
    # context.browser('/cover/')
    # context.browser.select_form(nr=0)
    # context.browser.form['username'] = 'foo'
    # context.browser.form['password'] = 'bar'
    # context.browser.submit()

    # context.browser.visit('/')
    # username_field = context.browser.find_by_id('username')
    # password_field = context.browser.find_by_id('password')
    # username_field.send_keys('foo')
    # password_field.send_keys('bar')
    # submit_button = context.browser.find_by_id('submit')
    # submit_button.click()

    br = context.browser
    br.get(context.base_url + '/InnsideSignUp/')

    # Checks for Cross-Site Request Forgery protection input
    # assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('first_name').send_keys('sara')
    br.find_element_by_name('last_name').send_keys('bara')
    br.find_element_by_name('email').send_keys('fb@gmail.com')
    # br.find_element_by_name('association').send_keys('HiOA Salsa')
    br.find_element_by_name('union_position').send_keys('leader')
    br.find_element_by_name('username').send_keys('sara')


@when('i edit in "leader"')
# @when('i fill in and register the form')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/InnsideSignUp/')

    br.find_element_by_name('union_position').send_keys('leader')


@when('update the admin form')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit').click()


# @when('cancel the admin form')
# def step_impl(context):
#     br = context.browser
#     br.find_element_by_name('cancel').click()


# @then('i will see a success message')
@then('i will see the new admin added with correct information')
def step_impl(context):
    # br = context.browser
    # response = br.response()
    # assert response.code == 200
    # assert br.geturl().endswith('/dashboard/')

    # assert context.browser.response.code == 200
    # assert context.browser.endswith('/dashboard/')

    br = context.browser

    # Checks success status
    # assert br.current_url.endswith('/dashboard/')
    br.get(context.base_url + '/admin_overview/')
    # br.find_element_by_name('message')


# @then('i will be redirected to overview of all admins')
# def step_impl(context):
#     br = context.browser
#     br.get(context.base_url + '/admin_overview/')
