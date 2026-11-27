# Implementasi Automation Testing + Environment Staging

## 1. Identitas Mahasiswa

- Nama: Risma Marisa
- NIM: 3224019Get-Item README.md | Select-Object Name,Length
- Semester: V (Lima)
- Institusi: STMIK Bandung
- Mata Kuliah: Implementasi dan Pengujian Perangkat Lunak
- Dosen Pengampu: Uro Abdurohim
- Tugas: Latihan Terstruktur Minggu 13

## 2. Deskripsi Project

Project ini dibuat untuk memenuhi tugas Minggu 13
mengenai implementasi automation testing dan
konfigurasi environment staging.

Aplikasi yang digunakan berupa sistem login sederhana
berbasis Python. Pengujian dilakukan menggunakan
Selenium dan PyTest untuk memastikan aplikasi dapat
menerima data login yang benar dan menolak data
login yang salah.

Pengujian menerapkan Page Object Model (POM),
virtual environment, variabel environment,
health check, dan mode headless.

## 3. Tujuan Pengujian

- Memastikan aplikasi dapat diakses.
- Memastikan fitur login berjalan sesuai skenario.
- Menguji penggunaan data login yang benar dan salah.
- Mengelola konfigurasi menggunakan file .env.
- Melakukan verifikasi kesiapan environment.
- Menerapkan automation testing melalui CI/CD.

## 4. Prasyarat

Software dan library yang digunakan:

| Software / Library | Versi |
|---|---|
| Python | 3.11.9 |
| Selenium | 4.54.0 |
| PyTest | 9.2.0 |
| Python-dotenv | 1.2.4 |
| Requests | 2.34.2 |
| Sistem Operasi Lokal | Windows 11 |
| Browser | Google Chrome |
| Code Editor | Visual Studio Code |
| Version Control | Git dan GitHub |

## 5. Struktur Project

    automation-testing-m13/
    ├── .github/
    │   └── workflows/
    ├── data/
    ├── pages/
    │   └── login_page.py
    ├── reports/
    ├── tests/
    │   └── test_login.py
    ├── .env.example
    ├── .gitignore
    ├── app.py
    ├── config.py
    ├── health_check.py
    ├── requirements.txt
    └── README.md

Folder reports menyimpan hasil pengujian lokal
dan dibuat kembali ketika pengujian dijalankan.

## 6. Langkah Instalasi

### Clone repository

    git clone https://github.com/Rismarisa/automation-testing-m13.git

    cd automation-testing-m13

### Membuat virtual environment

    py -3.11 -m venv venv

### Mengaktifkan virtual environment

    .\venv\Scripts\Activate.ps1

### Menginstal dependensi

    python -m pip install -r requirements.txt

## 7. Konfigurasi Environment

Salin file .env.example menjadi .env.

    Copy-Item .env.example .env

Sesuaikan konfigurasi berikut:

| Variabel | Fungsi |
|---|---|
| BASE_URL | Alamat aplikasi pengujian |
| TEST_USER | Username akun pengujian |
| TEST_PASS | Password akun pengujian |
| BROWSER | Browser yang digunakan |
| HEADLESS | Mengatur mode headless |

Gunakan BASE_URL berikut untuk pengujian lokal:

    http://127.0.0.1:8765

Isi TEST_USER dan TEST_PASS dengan kredensial
khusus pengujian. Gunakan chrome untuk BROWSER
dan true untuk HEADLESS.

File .env tidak diunggah ke GitHub karena
berisi konfigurasi dan kredensial pengujian.

## 8. Menjalankan Aplikasi

Jalankan perintah berikut pada terminal pertama:

    python app.py

Aplikasi dapat dibuka melalui:

    http://127.0.0.1:8765

Server harus tetap berjalan selama pengujian.

## 9. Menjalankan Health Check

Buka terminal kedua dan aktifkan virtual environment.

Jalankan perintah berikut:

    python health_check.py

Jika aplikasi siap digunakan, hasil pemeriksaan
menampilkan HTTP status code 200 dan status PASS.

Pengujian tidak dilanjutkan apabila health check gagal.

## 10. Menjalankan Automation Testing

Jalankan perintah berikut:

    python -m pytest tests/test_login.py -v --junitxml=reports/test-results.xml

Selenium akan menjalankan browser secara otomatis.
PyTest digunakan untuk memeriksa kesesuaian hasil
aktual dengan hasil yang diharapkan.

## 11. Hasil Pengujian Lokal

| ID | Skenario | Expected Result | Status |
|---|---|---|---|
| TC-01 | Username dan password benar | Login berhasil | PASSED |
| TC-02 | Password salah | Login ditolak | PASSED |
| TC-03 | Username salah | Login ditolak | PASSED |
| TC-04 | Username dan password salah | Login ditolak | PASSED |

Total pengujian: 4
Pengujian berhasil: 4
Pengujian gagal: 0
Persentase keberhasilan: 100%

Seluruh skenario berhasil dijalankan pada
environment lokal.

## 12. Laporan Pengujian

Hasil pengujian tersimpan dalam folder reports:

- TC01_login_valid.png
- TC02_invalid_password.png
- TC03_invalid_username.png
- TC04_invalid_credentials.png
- test-results.xml

Screenshot dihasilkan secara otomatis oleh Selenium,
sedangkan laporan XML dihasilkan oleh PyTest.

## 13. Deployment dan CI/CD

GitHub Actions digunakan untuk menjalankan pengujian
secara otomatis melalui trigger push dan pull request.

Konfigurasi sensitif dikelola menggunakan GitHub Secrets.
Browser dijalankan menggunakan mode headless.

Environment staging pada project ini merupakan
simulasi lingkungan pengujian yang terisolasi
di dalam runner GitHub Actions.

Status pipeline akan diperiksa setelah workflow
berhasil dikonfigurasi dan dijalankan.

## 14. Troubleshooting

### Python tidak terdeteksi

Gunakan Python Launcher:

    py -3.11 --version

### Pip belum terpasang

    py -3.11 -m ensurepip --upgrade

### Library tidak ditemukan

    python -m pip install -r requirements.txt

### Port 8080 tidak dapat digunakan

Pada saat implementasi ditemukan WinError 10013.
Masalah diatasi dengan mengganti port menjadi 8765
dan menyesuaikan konfigurasi BASE_URL.

### Health check mengalami timeout

Pada pengujian awal, health check mengalami timeout.
Server kemudian diubah dari HTTPServer menjadi
ThreadingHTTPServer agar dapat menangani beberapa
koneksi secara bersamaan.

Setelah perbaikan, health check berhasil mendapatkan
HTTP status code 200 dan status PASS.

### ChromeDriver gagal dijalankan

Pastikan Google Chrome tersedia dan koneksi internet
aktif agar Selenium Manager dapat menyiapkan driver.

## 15. Kesimpulan

Berdasarkan pengujian yang telah dilakukan, aplikasi
login memberikan respons sesuai dengan empat skenario
pengujian yang ditentukan.

Seluruh test case mendapatkan status PASSED pada
environment lokal. Penggunaan virtual environment,
Page Object Model, variabel environment, dan health
check membuat proses pengujian lebih terstruktur
dan mudah dijalankan kembali.

## 16. Referensi

- Uro Abdurohim. Materi Perkuliahan Minggu 13.
- https://www.selenium.dev/documentation/
- https://docs.pytest.org/
- https://docs.github.com/actions/
- https://pypi.org/project/python-dotenv/
- https://12factor.net/config

## 17. Repository GitHub

https://github.com/Rismarisa/automation-testing-m13
