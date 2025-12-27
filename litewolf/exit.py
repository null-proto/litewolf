import signal
import sys

from litewolf.logger import logger


def exit_hook():
  def handle_sigint(sig, frame):
    logger.info("CTRL+C caught, cleaning up…")
    sys.exit(0)

  signal.signal(signal.SIGINT, handle_sigint)
