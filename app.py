import tornado.web
import tornado.ioloop
import tornado.gen
from tornado import httpclient
from tornado import curl_httpclient
import tornadoredis
import settings as conf
import random


c = tornadoredis.Client()
c.connect()

current_jobs = {}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        pass

class JobHandler(tornado.web.RequestHandler):
    def get(self):
        pass

class AddPhoneHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, *args, **kwargs):
        pass


NOT_FOUND_HTML_PATTERN = u'Пользователь не найден'
FOUND_HTML_PATTERN = u'Если это не Вы,' #<span class="ii_label explain">Если это не Вы, <a href="/restore?rh=99fe2e6ba12c7d2c45">нажмите здесь »</a></span>
INPUT_HTML_PATTERN = u'name="login"'
CAPTCHA_HTML_PATTERN = u"Введите код с картинки"

class Application(tornado.web.Application):
    @tornado.gen.engine
    def period_call(self):
        foo = yield tornado.gen.Task(c.sadd, "key", "%i"%random.randint(1,10000))
        bar = yield tornado.gen.Task(c.scard, "key")
        print bar
        def handler(response):
            print response
        http_client = curl_httpclient.CurlAsyncHTTPClient()
        # http_client = httpclient.AsyncHTTPClient()
        http_client.fetch("http://m.vk.com/restore",handler)

    def http_client_handler(self, response):
        if response.error:
            pass
        else:
            body = response.body
            if INPUT_HTML_PATTERN in body:
                pass


app = Application([
              (r"/", MainHandler),
], debug=True)
ioloop = tornado.ioloop.IOLoop.instance()
period_loop = tornado.ioloop.PeriodicCallback(
                                                    app.period_call,
                                                    getattr(conf,"PERIOD_CALL_TIME",1000),
                                                    ioloop
                                                )


if __name__ == "__main__":
    app.listen(8888)
    period_loop.start()
    ioloop.start()