from selenium import webdriver


def before_all(context):
    # PhantomJS is used there (headless browser - meaning we can execute tests in a command-line environment, which is what we want for use with SemaphoreCI
    # For debugging purposes, you can use the Firefox driver instead.

    context.browser = webdriver.PhantomJS(executable_path=r'C:\PhantomJS\bin\phantomjs.exe')
    context.browser.implicitly_wait(1)
    context.server_url = 'http://localhost:8000'


def after_all(context):
    # Explicitly quits the browser, otherwise it won't once tests are done
    context.browser = webdriver.PhantomJS(executable_path=r'C:\PhantomJS\bin\phantomjs.exe')
    context.browser.set_window_size(1920, 1080)
    try:
        context.browser.get('http://127.0.0.1:8000/')

    except Exception:
        # context.browser.save_screenshot('screenshot.png')
        context.browser.get_screenshot_as_file('screenshot.png')

    # context.browser.close()

    context.browser.quit()


def before_feature(context, feature):
    # Code to be executed each time a feature is going to be tested
    pass


# from features.browser import Browser
# from selenium import webdriver
# import SimpleHTTPServer
# import SocketServer
# import threading
#
#
# def before_all(context):
#     context.browser = Browser()
#     PORT = 8000
#     Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
#     context.server = SocketServer.TCPServer(("", PORT), Handler)
#     context.thread = threading.Thread(target=context.server.serve_forever)
#     context.thread.start()
#
#
# def after_all(context):
#     context.browser.close()
#     # shut down the web server
#     context.server.server_close()
#     context.thread.join()


# from features.browser import Browser
#
#
# def before_all(context):
#     context.browser = Browser()
#
#
# def after_all(context):
#     context.browser.close()
#     context.browser = None


# from __future__ import absolute_import
# import os
# import django
# from django.conf import settings
# from django.test.utils import get_runner
#
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'behave_dj.settings'
#
#
# def before_all(context):
#     if not settings.configured:
#         # from behave_dj import settings as _settings
#         settings.configure(DEBUG=True)
#     django.setup()
#     context.runner = get_runner(settings)()
#
#
# def before_scenario(context, scenario):
#     context.runner.setup_test_environment()
#     context.old_db_config = context.runner.setup_databases()
#     from django.test import Client
#     context.browser = Client()
#
#
# def after_scenario(context, scenario):
#     context.runner.teardown_databases(context.old_db_config)
#     context.runner.teardown_test_environment()


# from features.browser import Browser
# from selenium import webdriver
#
#
# def before_all(context):
#     context.browser = Browser()
#
#
# def after_all(context):
#     context.browser.close()

