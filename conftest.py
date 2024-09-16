# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Set language for browser')

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    chrome_options = Options()
    chrome_options.add_argument(f'--lang={language}')
    
    # Path to your chromedriver executable
    chrome_service = ChromeService(executable_path='/path/to/chromedriver')
    
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield browser
    browser.quit()
