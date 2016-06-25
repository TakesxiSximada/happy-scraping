import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    """
    - GET
    - POST
    - PUT
    - PATCH
    - HEAD
    - DELETE
    """
    def get(self):
        self.set_header('receive', 'GET')
        self.write("receive GET")

    def post(self):
        self.set_header('receive', 'GET')
        self.write("receive POST")

    def put(self):
        self.set_header('receive', 'PUT')
        self.write("receive PUT")

    def patch(self):
        self.set_header('receive', 'PATCH')
        self.write("receive PATCH")

    def head(self):
        self.set_header('receive', 'HEAD (but head method is no body)')
        self.write("receive HEAD (but head method is no body)")

    def delete(self):
        self.set_header('receive', 'DELETE')
        self.write("receive DELETE")

    def options(self):
        self.set_header('receive', 'OPTIONS')
        self.write("receive OPTIONS")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
