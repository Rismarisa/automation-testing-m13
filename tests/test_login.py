
import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import BASE_URL, TEST_USER, TEST_PASS
from config import BROWSER, HEADLESS
from pages.login_page import LoginPage


# Folder penyimpanan hasil pengujian
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


# Konfigurasi browser Selenium
@pytest.fixture
def driver():
    if BROWSER.lower() != "chrome":
        raise ValueError("Browser yang digunakan harus Chrome")

    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")

    browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(30)

    yield browser

    browser.quit()


# TC-01: Pengujian login dengan data benar
def test_login_valid(driver):
    page = LoginPage(driver)

    page.open_page(BASE_URL)
    page.login(TEST_USER, TEST_PASS)

    hasil = page.get_message()

    driver.save_screenshot(
        str(REPORT_DIR / "TC01_login_valid.png")
    )

    assert hasil == "Login berhasil!"


# TC-02: Pengujian dengan password salah
def test_login_invalid_password(driver):
    page = LoginPage(driver)

    page.open_page(BASE_URL)
    page.login(TEST_USER, TEST_PASS + "_salah")

    hasil = page.get_message()

    driver.save_screenshot(
        str(REPORT_DIR / "TC02_invalid_password.png")
    )

    assert hasil == "Username atau password salah!"


# TC-03: Pengujian dengan username salah
def test_login_invalid_username(driver):
    page = LoginPage(driver)

    page.open_page(BASE_URL)
    page.login(TEST_USER + "_salah", TEST_PASS)

    hasil = page.get_message()

    driver.save_screenshot(
        str(REPORT_DIR / "TC03_invalid_username.png")
    )

    assert hasil == "Username atau password salah!"


# TC-04: Pengujian username dan password salah
def test_login_invalid_credentials(driver):
    page = LoginPage(driver)

    page.open_page(BASE_URL)
    page.login(TEST_USER + "_salah", TEST_PASS + "_salah")

    hasil = page.get_message()

    driver.save_screenshot(
        str(REPORT_DIR / "TC04_invalid_credentials.png")
    )

    assert hasil == "Username atau password salah!"
