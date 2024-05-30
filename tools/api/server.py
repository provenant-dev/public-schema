# -*- encoding: utf-8 -*-
"""
schema registry server module

"""
import argparse

import falcon
from hio.base import doing
from hio.core import http
from api.app import serving

parser = argparse.ArgumentParser(description="Runs schema registry api server")
parser.add_argument('-p', '--http',
                    action='store',
                    default=7723,
                    help="Port on which to serve schema SADs.  Defaults to 7723")

parser.add_argument('-r', '--registry-file',
                    action='store', dest="registryFile",
                    required=True,
                    help="Path of schema registry.json file")


def launch(args):
    app = falcon.App()
    server = http.Server(port=int(args.http), app=app)
    if not server.reopen():
        raise RuntimeError(f"cannot create http server on port {int(args.http)}")
    httpServerDoer = http.ServerDoer(server=server)

    serving.loadEnds(app, registryFile=args.registryFile)
    print(f"Schema Registry server running on port {args.http}.")

    doers = [httpServerDoer]

    tock = 0.03125
    doist = doing.Doist(limit=0.0, tock=tock, real=True)
    doist.do(doers=doers)


def main():
    args = parser.parse_args()
    launch(args)


if __name__ == "__main__":
    main()