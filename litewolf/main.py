import importlib.metadata
import argparse
import logging
import uvicorn

from .exit import exit_hook
from .logger import logger
from .api import srv


def _start(host: str ,port: int , debug=False):
  logger.setLevel(logging.DEBUG if debug else logging.INFO)

  exit_hook()

  logger.debug(f"address http://{host}:{port}/")
  logger.info("start serving")

  uvicorn.run(srv, host=host , port=port)



def main():
  parser = argparse.ArgumentParser()
  parser.usage = "\n  python -m " + __package__ +" [flags] [options]\nor:\n  poetry run app [flags] [options]" # type: ignore
  parser.add_argument("--debug", action="store_true",help="prints debug messages")
  parser.add_argument("-p","--port", type=int , default=8080,help="port number")
  parser.add_argument("--host", type=str , default="0.0.0.0",help="ip address")
  parser.add_argument("-v","--version", action="version", version= __package__ + " v" + importlib.metadata.version("litewolf")) #type: ignore

  args = parser.parse_args()

  _start(debug=args.debug, host=args.host , port=args.port)
