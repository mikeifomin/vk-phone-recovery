import tornado.web
import tornado.ioloop
from tornado import curl_httpclient

class MainHandler(tornado.web.RequestHandler):
    pass
app = tornado.web.Application([
              (r"/",)
],debug=True)


if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()