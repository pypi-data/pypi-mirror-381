import logging

logger = logging.getLogger("scrippy.main")


class ScrippyApiError(Exception):
  """Specific error class."""

  def __init__(self, message):
    self.message = message
    super().__init__(self.message)
