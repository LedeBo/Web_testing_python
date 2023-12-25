from conftest import testdata
from testpage import OperationsHelper
import logging
import time
import yaml

with open("./testdata.yaml") as f:
    data = yaml.safe_load(f)
    browser = testdata["browser"]


def test_step1(browser):
    logging.info("Test1 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login("test")
    test_page.enter_pass("test")
    test_page.click_login_button()
    time.sleep(3)
    assert test_page.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata['login'])
    test_page.enter_pass(testdata['password'])
    test_page.click_login_button()
    time.sleep(2)
    assert test_page.get_profile_text() == f"Hello, GB2023090a58615"


def test_step3(browser):
    logging.info("Test3 Starting")
    test_page = OperationsHelper(browser)
    test_page.click_to_do_new_post()
    test_page.enter_title("Hello, world")
    test_page.click_save_post_button()
    time.sleep(5)
    assert test_page.get_title_text() == "Hello, world"




def test_step4(browser):
    logging.info("Test4 Starting")
    test_page = OperationsHelper(browser)
    test_page.click_contact_button()
    test_page.enter_name("Amy")
    test_page.enter_email("amy@mail.ru")
    test_page.enter_contact_content("my contact")
    test_page.contact_us_save_button()
    time.sleep(3)
    assert test_page.get_alert_text() == "Form successfully submitted"