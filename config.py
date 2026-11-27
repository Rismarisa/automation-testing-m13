import os
from dotenv import load_dotenv

# Membaca file .env
load_dotenv()

# Mengambil konfigurasi environment
BASE_URL = os.getenv("BASE_URL")
TEST_USER = os.getenv("TEST_USER")
TEST_PASS = os.getenv("TEST_PASS")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

# Memeriksa kelengkapan konfigurasi
if not BASE_URL or not TEST_USER or not TEST_PASS:
    raise ValueError("Konfigurasi environment belum lengkap!")

# Menampilkan hasil konfigurasi
if __name__ == "__main__":
    print("=" * 45)
    print("KONFIGURASI ENVIRONMENT TESTING")
    print("=" * 45)
    print("Nama       : Risma Marisa")
    print("NIM        : 3224019")
    print("-" * 45)
    print("BASE_URL   :", BASE_URL)
    print("TEST_USER  :", TEST_USER)
    print("TEST_PASS  :", "********")
    print("BROWSER    :", BROWSER)
    print("HEADLESS   :", HEADLESS)
    print("-" * 45)
    print("Status     : Konfigurasi berhasil dibaca")
    print("=" * 45)
