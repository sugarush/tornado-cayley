from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

from cayley import CayleyABC


def encode(data):
    return json.dumps(data, separators=(',',':')).replace("</", "<\\/")

def decode(data):
    return json.loads(to_basestring(data))


class CayleyClient(CayleyABC):

    def initialize(self):
        self.client = AsyncHTTPClient()

    @gen.coroutine
    def fetch(self, path, **kargs):
        kargs['method'] = kargs.get('method', 'POST')
        request = HTTPRequest(self.url(path), **kargs)
        response = yield self.client.fetch(request, raise_error=False)
        raise gen.Return(response)

    @gen.coroutine
    def run(self, query):
        response = yield self.fetch('/query/gremlin', body=str(query))
        raise gen.Return(decode(response.body))

    @gen.coroutine
    def write(self, quads):
        self.validate_quads(quads)
        response = yield self.fetch('/write', body=encode(quads))
        raise gen.Return(decode(response.body))

    @gen.coroutine
    def delete(self, quads):
        self.validate_quads(quads)
        response = yield self.fetch('/delete', body=encode(quads))
        raise gen.Return(decode(response.body))
