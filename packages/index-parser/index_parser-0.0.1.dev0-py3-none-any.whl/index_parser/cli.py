#!/usr/bin/env python
# coding=utf-8
# Stan 2021-05-31

import argparse

from .app import app

def main():
    parser = argparse.ArgumentParser(description="Parser tool")

    parser.add_argument('--host',
                        help="specify a host",
                        metavar="host")

    parser.add_argument('--port',
                        help="specify a port",
                        metavar="port")

    parser.add_argument('--debug',
                        action='store_true',
                        help="debug mode")

    args = parser.parse_args()
    params = {k: v for k, v in vars(args).items() if v}
    app.run(**params)
