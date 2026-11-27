from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from config import TEST_USER, TEST_PASS


# Tampilan halaman login
def login_page(message=""):
    return f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <title>Automation Testing M13</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #edf2f7;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }}

            .container {{
                background: white;
                padding: 35px;
                width: 350px;
                border-radius: 12px;
                box-shadow: 0 4px 15px #0002;
            }}

            h2 {{
                color: #234567;
                text-align: center;
            }}

            input {{
                width: 100%;
                padding: 12px;
                margin: 8px 0 16px;
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}

            button {{
                width: 100%;
                padding: 12px;
                background: #234567;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}

            #message {{
                text-align: center;
                font-weight: bold;
                color: #234567;
            }}

            footer {{
                text-align: center;
                font-size: 12px;
                color: #777;
                margin-top: 25px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Login System</h2>
            <p style="text-align:center">
                Automation Testing Minggu 13
            </p>

            <form action="/login" method="POST">
                <label>Username</label>
                <input type="text" id="username"
                       name="username" required>

                <label>Password</label>
                <input type="password" id="password"
                       name="password" required>

                <button type="submit" id="login-button">
                    Login
                </button>
            </form>

            <p id="message">{message}</p>

            <footer>
                Risma Marisa | 3224019<br>
                STMIK Bandung
            </footer>
        </div>
    </body>
    </html>
    """


class LoginHandler(BaseHTTPRequestHandler):

    def send_content(self, content, content_type, status=200):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

    # Menampilkan halaman dan health check
    def do_GET(self):
        if self.path == "/health":
            self.send_content(
                '{"status": "healthy"}',
                "application/json"
            )

        elif self.path == "/":
            self.send_content(
                login_page(),
                "text/html; charset=utf-8"
            )

        else:
            self.send_error(404)

    # Memproses data login
    def do_POST(self):
        if self.path != "/login":
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        data = parse_qs(body)

        username = data.get("username", [""])[0]
        password = data.get("password", [""])[0]

        if username == TEST_USER and password == TEST_PASS:
            message = "Login berhasil!"
        else:
            message = "Username atau password salah!"

        self.send_content(
            login_page(message),
            "text/html; charset=utf-8"
        )


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8765), LoginHandler)

    print("=" * 50)
    print("AUTOMATION TESTING - MINGGU 13")
    print("=" * 50)
    print("Nama   : Risma Marisa")
    print("NIM    : 3224019")
    print("Server : http://127.0.0.1:8765")
    print("Health : http://127.0.0.1:8765/health")
    print("Status : Server berhasil dijalankan")
    print("=" * 50)
    print("Tekan Ctrl+C untuk menghentikan server.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dihentikan.")
    finally:
        server.server_close()
