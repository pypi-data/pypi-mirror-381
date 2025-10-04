class BaseException(Exception):
  def __init__(self, message: str, status_code: int, path: str):
    self.message = message
    self.status_code = status_code
    self.error_code = 'API_BASE_EXCEPTION'
    self.path = path