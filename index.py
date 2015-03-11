#-*- coding:utf-8 -*-

import markdown
import os.path
import tornado.options
import tornado.web
import tornado.wsgi
import torndb

class Application(tornado.wsgi.WSGIApplication):
    def __init__(self):
        template_path=os.path.join(os.path.dirname(__file__), "templates")
        static_path=os.path.join(os.path.dirname(__file__), "static")
        settings = {
            "login_url": "/auth/login",
            "cookie_secret": "CkwXIkG6RXs15skVeMBhdbJKt0QSqk1tivD1smsr98Y=",
            "template_path":template_path,
            "static_path":static_path,
            "debug":True,
        }
        handlers=[
            (r'/',HomePageHandler),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
    # def initialize(self):
    #     host = "sqld.duapp.com:4050"
    #     user = "kDHlBFpj7cCPFF4K8jH5ojBC"
    #     password = "BKoBwnVdwUYq3d0mFZdRBGhupoatb6w7"
    #     dbname = "iCzzQzlDivOZbTlFgFay"
    #     self.db=torndb.Connection(host, dbname,user,password)

    def get(self):
        self.write_error(404)

    def get_current_user(self):
        return self.get_secure_cookie("username")

class HomePageHandler(BaseHandler):
    def get(self):
        self.render("index.html")


from bae.core.wsgi import WSGIApplication
application = WSGIApplication(Application())
