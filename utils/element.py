import config.settings as default_settings
from playwright._impl._locator import Locator
from playwright.sync_api import expect
import inspect

def wait_for(locator, state='visible', timeout=default_settings.DEFAULT_ELEMENT_WAIT):
    # https://playwright.dev/python/docs/api/class-locator#locator-wait-for
    if(locator):
        print("Waiting for locator : {}".format(locator))
        locator.wait_for(state=state, timeout=timeout)
    else:
        print("Not a locator that sent to perform wait_for : {}".format(locator))

def click(locator):
    if(locator):
        wait_for(locator)
        print("Clicking on locator : {}".format(locator))
        locator.click()
    else:
        print("Not a locator that sent to perform click with selector: {}".format(locator))

def fill(locator, value):
    if(locator):
        wait_for(locator)
        print("Fill value: {}, at locator : {}".format(value, locator))
        locator.fill(value)
    else:
        print("Not a locator that sent to perform click with selector: {}".format(locator))


def press(locator, value):
    if(locator):
        wait_for(locator)
        print("Press '{}' action at {}".format(value, locator))
        locator.press(value)
    else:
        print("Not a locator that sent to perform click with selector: {}".format(locator))

def expect_to_be_visible(locator):
    if(locator):
        wait_for(locator)
        print("Expect to be visible locator: {}".format(locator))
        expect(locator).to_be_visible()
    else:
        print("Not a locator that sent to perform expect_to_be_visible with selector: {}".format(locator))