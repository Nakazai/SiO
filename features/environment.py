from selenium import webdriver


def before_all(context):
    context.browser = webdriver.PhantomJS(executable_path=r'C:\PhantomJS\bin\phantomjs.exe')
    context.browser.implicitly_wait(1)
    context.server_url = 'http://localhost:8000'


def after_all(context):
    context.browser = webdriver.PhantomJS(executable_path=r'C:\PhantomJS\bin\phantomjs.exe')
    context.browser.set_window_size(1920, 1080)
    try:
        context.browser.get('http://127.0.0.1:8000/')

    except Exception:
        context.browser.get_screenshot_as_file('screenshot.png')

    context.browser.quit()


def before_feature(context, feature):
    pass




