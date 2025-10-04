from typing import Awaitable, Callable
import zmq # type: ignore
import asyncio
import inspect

from .BaseZQMServer import BaseZMQServer

class AsyncZMQServer(BaseZMQServer):
  async def handle_request(self, request: dict) -> dict:
    request = self._extract_data(request)
    handler = self._get_handler(request.path)
    middleware_chain = self.__prepare_middleware_chain(request, handler)
    return await middleware_chain()

  def __prepare_middleware_chain(
    self, 
    request: dict, 
    handler: Callable
  ) -> Callable[[], Awaitable[dict]]:
    async def next_middleware(index: int) -> dict:
      if index < len(self.middlewares):
        middleware = self.middlewares[index]
        async def next_func() -> dict:
          return await next_middleware(index + 1)
      
        if inspect.iscoroutinefunction(middleware):
          return await middleware(request, next_func)
        else:
          result = middleware(request, next_func)
          if inspect.iscoroutine(result):
              return await result
          return result
      else:
        if inspect.iscoroutinefunction(handler):
          return await handler(request)
        else:
          return handler(request)
        
    return lambda: next_middleware(0)
  
  async def run(self, address="tcp://127.0.0.1:5555"):
    self._bind(address, type="Async")
    while True:
      try:
        request = self._retrieve_data()
        response = await self.handle_request(request)
        self._send_response(response)
      except zmq.Again:
        await asyncio.sleep(0.001)
      except Exception as e:
        self._handle_exception(e)

