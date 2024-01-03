import pytest
from selenium.webdriver.common.by import By

from DataSet import test_data
from selenium import webdriver


@pytest.fixture(scope="class")
def browser_setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.get(test_data.Url)
    request.cls.driver = driver
    # request.cls.options = options;

    yield
    driver.close()
