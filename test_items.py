# test_items.py
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart_button(browser):
    # Открываем страницу
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    
    # Даем странице немного времени для загрузки
    time.sleep(30)
    
    # Проверяем наличие кнопки "Добавить в корзину"
    try:
        add_to_cart_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
        )
        assert add_to_cart_button.is_displayed(), "Add to cart button is not displayed."
    except Exception as e:
        pytest.fail(f"Test failed with error: {str(e)}")
