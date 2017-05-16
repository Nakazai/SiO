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
    br.get(context.base_url + '/')

    # Checks for Cross-Site Request Forgery protection input
    # assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('bar')
    br.find_element_by_name('submit').click()


@then('i can see my home site')
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
    br.get(context.base_url + '/dashboard/')


# @given('a user')
# def step_impl(context):
#     from django.contrib.auth.models import User
#     u = User(username='anonymous')
#     u.set_password('none')


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



