
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Lokasi elemen pada halaman login
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    MESSAGE = (By.ID, "message")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Membuka halaman login
    def open_page(self, base_url):
        self.driver.get(base_url)

    # Memasukkan username
    def input_username(self, username):
        element = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        element.clear()
        element.send_keys(username)

    # Memasukkan password
    def input_password(self, password):
        element = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        element.clear()
        element.send_keys(password)

    # Menekan tombol login
    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    # Menjalankan proses login
    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()

    # Mengambil pesan hasil login
    def get_message(self):
        self.wait.until(
            lambda driver: driver.find_element(
                *self.MESSAGE
            ).text.strip() != ""
        )
        return self.driver.find_element(*self.MESSAGE).text
