from sanic import Sanic
from sanic.response import text
from sanic_openapi import doc
from sanic_openapi import swagger_blueprint, openapi_blueprint

from example.api.compress import compress
from example.api.hello import blueprint as hello_blueprint


app = Sanic()
app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)
app.blueprint(hello_blueprint)

app.config.API_VERSION = '0.0.1'
app.config.API_TITLE = 'Example API'
app.config.API_DESCRIPTION = 'Example API'
compress(app)


@app.get('/')
@doc.summary('Home')
@doc.produces(str, content_type='application/text')
async def get_home(request):
    return text('Hello World')


def main():
    app.run(port=8080)


if __name__ == '__main__':
    main()
