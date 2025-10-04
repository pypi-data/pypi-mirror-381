import json
import zmq

from typing import Dict, Callable, Any

from ..utils.RequestContext import RequestContext
from ..utils.index import MiddlewareFunction, RouteHandler

from ..exceptions.NotFoundException import NotFoundException 
from ..exceptions.InvalidHandlerException import InvalidHandlerException
from ..exceptions.BaseException import BaseException

class BaseZMQServer:
  def __init__(self):
    self.routes: Dict[str, Dict[str, Callable]] = {}
    self.context = zmq.Context()
    self.socket = self.context.socket(zmq.REP)
    self.error_handler: Callable[[Exception], Any] | None = None
    self.middlewares = []

  def register_error_handler(self, handler: Callable[[BaseException], Any]):
    self.error_handler = handler

  def route(self, path: str) -> Callable[[RouteHandler], RouteHandler]:
    def decorator(func: RouteHandler) -> RouteHandler:
      self.routes[path] = func
      return func
    return decorator
  
  def use(self, func: MiddlewareFunction) -> MiddlewareFunction:
      """Add middleware function"""
      self.middlewares.append(func)
      return func

  def _bind(self, address="tcp://127.0.0.1:5555", type=""):
    self.socket.bind(address)
    print(f" {type} ZMQ Router bound to {address} ")
    print(f" {type} ZMQ Server is listening on {address} ")

  def _get_handler(self, path: str) -> Callable:
    if path not in self.routes:
      raise NotFoundException(path=path)
    
    handler = self.routes[path]

    if not callable(handler):
      raise InvalidHandlerException(path=path)
    
    return handler
  
  def _extract_data(self, request: dict) -> RequestContext:
    return RequestContext(request)
  
  def _retrieve_data(self) -> dict:
    message = self.socket.recv_string(zmq.NOBLOCK)
    return json.loads(message)

  def _send_response(self, response: dict):
    self.socket.send_string(json.dumps(response))

  def _handle_exception(self, e: Exception):
    if self.error_handler:
      self.error_handler(e, self)
      return
    
    if isinstance(e, BaseException):
      self._send_response({
        "error": e.message,
        "status": e.status_code,
        "error_code": e.error_code,
        "path": e.path
      })
    elif isinstance(e, json.JSONDecodeError):
      self._send_response({
        "error": "Invalid JSON",
        "error_code": "INVALID_JSON",
        "status": 400
      })
    elif isinstance(e, KeyboardInterrupt):
      print("Gracefully shutting down server... ")
      self.socket.close()
      self.context.term()
      exit(0)
    else:
      self._send_response({
        "error": str(e),
        "error_code": "INTERNAL_SERVER_ERROR",
        "status": 500
      })