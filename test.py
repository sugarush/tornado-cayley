from tornado.testing import AsyncTestCase, gen_test

from tornado_cayley import CayleyClient, InvalidQuad, decode

class TestCayley(AsyncTestCase):

    def setUp(self):
        super(TestCayley, self).setUp()
        self.cayley = CayleyClient()

    def test_url(self):
        url = self.cayley._url('/write')
        self.assertEqual(url, 'http://localhost:64210/api/v1/write')

    @gen_test
    def test_fetch(self):
        response = yield self.cayley._fetch('/query/gremlin', body='g.V()', method='POST')
        self.assertDictEqual({ 'result': None }, decode(response.body))

    @gen_test
    def test_write_delete(self):
        quad = {
            'object': 'cayley',
            'predicate': 'has',
            'subject': 'nodes'
        }
        response = yield self.cayley.write_batch([quad])
        self.assertDictEqual({'result': 'Successfully wrote 1 quads.'}, response)

        response = yield self.cayley.delete_batch([quad])
        self.assertDictEqual({'result': 'Successfully deleted 1 quads.'}, response)

        del(quad['object'])

        tested = False
        try:
            response = yield self.cayley.delete_batch([quad])
        except Exception, e:
            self.assertIsInstance(e, InvalidQuad)
            tested = True

        self.assertTrue(tested)

    @gen_test
    def test_run(self):
        query = self.cayley.graph.V('alice').All()
        quad = {
            'object': 'alice',
            'predicate': 'knows',
            'subject': 'bob'
        }
        yield self.cayley.write_batch([quad])
        response = yield self.cayley.run(query)
        self.assertDictEqual({'result': [{'id': 'alice'}]}, response)
        yield self.cayley.delete_batch([quad])
