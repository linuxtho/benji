"""benji -- A module-based IRC Robot

Usage:
    benji [-c=<config_file>]
    benji (-h | --help)
    benji --version

Options:
    -c=<config_file>    benji.yml config file [default: /etc/benji.yml]
    -h --help           Show this screen
    --version           Show version

"""
import os
import sys

from docopt import docopt

import benji


def main():
    args = docopt(__doc__)

    if args.get('--version'):
        print("Benji IRC Robot v{0}".format(benji.VERSION))
        sys.exit(os.EX_OK)

    print(args)

    config = benji.config.load_config(args['-c'])
    bot = benji.bot.BenjiBot(**config)
    bot.start()
