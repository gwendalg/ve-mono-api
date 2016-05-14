"""
apcaccess.__main__

Provides the command-line functionalty similar to the original apcaccess cmd.
"""

import argparse
import logging
import vemonostrip


if __name__ == "__main__":
    # No need to use "proper" names on such simple code.
    # pylint: disable=invalid-name
    p = argparse.ArgumentParser()
    p.add_argument("--server", type=str, required=True)
    p.add_argument("--plug", type=int, default=0)
    p.add_argument("--op", type=str, choices=['set', 'get'])
    p.add_argument("--value", type=str, choices=['on', 'off', 'state', 'watts'])
    args = p.parse_args()
    plug = vemonostrip.VeMonoStrip(args.server, args.plug)
    if args.op == 'get':
        try:
            result = plug.Get(args.value)
        except vemonostrip.VeMonoStripErr as e:
            logging.error(e)
            exit(1)
        print result
    else:
        try:
            result = plug.Set(args.value)
        except vemonostrip.VeMonoStripErr as e:
            logging.error(e)
