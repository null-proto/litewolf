import colorlog
import logging

_formatter = colorlog.ColoredFormatter(
  "%(time_log_color)s%(asctime)s%(reset)s %(log_color)s%(levelname)-8s%(reset)s %(message_log_color)s%(message)s%(reset)s",
  log_colors={
    "DEBUG": "cyan",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "red,bg_black",
  },
  secondary_log_colors={
    "time": {
      "DEBUG": "blue",
      "INFO": "blue",
      "WARNING": "blue",
      "ERROR": "blue",
      "CRITICAL": "purple",
    },
    "message": {
      "DEBUG": "white",
      "INFO": "white",
      "WARNING": "yellow",
      "ERROR": "red",
      "CRITICAL": "red",
    },
  },  # type: ignore
)

handler = colorlog.StreamHandler()
handler.setFormatter(_formatter)

logger = logging.getLogger()
logger.handlers = []
logger.addHandler(handler)
