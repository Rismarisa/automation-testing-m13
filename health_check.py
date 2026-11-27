import requests
from config import BASE_URL


def health_check():
    url = f"{BASE_URL.rstrip('/')}/health"

    print("=" * 50)
    print("VERIFIKASI ENVIRONMENT - HEALTH CHECK")
    print("=" * 50)
    print("Nama : Risma Marisa")
    print("NIM  : 3224019")
    print("-" * 50)
    print("Target URL  :", url)

    try:
        response = requests.get(url, timeout=10)

        print("Status Code :", response.status_code)

        if (response.status_code == 200
                and response.json().get("status") == "healthy"):
            print("Response    :", response.text)
            print("Status      : PASS")
            print("Keterangan  : Aplikasi siap diuji.")
            return True

        print("Status      : FAIL")
        print("Keterangan  : Aplikasi belum siap diuji.")
        return False

    except (requests.RequestException, ValueError) as error:
        print("Status      : FAIL")
        print("Error       :", error)
        return False

    finally:
        print("=" * 50)


if __name__ == "__main__":
    if not health_check():
        raise SystemExit(1)
