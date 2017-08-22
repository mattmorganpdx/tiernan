#!/usr/bin/python3
from run_sslscan import scan
from flask import Flask, request, Response
from ansi2html import Ansi2HTMLConverter

app = Flask(__name__)
ansi_converter = Ansi2HTMLConverter()


@app.route("/", methods=['GET'])
def get_scan():
    request_form = """
    <form action="/" method="post">
    Site to scan: <input type="text" name="target_site" size="50"><br>
    <input type="submit" value="Submit">
    </form>

    """
    return request_form


@app.route("/", methods=['POST'])
def run_scan():
    target = request.form.get('target_site')

    def generate():
        yield "<br/>"
        # This generate sends something back to the browser to avoid timeouts on the POST.
        # If the time bought by the single <br/> were to be exceeded this would need to be rewritten.
        # if subprocess Popen were used instead of run then you could stream back data while waiting on the scan.
        # This caused me a problem AFTER I dockerized sslscan and might have "gone away" now that it's all dockerized.
        scan_results = scan(target)
        html = ansi_converter.convert(scan_results)
        yield html
    return Response(generate())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
