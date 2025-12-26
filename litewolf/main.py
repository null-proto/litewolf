import importlib.metadata
import argparse
import logging

import litewolf.exit
import time

from litewolf.logger import logger

VERSION = "litewolf v" + importlib.metadata.version("litewolf")


def _start(debug=False):
  logger.setLevel(logging.DEBUG if debug else logging.INFO)

  litewolf.exit.exit_()

  logger.debug("hello world")
  logger.info("hello world")
  logger.warning("hello world")
  logger.error("hello world")
  logger.critical("hello world")
  time.sleep(2)


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--debug", action="store_true")
  parser.add_argument("--version", action="version", version=VERSION)

  args = parser.parse_args()

  _start(debug=args.debug)
