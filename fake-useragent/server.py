# -*- coding: utf-8 -*-
import sys
import argparse

import ipdb
from tornado.ioloop import IOLoop
from tornado.web import (
    Application,
    RequestHandler,
)


class DebugHandler(RequestHandler):
    def get(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def head(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def post(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def delete(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def patch(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def put(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def options(self, *args, **kwds):
        ipdb.set_trace()
        pass


def make_app():
    return Application([
        (r"(.*)", DebugHandler),
    ])


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8000)
    args = parser.parse_args(argv)

    app = make_app()
    app.listen(args.port)

    mainloop = IOLoop.current()
    mainloop.start()

if __name__ == '__main__':
    sys.exit(main())
