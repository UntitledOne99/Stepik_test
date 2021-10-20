import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox}

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',help="Choose browser: chrome or firefox")
    parser.addoption('--language',action='store', default='Ru',help="Choose language: Ru or En")
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name in supported_browsers:
        #browser = supported_browsers.get(browser_name)()
        if browser_name == 'chrome':
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            browser = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", user_language)
            browser = webdriver.Firefox(firefox_profile=fp)
        print(f"\nusing {user_language} language for test..")
        print(f"\nstart {browser_name} browser for test..")
    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser..")
    browser.quit()