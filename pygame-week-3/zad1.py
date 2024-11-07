class Response:

    def __init__(self, res: str) -> None:
        self.res = res

    def __str__(self) -> str:
        return self.res

class Request:

    def __init__(self, req: str, is_admin=False):
        self.req = req 
        self.is_admin = is_admin

    def __str__(self):
        return self.req

class WebEndpoint():

    def serve_request(self, request: Request):
        res = Response('Response for ' + request.req)
        return res 
    

class CompressedWebEndpointDecorator(WebEndpoint):

    def __init__(self, endpoint: WebEndpoint, compression_algorithm='LZ77') -> None:
        self._endpoint = endpoint
        self.compression_algorithm = compression_algorithm

    def serve_request(self, request: Request):
        res = self._endpoint.serve_request(request)
        res.res = f'Compressed ({res.res}) with {self.compression_algorithm}'

        return res

    

if __name__ == '__main__':
    we = CompressedWebEndpointDecorator(WebEndpoint(), 'zip')
    req = Request('video')
    print(we.serve_request(req))
