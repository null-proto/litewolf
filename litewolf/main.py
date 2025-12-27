import importlib.metadata
import argparse
import logging
import time

from .exit import exit_hook
from .logger import logger



def _start(debug=False):
  logger.setLevel(logging.DEBUG if debug else logging.INFO)

  exit_hook()

  logger.debug("hello world")
  logger.info("hello world")
  logger.warning("hello world")
  logger.error("hello world")
  logger.critical("hello world")
  time.sleep(2)


def main():
  parser = argparse.ArgumentParser()
  parser.usage = "\n  python -m " + __package__ +" [flags] [options]\nor:\n  poetry run app [flags] [options]" # type: ignore
  parser.add_argument("--debug", action="store_true",help="prints debug messages")
  parser.add_argument("-v","--version", action="version", version= __package__ + " v" + importlib.metadata.version("litewolf")) #type: ignore

  args = parser.parse_args()

  _start(debug=args.debug)
