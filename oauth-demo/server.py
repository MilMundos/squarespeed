import json, requests

from urllib.parse import parse_qsl, urlencode
from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader

HOST = "localhost"
PORT = 8080
ENV = Environment(loader=FileSystemLoader("templates"))

with open("config.json", "r") as file:
    CONFIG = json.load(file)


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-type", "text/html")
        self.end_headers()

        if "redirect" in self.path:

            print("got temp authorization")
            print(self.path)

        else:
            template = ENV.get_template("index.html")
            self.wfile.write(template.render(client_id=CONFIG["client_id"]).encode())


with HTTPServer((HOST, PORT), Server) as httpd:
    print(f"starting server at {HOST}:{PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
