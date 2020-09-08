from behave.fixture import use_fixture_by_tag

from pages.base_page import get_web

def before_all(context):
    web = get_web(context.config.userdata['browser'])
    context.web = web