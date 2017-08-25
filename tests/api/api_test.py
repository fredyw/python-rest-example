import gzip
import json

from example.api.api import app


def test_get_home():
    request, response = app.test_client.get('/')
    assert 200 == response.status
    assert 'Hello World' == response.text


def test_post_hello():
    json_request = {
        'name': 'Foo'
    }
    request, response = app.test_client.post('/hello',
                                             data=json.dumps(json_request))
    assert 200 == response.status
    json_response = json.loads(response.text)
    assert 'Hello, Foo' == json_response['message']


def test_post_hello_compressed():
    json_request = {
        'name': 'Foo'
    }
    compressed_json = gzip.compress(bytes(json.dumps(json_request), 'utf-8'))
    request, response = app.test_client.post('/hello',
                                             data=compressed_json,
                                             headers={
                                                 'Content-Type': 'application/json',
                                                 'Content-Encoding': 'gzip',
                                                 'Accept-Encoding': 'gzip',
                                                 'Content-Length': str(len(compressed_json))
                                             })
    assert 200 == response.status
    json_response = json.loads(response.text)
    assert 'Hello, Foo' == json_response['message']
