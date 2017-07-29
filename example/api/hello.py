from sanic.blueprints import Blueprint
from sanic.response import json
from sanic_openapi import doc

blueprint = Blueprint('Hello', '/hello')


class HelloRequest:
    name = str


class HelloResponse:
    message = str


@blueprint.post('/')
@doc.summary('Gets a hello message')
@doc.consumes(HelloRequest, content_type='application/json')
@doc.produces(HelloResponse, content_type='application/json')
async def post_hello(request):
    name = request.json['name']
    return json({'message': 'Hello, {0}'.format(name)})
