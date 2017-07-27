from sanic import Sanic
from sanic.response import text, json

app = Sanic()


@app.route('/')
async def get_home(request):
    return text('Hello World')


@app.route('/hello', methods=['POST'])
async def post_hello(request):
    name = request.json['name']
    return json({'message': 'Hello, {0}'.format(name)})


def main():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
