# from sched import scheduler
# from time import time, sleep


class Message:
  def __init__(self):
    self._message = ""
    self._score = 0

  def get_message(self):
    """Gets the banner message.
    
    Returns:
      string: The message.
    """
    return self._message
    
  def set_message(self, message):
    """Updates the banner message.
    
    Args:
      message (string): The given message.
    """
    self._message = message

  def reset_message(self, seconds):
    """Resets the message to empty string after certain amount of time.
    """
    # seconds = sleep(30 - time() % 60)

    # schedule.every(seconds).minute.do(self.set_message(""))
    # sleep(60 - time() % 10)
    # self.set_message("")

