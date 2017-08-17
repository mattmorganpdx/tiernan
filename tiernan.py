from run_sslscan import scan
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_scan():
    request_form = """
	<form action="/" method="post">
     Site to scan: <input type="text" name="target_site"><br>
    <input type="submit" value="Submit">
    </form>

    """
    return request_form

@app.route("/", methods=['POST'])
def run_scan():
    target = request.form.get('target_site')
    return "<pre>{}</pre>".format(scan(target))
