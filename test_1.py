from testpage import OperationsHelper
import logging
import yaml
import time


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


# def test_step1(browser):
#     logging.info("Test1 Starting")
#     test_page = OperationsHelper(browser)
#     test_page.go_to_site()
#     test_page.enter_login("test")
#     test_page.enter_pass("test")
#     test_page.click_login_button()
#     assert test_page.get_error_text() == "401"
#
#
# def test_step_2(browser):
#     logging.info("Test2 starting")
#     test_page = OperationsHelper(browser)
#     test_page.go_to_site()
#     test_page.enter_login(testdata['login'])
#     test_page.enter_pass(testdata['password'])
#     test_page.click_login_button()
#     assert test_page.get_success_text() == f'Hello, {testdata["login"]}'


def test_step_3(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata['login'])
    test_page.enter_pass(testdata['password'])
    test_page.click_login_button()
    time.sleep(3)

    test_page.click_contact_us()
    time.sleep(3)

    test_page.enter_user_name("Эми")
    test_page.enter_user_email("mail@mail.ru")
    test_page.enter_user_text("Hello")
    time.sleep(1)

    test_page.click_contact_us()
    time.sleep(1)

    assert test_page.get_alert_text() == "Form successfully submitted"