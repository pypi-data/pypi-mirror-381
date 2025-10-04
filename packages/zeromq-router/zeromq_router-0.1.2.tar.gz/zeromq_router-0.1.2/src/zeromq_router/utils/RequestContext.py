class RequestContext:
    def __init__(self, request: dict):
        self.request = request
        self._path = request.get('path', '/')
        self._data = request.get('data', {})

    @property
    def path(self) -> str:
        return self._path
    
    @property
    def data(self) -> dict:
        return self._data
    
    def get(self, key: str, default=None):
        return self._data.get(key, default)
