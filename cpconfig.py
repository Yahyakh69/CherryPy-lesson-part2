import cherrypyimport os,os.path_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))class Root:       _cp_config = {'tools.gzip.on': True}       @cherrypy.expose       def index(self):           _header ="""<html>                 <head>                                 <link rel="stylesheet" type="text/css" href="/style.css"></link>                </head>              <body>              <h3> Hello</h3>              <a href=default>click here</a>                                </body>           </html>                  """                             return _header                                        @cherrypy.expose       def default(self):           return ("<h3>How you doing ? </h3>"," <a href=hello> click here </a>")       @cherrypy.expose              @cherrypy.tools.gzip()       def nothing(self, msg):           return msg       @cherrypy.expose       def hello(self):           return "Ok,Bye"       hello._cp_config = {'tools.gzip.on': False}              if __name__ == '__main__':             conf = {           'global': {                        'server.socket_host': 'localhost',                       'server.socket_port': 8080,                     },                  '/style.css': {               'tools.staticfile.on': True,               'tools.staticfile.filename': os.path.join(_curdir,'style.css')          } }             cherrypy.quickstart(Root(),'/', config=conf)                                                                                                                                                                                          