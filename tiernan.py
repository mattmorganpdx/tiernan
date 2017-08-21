from run_sslscan import scan
from flask import Flask, request, session
from ansi2html import Ansi2HTMLConverter
import time
import os
from datetime import timedelta

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(seconds=30)
app.secret_key = os.urandom(24)
ansi_converter = Ansi2HTMLConverter()


@app.route("/", methods=['GET'])
def get_scan():
    session.permanent = True
    request_form = """
    <form action="/" method="post">
    Site to scan: <input type="text" name="target_site"><br>
    <input type="submit" value="Submit">
    </form>

    """
    return request_form


@app.route("/", methods=['POST'])
def run_scan():
    print(time.time())
    target = request.form.get('target_site')
    scan_results = scan(target)
    html = ansi_converter.convert(scan_results)
    print(time.time())
    return html
