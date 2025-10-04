from typing import Dict, Callable, Any, List, Protocol, TypedDict, Optional, Union

class RequestDict(TypedDict, total=False):
    path: str
    method: str
    data: Dict[str, Any]

class ContextDict(TypedDict, total=False):
    request: RequestDict
    path: str
    data: Dict[str, Any]
    metadata: Dict[str, Any]

class ResponseDict(TypedDict, total=False):
    message: str
    status: int
    data: Any


NextFunction = Callable[[], ResponseDict]
MiddlewareFunction = Callable[[ContextDict, NextFunction], ResponseDict]
RouteHandler = Callable[[ContextDict], ResponseDict]