import pytest
from selenium import webdriver
import os

@pytest.fixture
def browser():
    """Opens Google Chrome driver and closes it at the end of each test"""
    print("Open Google Chrome")
    driver = webdriver.Chrome()
    yield driver
    print("Close Google Chrome")
    driver.quit()

@pytest.fixture
def screenshot_on_failure(request, browser):
    """Takes a screenshot if a test fails and sends it into the screenshots directory"""
    yield
    if request.session.testsfailed:
        test_name = request.node.name
        screenshot_dir = os.path.join(os.path.dirname(__file__), "../screenshots")
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_screenshot.png")
        browser.save_screenshot(screenshot_path)
