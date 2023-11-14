from utilities.main import BaseDriver

def before_scenario(context, scenario):
    context.driver = BaseDriver()
    context.driver.browse_open()


def after_scenario(context, scenario):
    context.driver.closed_browser()
