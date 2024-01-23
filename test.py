import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--remote-debugging-pipe')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_pay(driver):
    try:
        driver.get("https://finance.dev.fabrique.studio/")



        add_payment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button--state-filled') and contains(., 'Добавить платёж')]"))
        )
        add_payment_button.click()

        try:
            element_to_check = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='checkbox__label' and text()='Доход/приход']"))
            )
            print("Элемент найден.")
            
            element_to_check.click()

            input_field = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//textarea[contains(@class, 'input__input')]"))
            )
            input_field.send_keys("Тестовые данные")

            save_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@form='idwm0cd' and contains(@class, 'button--state-filled') and contains(@class, 'button--size-sm')]"))
            )
            save_button.click()

        except Exception as e:
            print("Элемент не найден. Ошибка:", e)

    finally:
        # Закрытие браузера
        driver.quit()
if __name__ == "__main__":
    pytest.main([__file__])