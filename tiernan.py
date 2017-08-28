#!/usr/bin/python3
from run_sslscan import scan
import cherrypy
from ansi2html import Ansi2HTMLConverter

ansi_converter = Ansi2HTMLConverter()
cherrypy.config.update({'server.socket_host': '0.0.0.0'})

class Tiernan(object):
    @cherrypy.expose
    def index(self):
        request_form = """
        <form action="/doScan" method="get">
        Site to scan: <input type="text" name="target_site" size="50"><br>
        <input type="submit" value="Submit">
        </form>

        """
        return request_form

    @cherrypy.expose
    def doScan(self, target_site):
        scan_results = scan(target_site)
        html = ansi_converter.convert(scan_results)
        return html

if __name__ == '__main__':
    cherrypy.quickstart(Tiernan())
