import importlib.metadata


def main():
  print('hello world '+ '(v ' + importlib.metadata.version("litewolf") + ')' )
