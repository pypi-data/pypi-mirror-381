from typing import Callable

from .BaseZQMServer import BaseZMQServer

class ZMQServer(BaseZMQServer):
    def __prepare_middleware_chain(self, request: dict, handler: Callable) -> Callable:
        def next_middleware(index: int) -> Callable:
            if index < len(self.middlewares):
                def middleware_chain() -> dict:
                    return self.middlewares[index](request, next_middleware(index + 1))
                return middleware_chain
            else:
                def final_handler() -> dict:
                    return handler(request)
                return final_handler
        
        return next_middleware(0)
    
    def handle_request(self, request: dict) -> dict:
        request = self._extract_data(request)
        handler = self._get_handler(request.path)
        middleware_chain = self.__prepare_middleware_chain(request, handler)
        return middleware_chain()

    def run(self, address="tcp://127.0.0.1:5555"):
        self._bind(address, type="Sync")
        while True:
            try:
                request = self._retrieve_data()
                response = self.handle_request(request)
                self._send_response(response)
            except Exception as e:
                self._handle_exception(e)
