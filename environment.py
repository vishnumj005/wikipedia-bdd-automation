from config.browser.driverfactory import Driver


def before_all(context):
    context.env = context.config.userdata['url']
    context.mode = context.config.userdata['mode']


def before_scenario(context, scenario):
    if context.config.userdata['browser'] in ["chrome", "firefox", "edge", "safari"]:
        context.browser = context.config.userdata['browser']
    else:
        context.browser = "chrome"

    driver_instance = Driver(context)
    context.driver = driver_instance.get_driver()
    context.driver.delete_all_cookies()


def after_scenario(context, scenario):
    context.driver.quit()
