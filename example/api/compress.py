import gzip


def compress(app):
    @app.middleware('request')
    async def compress_request(request):
        if 'Content-Encoding' in request.headers:
            if request.headers['Content-Encoding'] == 'gzip':
                request.body = gzip.decompress(request.body)

    @app.middleware('response')
    async def compress_response(request, response):
        if 'Accept-Encoding' in request.headers:
            if 'gzip' in request.headers['Accept-Encoding']:
                compressed_body = gzip.compress(response.body)
                compressed_body_length = len(compressed_body)
                response.body = compressed_body
                response.headers['Content-Encoding'] = 'gzip'
                response.headers['Vary'] = 'Accept-Encoding'
                response.headers['Content-Length'] = compressed_body_length
